#include <linux/icmp.h>
#include <linux/ip.h>
#include <linux/kernel.h>
#include <linux/module.h>
#include <linux/netdevice.h>
#include <linux/netfilter.h>
#include <linux/netfilter_ipv4.h>
#include <linux/skbuff.h>
#include <linux/tcp.h>
#include <linux/udp.h>
#include <net/ip.h>
#include <net/net_namespace.h>

static const struct {
	__be32 dns_address;
	u16 dns_port;
	__be32 vm_address;
	u16 telnet_port;
} policy = {
	.dns_address = cpu_to_be32(0x08080808), /* 8.8.8.8 */
	.dns_port = 53,
	.vm_address = cpu_to_be32(0x0a090001), /* 10.9.0.1 */
	.telnet_port = 23,
};

static unsigned int task = 2;
module_param(task, uint, 0444);
MODULE_PARM_DESC(task, "1: DNS block, 2: trace IPv4 hooks (default), 3: ping and Telnet block");

static unsigned int blockUDP(void *priv, struct sk_buff *skb,
			     const struct nf_hook_state *state)
{
	const struct iphdr *iph = ip_hdr(skb);
	struct udphdr buffer;
	const struct udphdr *udp;

	if (iph->protocol != IPPROTO_UDP || iph->daddr != policy.dns_address ||
	    (iph->frag_off & htons(IP_OFFSET)))
		return NF_ACCEPT;

	udp = skb_header_pointer(skb, skb_network_offset(skb) + ip_hdrlen(skb),
				 sizeof(buffer), &buffer);
	if (!udp || udp->dest != htons(policy.dns_port))
		return NF_ACCEPT;

	pr_info_ratelimited("seedFilter: Dropping %pI4 (UDP), port %u\n",
			    &iph->daddr, policy.dns_port);
	return NF_DROP;
}

static bool targets_vm(const struct iphdr *iph,
		       const struct nf_hook_state *state)
{
	return iph->daddr == policy.vm_address &&
	       !(state->in->flags & IFF_LOOPBACK);
}

static unsigned int blockPing(void *priv, struct sk_buff *skb,
			      const struct nf_hook_state *state)
{
	const struct iphdr *iph = ip_hdr(skb);
	struct icmphdr buffer;
	const struct icmphdr *icmp;

	if (iph->protocol != IPPROTO_ICMP || !targets_vm(iph, state))
		return NF_ACCEPT;

	icmp = skb_header_pointer(skb, skb_network_offset(skb) + ip_hdrlen(skb),
				  sizeof(buffer), &buffer);
	if (!icmp || icmp->type != ICMP_ECHO)
		return NF_ACCEPT;

	pr_info_ratelimited("seedFilter: Dropping ICMP Echo Request %pI4 -> %pI4\n",
			    &iph->saddr, &iph->daddr);
	return NF_DROP;
}

static unsigned int blockTelnet(void *priv, struct sk_buff *skb,
				const struct nf_hook_state *state)
{
	const struct iphdr *iph = ip_hdr(skb);
	struct tcphdr buffer;
	const struct tcphdr *tcp;

	if (iph->protocol != IPPROTO_TCP || !targets_vm(iph, state))
		return NF_ACCEPT;

	tcp = skb_header_pointer(skb, skb_network_offset(skb) + ip_hdrlen(skb),
				 sizeof(buffer), &buffer);
	if (!tcp || tcp->dest != htons(policy.telnet_port))
		return NF_ACCEPT;

	pr_info_ratelimited("seedFilter: Dropping TCP %pI4 -> %pI4, port %u\n",
			    &iph->saddr, &iph->daddr, policy.telnet_port);
	return NF_DROP;
}

static unsigned int printInfo(void *priv, struct sk_buff *skb,
			      const struct nf_hook_state *state)
{
	const struct iphdr *iph = ip_hdr(skb);
	const char *hook;
	const char *protocol;

	switch (state->hook) {
	case NF_INET_PRE_ROUTING:
		hook = "PRE_ROUTING";
		break;
	case NF_INET_LOCAL_IN:
		hook = "LOCAL_IN";
		break;
	case NF_INET_FORWARD:
		hook = "FORWARD";
		break;
	case NF_INET_LOCAL_OUT:
		hook = "LOCAL_OUT";
		break;
	case NF_INET_POST_ROUTING:
		hook = "POST_ROUTING";
		break;
	default:
		hook = "UNKNOWN";
		break;
	}

	switch (iph->protocol) {
	case IPPROTO_UDP:
		protocol = "UDP";
		break;
	case IPPROTO_TCP:
		protocol = "TCP";
		break;
	case IPPROTO_ICMP:
		protocol = "ICMP";
		break;
	default:
		protocol = "OTHER";
		break;
	}

	pr_info("seedFilter: %s %pI4 -> %pI4 (%s)\n",
		hook, &iph->saddr, &iph->daddr, protocol);

	return NF_ACCEPT;
}

#define IPV4_HOOK(callback, point) { \
	.hook = (callback),          \
	.hooknum = (point),          \
	.pf = NFPROTO_IPV4,          \
	.priority = NF_IP_PRI_FIRST, \
}

static const struct nf_hook_ops dns_hooks[] = {
	IPV4_HOOK(printInfo, NF_INET_LOCAL_OUT),
	IPV4_HOOK(blockUDP, NF_INET_POST_ROUTING),
};

static const struct nf_hook_ops trace_hooks[] = {
	IPV4_HOOK(printInfo, NF_INET_PRE_ROUTING),
	IPV4_HOOK(printInfo, NF_INET_LOCAL_IN),
	IPV4_HOOK(printInfo, NF_INET_FORWARD),
	IPV4_HOOK(printInfo, NF_INET_LOCAL_OUT),
	IPV4_HOOK(printInfo, NF_INET_POST_ROUTING),
};

static const struct nf_hook_ops vm_hooks[] = {
	IPV4_HOOK(blockPing, NF_INET_LOCAL_IN),
	IPV4_HOOK(blockTelnet, NF_INET_LOCAL_IN),
};

static const struct {
	const struct nf_hook_ops *hooks;
	unsigned int count;
} task_hooks[] = {
	[1] = { dns_hooks, ARRAY_SIZE(dns_hooks) },
	[2] = { trace_hooks, ARRAY_SIZE(trace_hooks) },
	[3] = { vm_hooks, ARRAY_SIZE(vm_hooks) },
};

static int __init registerFilter(void)
{
	if (task == 0 || task >= ARRAY_SIZE(task_hooks)) {
		pr_err("seedFilter: task must be 1, 2 or 3\n");
		return -EINVAL;
	}

	return nf_register_net_hooks(&init_net, task_hooks[task].hooks,
				     task_hooks[task].count);
}

static void __exit removeFilter(void)
{
	nf_unregister_net_hooks(&init_net, task_hooks[task].hooks,
				task_hooks[task].count);
}

module_init(registerFilter);
module_exit(removeFilter);

MODULE_LICENSE("GPL");
MODULE_DESCRIPTION("SEED lab Task 1.B IPv4 Netfilter firewall");
