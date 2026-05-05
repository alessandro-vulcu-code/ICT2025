# Chapter 6 - Analysis of the GoBackN Protocol

## Table of Contents

- [[#6.0.1 Markov packet errors - Error free feedback|6.0.1 Markov packet errors - Error free feedback]]
- [[#6.0.2 Bidirectional Markov packet errors - 4 states model|6.0.2 Bidirectional Markov packet errors - 4 states model]]
- [[#6.0.3 Bidirectional Markov packet errors - 3 states model|6.0.3 Bidirectional Markov packet errors - 3 states model]]
- [[#6.0.4 Bidirectional Markov packet errors - 2 states model|6.0.4 Bidirectional Markov packet errors - 2 states model]]
- [[#6.1 Counting processes and their statistics|6.1 Counting processes and their statistics]]
  - [[#6.1.1 Transform methods for recursive equations|6.1.1 Transform methods for recursive equations]]
  - [[#6.1.2 Generalization|6.1.2 Generalization]]
- [[#6.1.3 GoBackN protocol - Transform approach|6.1.3 GoBackN protocol - Transform approach]]
- [[#6.1.4 GoBackN protocol - Generalization|6.1.4 GoBackN protocol - Generalization]]
- [[#Analytical Index|Analytical Index]]
- [[#Summary Table|Summary Table]]

---

The GoBackN Protocol is a data transmission protocol which sends data in packets of some bits through a channel. There is in addition an other channel implemented for reliability and control: for every packet the sender is notified whether the packet has been correctly received. If so, transmission is successful. In the other case, so if the packet is either lost or corrupted, then a negative acknowledgment requests the sender for another transmission. It is a very common protocol in networks, and it is useful because it permits to deal with errors by retransmitting the corrupted data.

GoBackN protocol is particularly designed for accepting packets in order. So, if a packet is either lost or corrupted, then it will need to be retransmitted. Because of the design, it will be needed to retransmit sequentially the following packets regardless whether there were errors concerning it. A sketch for this protocol is shown in the figure below (6.1).

![[Stochastic_Processes_2020_p227_img87.jpeg]]
*Figure 6.1 - Representation of a possible evolution GoBackN protocol: once the sender is notified that a packet is corrupted, it goes back to that packet and retransmits it again followed by its consecutive, ordered packets. A packet, identified by the number above, may be successfully received (0) or may contain an error (1) and therefore the necessity to send it again. In this particular case, the Roundtrip time is equal to  $N = 3$ .*

Usually, when designing a GoBackN, we define  $N$  as the Roundtrip time, i.e. the number of time steps after which the sender is notified about an eventual error. As a consequence, every time a channel at time  $t$  has an error, its packet will be sent again at time  $t + N$ . Note as in the interval of time  $(t + 1, t + N - 1)$  the sender has not been notified about the bad channel yet, and so keeps sending packets until it receives the acknowledgment that there has been an error. From that moment on, it will resume the transmission sequentially starting from that specific packet that was incorrect. We assume, for sake of simplicity, that there are always packets to be sent, and so there are no empty slots.

There might be other protocols, with referral to image (6.1) we could for example retransmit only the packet corrupted, that are 3, 4, and then resume the transmission from the last packet it has successfully received. This is called Selective Repeat. It is indeed more efficient, since we do not need to send packets that were correctly delivered more than once. This requires in addition the faculty for the receiver to be able to accept packets out of order, finally reordering them, once the complete sequence has been dispatched successfully up to the last channel. Then the transmission starts again.

This is not what GoBackN does, so to keep the receiver simple. In fact it does not accept packets out of order, and moreover when packets have a sequence different from the expected one, they are simply rejected as for the ($X$) in the image above (6.1). We can see that every time there is an error, the sequence restarts from the appropriate time. If this happens, once the incorrect packet has been sent, the subsequent $N-1$ channels will be retransmitted no matter whether they have been successfully transmitted, and so they are at first ignored. In each time slot, the channel may be in two different states: good (0), or bad (1).

On the other hand, from the point of view of the protocol. not all slots contain the so called throughput opportunities. A throughput opportunity is defined as the average number of successful packets received and accepted by the protocol per slot. A slot can therefore be a throughput opportunity when, if the slot is good, that packet is counted as a success. With referral to image (6.1) first three packets are throughput opportunities, while the fourth and the fifth are not. Note that the third one actually is a throughput opportunity: despite the fact that the packet is not correct, it still has been received as well as accepted. Given the bad transmission, fourth and fifth ones indeed are not accepted, regardless their channel state. because of the protocol and so they are not throughput opportunities. For the point of view of the protocol packets fourth and fifth do not even exist, since only the retransmitted ones will be considered. What the protocol sees is not every single slot, but every slot as long as the transmission is successful. When an error occurs, it will skip $N-1$ slots and look at the channel $N$ slots later. We can see it as a sampling rule: every time there is a success, then sample at the very next slot. Whereas if a failure occurs, then sample $N$ slots later. Sampled slots will be indeed the only slots seen by the protocol. In the computation of throughput opportunity, and so the efficiency of our protocol, we will count then all packets received and accepted normalized by the number of all packets sent, regardless they were correct/wrong or had been skipped or accepted.

This is a very simple data transmission protocol. It is common use in networking courses to study a protocol by adding some errors in i.i.d. channels, according to some probability and independently, and see how the system behaves. Even though there is some memory in our process, let us still assume that we can model our system by using a 2-state Markov chain which are 0 and 1. There may be also a certain distribution that describes how these states are distributed statistically. We will now try to find the throughput of this protocol using several ways and for different cases, where in all of them Markov errors


will be present. Models will differ by the feedback behavior, that is to say the acknowledgements that the sender receives, that might be either perfect (no error) or subject to errors, that in turn might be Markov or independent.

> [!Important] Definition - GoBackN Throughput Opportunity
> **Statement:** A slot is a throughput opportunity when, if the channel is good, the corresponding packet is counted as successfully received and accepted by the protocol. After an error, GoBackN skips the following $N-1$ slots from the protocol point of view and samples again $N$ slots later.
>
> **Intuition:** The physical channel has one state per slot, but the protocol observes only the slots that matter for accepted in-order delivery. Throughput is therefore a reward per real transmitted slot, not simply the fraction of good channel states.

## 6.0.1 Markov packet errors - Error free feedback

Let us consider the GoBackN protocol on a Markov channel, where data packet errors follow a two-state Markov chain. Transmissions may be either be $0$ for good channel or $1$ for bad channels. Acknowledgments are error-free and the round-trip of the system is $m$ slots. This means that if a packed transmitted in slot $t$ is corrupted, the sender will be notified by the end of slot $t+m-1$ and the packet will be retransmitted in slot $t+m$.
Let the two-channel matrix be:

$$
\mathbf{C}=\begin{bmatrix}p_{00}&p_{10}\\
p_{10}&p_{11}\end{bmatrix}
$$

whose entries are the transition probabilities for good and bad states. Note as if a channel is good, then the system will look at the very next slot, whose state will depend of the transition probabilities shown in $\mathbf{C}.$ Whereas if a channel is bad, the next time the protocol will look at the channel will be $m$ slots later. The transition probability we need to consider for this case is therefore different, namely the $m$-step transition probability.
These probabilities are given by:

$$
\mathbf{C}^{m}=\begin{bmatrix}p_{00}(m)&p_{10}(m)\\
p_{10}(m)&p_{11}(m)\end{bmatrix}
$$

From the point of view of the protocol operation, this channel is sampled every slot when transmissions are correct, and once every $m$ slots when errors occur. Therefore, every time state $\mathbf{0}$ is visited, one success is counted (one packet was indeed correctly delivered) and the time spent in that state before the next transition is $\mathbf{1}$ slot. On the other hand, when we visit state $1$ (bad channel), no successes are counted and the time spent in that state before the next transition is $m$ slots.
Accordingly, the transition probabilities from each state are taken either from $\mathbf{C}$ or $\mathbf{C}^{m}$ depending on the time spent, so that the transition matrix for the protocol model is:

$$
\mathbf{P}=\begin{bmatrix}p_{GG}(m)&p_{GB}(m)\\
p_{BG}(m)&p_{BB}(m)\end{bmatrix}=\begin{bmatrix}p_{00}&p_{10}\\
p_{10}(m)&p_{11}(m)\end{bmatrix}
$$

whereas the time $T$ and reward $R$ (success) metrics in the two states are:

$T_{G}=1\quad T_{B}=m\quad R_{G}=1\quad R_{B}=0$ (6.2)

Note as when we have a bad channel, we must take into account that we spend


![[Stochastic_Processes_2020_p230_img88.jpeg]]
*Figure 6.2 -  Protocol may be either in a good state (good channel) or in a bad state (bad channel). In the first case, reward and time metrics will be both one. On the other hand, if the channel is bad, the reward will be null and the time will be $m$ time slots. Transition probabilities between these states are either one-step or $m$-step, according to which channel we are in, as stated in (6.1)*

$m$ time slots in the bad state, and therefore draw our transition probabilities from the $m$-step transition matrix $\mathbf{C}^m$. All what is depicted in figure (6.2) defines a complete, despite very simple, semi-Markov model with rewards. We can find the embedded Markov-chain that looks only at the transition probabilities between states in $\mathbf{P}$. In addition there is the time distribution: it is equal for all transition probabilities leaving a same state, namely 1 for the good state, and $m$ for the bad one. Finally there is an other metric, the reward metric, that counts the number of successes we have. We can therefore ask ourselves to compute, in the long run, what is the average reward/successes per unit time: namely the throughput.

In order to compute the throughput we need first to find the limiting probabilities for the embedded Markov chain, and then apply the results we have found for the renewal reward theory. Given the transition probability $\mathbf{P}$, the limiting probabilities for a two states Markov chain are proportional to the probability of moving into that state from the others. So:

> [!Important] Result - GoBackN Throughput with Markov Packet Errors and Error-Free Feedback
> **Statement:** For the two-state Markov packet-error channel with error-free feedback and round-trip time $m$, the GoBackN throughput is:
>
> $$
> \eta=\frac{p_{10}(m)}{p_{10}(m)+mp_{01}}.
> $$
>
> In the i.i.d. error case with error probability $\epsilon$:
>
> $$
> \eta_{iid}=\frac{1-\epsilon}{1-\epsilon+m\epsilon}.
> $$
>
> **Proof:** The complete derivation through embedded Markov-chain stationary probabilities and renewal reward theory is transcribed below.
>
> **Intuition:** A good sampled slot gives one packet in one slot; a bad sampled slot gives no packet and consumes $m$ slots before the protocol can sample the channel again.

$$
\pi_G = \frac{p_{10}(m)}{p_{01} + p_{10}(m)} \quad \pi_B = \frac{p_{01}}{p_{01} + p_{10}(m)} \tag{6.3}
$$

and, if $R(t)$ counts the number of successful packets in $[0,t]$, the protocol throughput is given by the limit:

$$
\lim_{t \to \infty} \frac{R(t)}{t}
$$

We know this, from the theory of rewards-renewal processes, to be equal with probability 1 to:

$$
\lim_{t \to \infty} \frac{R(t)}{t} = \eta = \frac{\pi_G R_G + \pi_B R_B}{\pi_G T_G + \pi_B T_B} = \frac{p_{10}(m)}{p_{10}(m) + m p_{01}} \quad \text{w.prob. 1}
$$

that is the final expression for the throughput. We simply substituted the values we have just found in (6.3) for $\pi_G$ and $\pi_B$ and in (6.2) for $T$'s and $R$'s. This last expression is measured in unit of (packets/slot).

A special case is when errors are i.i.d. with probability $\epsilon$, and so $\mathbf{C}$ and the


throughput becomes:

$\mathbf{C}=\mathbf{C}^{m}=\begin{bmatrix}1-\epsilon&\epsilon\cr 1-\epsilon&\epsilon\end{bmatrix}\qquad\eta_{iid}=\frac{1-\epsilon}{1-\epsilon+m\epsilon}$ (6.4)

We can note that the probability of going to a *good* state, i.e. where the second index is 0, is always $1-\epsilon$. Whereas the probability to go to a bad state denoted by the second index equal to 1, is always $\epsilon$.

These last results could have been derived invoking renewal theory. Recall from (6.2) that *every time we land into state $G$* we obtain *1 reward*, moreover this is a *renewal time* being it a Markov chain. The evolution of the process will therefore restart as if from scratch every time we land in this state, and so a new *cycle* will restart and last until we come back to $G$ again. Each of these renewal cycle will contain exactly *one* reward, since we can visit state $G$ only once per cycle. The *average duration* of a renewal cycle *will be* obviously the average return time to this state, namely *the average recurrence time*. Putting together the information about the number of rewards per cycle (one) and its average duration, we can compute the throughput as the ratio between these quantities.

In order to find the average recurrence time, we use the *first-step analysis* and we evaluate the duration of all transitions that bring us back to $G$ and their probabilities. For these computations, recall that the time we spend in a state is a geometric random variable whose mean is the inverse of the probability of leaving the state, in this case $(p_{10}(m))^{-1}$. We must pay attention moreover that this transition takes exactly $m$ time steps, and so the mean we are looking for is $m/p_{10}(m)$. In formulas:

$m=1\cdot p_{00}+p_{01}\left[1+\frac{m}{p_{10}(m)}\right]=1+\frac{mp_{01}}{p_{10}(m)}$

where $p_{00}+p_{10}=1$.

The *throughput* (average fraction of time spent in state $G$) is then:

$\eta=P_{G}=\lim_{t\rightarrow\infty}P[Z(t)=G|Z(0)=i]=m_{G}^{-1}=\frac{p_{10}(m)}{p_{10}(m)+mp_{01}}$

as we already found before.

## 6.0.2 Bidirectional Markov packet errors - 4 states model

Now we suppose that errors can occur in the reverse direction as well: i.e. the feedback channel might not successfully transmit the data. We now assume that the error process for the feedback channel is a Markov process, whose possible states are either 1 *bad transmission*, or 0 *good transmission*. These states are labelled as $q_{ij}$ and are different from the $p_{kl}$ that correspond to the transmission channel: indeed they are two different channels that transmit two different kind of packets, whose data may be different in length and encoding as well. Therefore the error structure is not *the same one in both directions*.


We now need to take into account all the possible combinations for data channel and feedback channel. That is, for  $q_{ij}$  the subscript  $i$  corresponds to the success of the transmission, while the  $j$  to the correctness of the acknowledgment. The process can be depicted as follows:

![[Stochastic_Processes_2020_p232_img89.jpeg]]
*Figure 6.3 - Graphical representation for the 4-states GoNBack protocol. These 4 states a cover all possible combinations for the success/failure for transmissions of the packets and successive acknowledgments. Consequently the only state that denotes a success and therefore a reward is the  $(0,0)$  one.*

$q_{00}$  denotes a packet successfully transmitted, and acknowledgment correctly received, whereas in  $q_{11}$  both of them are bad channels.

$q_{10}$  instead refers to a packet that is in error, but the acknowledgement is correct, while  $q_{01}$  viceversa.

The only state that corresponds to a success can be only  $q_{00}$ , whose time duration associated is 1 slot, whereas the other ones will denote a failure. In the case there is a failure in some data channel, we know that the corresponding feedback will be received  $m$  time slots later. The time associated to all transitions going out of these three states will be therefore  $m$ : the corresponding transition probabilities will be computed according to the  $m$  steps in both directions.

The transition probability matrix for this protocol will be:

|   | (0,0) | (0,1) | (1,0) | (1,1)  |
| --- | --- | --- | --- | --- |
|  P = | (0,0) | p00q00 | p00q01 | p01q00  |
|   |  (0,1) | p00(m)q10(m) | p00(m)q11(m) | p01(m)q10(m)  |
|   |  (1,0) | p10(m)q00(m) | p10(m)q01(m) | p11(m)q00(m)  |
|   |  (1,1) | p10(m)q10(m) | p10(m)q11(m) | p11(m)q10(m)  |

Note as the first row, corresponding to the success state, has all 1-step transition probabilities. Whereas the other rows are made up of  $m$ -step transition probabilities, according to what we said before.

Therefore the structure shown in (6.2), and the just written transition probability matrix and the metrics of reward/failure provide the complete semi-Markov model for this special protocol, where Markov errors can occur in both directions. We can use now the formula (5.24) applied to our problem: we choose the second metric to be the time.


The average throughput is then obtained in the limit as:

> [!Important] Result - Four-State Bidirectional Markov Error Model
> **Statement:** When both data and feedback channels have Markov errors, the four-state model has throughput:
>
> $$
> \eta = \frac {\pi_ {(0 , 0)}}{\pi_ {(0 , 0)} + m (1 - \pi_ {(0 , 0)})}.
> $$
>
> **Intuition:** Only state $(0,0)$ contributes reward and consumes one slot; all other states are failures and consume $m$ slots.

$$
\eta = \frac {\sum_ {i} \pi_ {i} R _ {i}}{\sum_ {i} \pi_ {i} T _ {i}} = \frac {\pi_ {(0 , 0)}}{\pi_ {(0 , 0)} + m (1 - \pi_ {(0 , 0)})}
$$

In the numerator the only non-null term is for the state  $(0,0)$ , and so  $R_{(0,0)} = 1$ . In the denominator we have that  $T_{(0,0)} = 1$  with probability  $\pi_{(0,0)}$ , while for the other states we will have that  $T = m$  with probability  $1 - \pi_{(0,0)}$ .

For this case we will not express  $\pi_{(0,0)}$  in a closed form, being the computations very tedious. We would indeed need to solve the stationary equations for (6.5) numerically, then find  $\pi_{(0,0)}$  and finally the average throughput.

## 6.0.3 Bidirectional Markov packet errors - 3 states model

Let us now consider a special case where the feedback channel has i.i.d. errors with probability  $\delta$ , but states are the same ones in  $\mathbf{C}$  matrix.

We can now split state  $G$  into two different states: in order to explicitly distinguish the cases with correct  $(G_0)$  and erroneous feedback  $(G_1)$ , respectively.

We note as  $G_0$  corresponds to state  $(0,0)$  of the figure (6.5), whereas  $G_1$  relates to state  $(0,1)$  of the same picture: despite the success in the transmission of the packet, there is an error in the acknowledgement.  $B$  does not need to be split: regardless the feedback state, it remains a failure. Moreover since errors are i.i.d., the next feedback state will have the same probability as the previous ones and so it does not depend on the previous feedbacks.

![[Stochastic_Processes_2020_p233_img90.jpeg]]
*Figure 6.4 - Representation of the embedded Markov chain for the 3-states model for GoBackN protocol, where feedback errors are i.i.d. We note as the state  $B$  is not split,  $G_{0}$  corresponds to a success, while  $G_{1}$  to a failure.*

Starting from  $G_{0}$  we know both packet and acknowledgement were correct, and we may stay there if both transmission and feedback are again correct with probability respectively  $p_{00}$  and  $1 - \delta$ . In the case that feedback is not correct (prob.  $\delta$ ) while acknowledgement is not (prob.  $p_{00}$ ) we go to  $G_{1}$ , from where we will leave in  $m$  steps depending on the goodness of data and feedback channels.

This picture can be obtained both from (6.2) and (6.5). In the first case we split  $G$  into  $G_{0}$  and  $G_{1}$ . In the second case, states  $(1,0)$  and  $(1,1)$  can be combined into a whole state  $B$  since there is no need to keep memory on the previous feedback state. As before, for the success state  $G_{0}$  we have 1 reward and 1 slot, while for the bad channels  $G_{1}$  and  $B$  we have no reward and  $m$  time


slots. We can solve the Markov chain whose transition matrix is:

$$
\mathbf {P} = \begin{array}{l l l l} & G _ {0} & G _ {1} & B \\ G _ {0} & (1 - \delta) p _ {0 0} & \delta p _ {0 0} & p _ {0 1} \\ G _ {1} & (1 - \delta) p _ {0 0} (m) & \delta p _ {0 0} (m) & p _ {0 1} (m) \\ B & (1 - \delta) p _ {1 0} (m) & \delta p _ {1 0} (m) & p _ {1 1} (m) \end{array}
$$

and compute the throughput recalling that:

> [!Important] Result - Three-State Model with i.i.d. Feedback Errors
> **Statement:** When feedback errors are i.i.d. with probability $\delta$, the three-state model gives:
>
> $$
> \eta = \frac {(1 - \delta) p _ {1 0} (m)}{[ (1 - \delta) p _ {0 1} + \delta p _ {0 1} (m) + \delta p _ {1 0} (m) ] m + (1 - \delta) p _ {1 0} (m)}.
> $$
>
> **Proof:** The stationary-equation derivation for $\pi_{G_0}$ and the substitution into (6.6) are transcribed below.
>
> **Intuition:** A successful data packet contributes throughput only if the feedback is also correct; otherwise the protocol spends $m$ slots recovering.

$$
R _ {G _ {0}} = 1 \quad R _ {G _ {1}} = R _ {B} = 0 \qquad T _ {G _ {0}} = 1 \quad T _ {G _ {1}} = T _ {B} = m
\eta = \frac {\pi_ {G _ {0}}}{\pi_ {G _ {0}} + m (1 - \pi_ {G _ {0}})} \tag {6.6}
$$

Solving the stationary equations  $\vec{\pi} = \vec{\pi}\mathbf{P}$  we find, for the first equations:

$$
\pi_{G_0} = \pi_{G_0} (1 - \delta) p_{00} + \pi_{G_1} (1 - \delta) p_{00} (m) + \pi_{B} (1 - \delta) p_{10} (m) \tag{6.7}
$$

$$
\pi_{G_1} = \pi_{G_0} \delta p_{00} + \pi_{G_1} \delta p_{00} (m) + \pi_{B} \delta p_{10} (m) \tag{6.8}
$$

Note that the first and the second column of the transition matrix are the same one in terms of  $p$ 's, except for the factors  $(1 - \delta)$  and  $\delta$ . Therefore the right hand sides of (6.8) are proportional according to  $\delta / (1 - \delta)$ .

We can compute then the ratio between  $\pi_{G_0}$  and  $\pi_{G_1}$  and find:

$$
\pi_ {G _ {1}} = \frac {\delta}{1 - \delta} \pi_ {G _ {0}} \tag {6.9}
$$

and, from the normalization condition retrieve  $\pi_B$ :

$$
\pi_ {B} = 1 - \pi_ {G _ {0}} - \pi_ {G _ {1}} = 1 - \pi_ {G _ {0}} - \frac {\delta}{1 - \delta} \pi_ {G _ {0}} = 1 - \frac {\pi_ {G _ {0}}}{1 - \delta} \tag {6.10}
$$

Therefore, we have from rewriting (6.9) and (6.10):

$$
(1 - \delta) \pi_ {G _ {1}} = \delta \pi_ {G _ {0}} \qquad (1 - \delta) \pi_ {B} = 1 - \delta - \pi_ {G _ {0}}
$$

Using these last two expressions in (6.8):

$$
\pi_ {G _ {0}} = \pi_ {G _ {0}} (1 - \delta) p _ {0 0} + \delta \pi_ {G _ {0}} p _ {0 0} (m) + (1 - \delta - \pi_ {G _ {0}}) p _ {1 0} (m)
\pi_ {G _ {0}} (1 - (1 - \delta)) p _ {0 0} - \delta p _ {0 0} (m) + p _ {1 0} (m)) = (1 - \delta) p _ {1 0} (m)
$$

and using  $p_{00} = 1 - p_{01}$  and  $p_{00}(m) = 1 - p_{01}(m)$  we obtain:

$$
\pi_ {G _ {0}} = \frac {(1 - \delta) p _ {1 0} (m)}{(1 - \delta) p _ {0 1} + \delta p _ {0 1} (m) + p _ {1 0} (m)}
$$


while:

$$
\begin{array}{l} 1 - \pi_ {G _ {0}} = 1 - \frac {(1 - \delta) p _ {1 0} (m)}{(1 - \delta) p _ {0 1} + \delta p _ {0 1} (m) + p _ {1 0} (m)} = \\ \frac {(1 - \delta) p _ {0 1} + \delta p _ {0 1} (m) + p _ {1 0} (m)}{(1 - \delta) p _ {0 1} + \delta p _ {0 1} (m) + p _ {1 0} (m)} \\ \end{array}
$$

We can substitute these two expressions for  $\pi_{G_0}$  and  $1 - \pi_{G_0}$  in (6.6), where we care only about the numerator since the denominator is equal for the just mentioned expressions and therefore cancels, finally obtaining the throughput:

$$
\eta = \frac {(1 - \delta) p _ {1 0} (m)}{[ (1 - \delta) p _ {0 1} + \delta p _ {0 1} (m) + \delta p _ {1 0} (m) ] m + (1 - \delta) p _ {1 0} (m)} \tag {6.11}
$$

## 6.0.4 Bidirectional Markov packet errors - 2 states model

Since there is no need to keep memory of the feedback channel state (as feedback errors are i.i.d.), the same protocol can be represented with only two states, i.e.  $G$  and  $B$ . By splitting  $G$  we make the good transmission channel to be deterministic: we can know deterministically whether there will be either the reward and how much time passes depending on which state we are, so  $G_0$  or  $G_1$ , and therefore the goodness of the feedback. We can merge these two states, with the consequence that a visit to this state may return different outcomes with different probabilities.

![[Stochastic_Processes_2020_p235_img91.jpeg]]
*Figure 6.5 - Representation of the embedded Markov chain for the 2-states model for GoBackN protocol, where feedback errors are i.i.d.*

When we visit state  $G$  we may have either a reward with probability  $(1 - \delta)p_{00}$  or not with probability  $\delta p_{00}(m)$  depending on the feedback. The two states now have been merged, and so the outcome is probabilistic.

We know eventually how to threat these semi-Markov processes from the theory, where rewards follow a certain distribution. Visit to  $B$  is always a failure.

In summary, for a visit to state  $G$  we have:

- reward: 1 with prob.  $(1 - \delta)$  and 0 with prob.  $\delta$ , average  $R_{G} = (1 - \delta)$
- time: 1 with prob.  $(1 - \delta)$  and m with prob.  $\delta$ , average  $T_{G} = (1 - \delta) + m\delta$
- transition to  $\mathrm{G}$  with prob.  $(1 - \delta)p_{00} + \delta p_{00}(m)$
- transition to B with prob.  $(1 - \delta)p_{01} + \delta p_{01}(m)$

whereas for a visit to state  $B$  we have that:

- no reward:  $R_{B} = 0$


time: always $m$, $T_{B}=m$
- transition to G with prob. $p_{10}(m)$
- transition to B with prob. $p_{11}(m)$

All this scheme defines entirely our semi-Markov model. Equivalently it can be expressed in the following forms:

$\mathbf{P}=\left\lVert(1-\delta)p_{00}+\delta p_{00}(m)\quad(1-\delta)p_{01}+\delta p_{01}(m)\right\rVert$ (6.12)

and the reward and time vectors are:

$\mathbf{R}=\binom{R_{G}}{R_{B}}=\binom{1-\delta}{0}\qquad\mathbf{T}=\binom{T_{G}}{T_{B}}=\binom{1-\delta+m\delta}{m}$

Now we need to compute the throughput $\eta=\frac{\sum_{i}\pi_{i}R_{i}}{\sum_{i}\pi_{i}T_{i}}=\frac{\pi_{G}R_{G}+\pi_{B}R_{B}}{\pi_{G}T_{G}+\pi_{B}T_{B}}$.
$\pi$’s are the limiting probabilities for the matrix (6.12), and keeping in mind the direct formula for the limiting probabilities for a two states Markov chain:

$\pi_{G}$ $=\frac{p_{10}(m)}{p_{10}(m)+(1-\delta)p_{01}+\delta p_{01}(m)}$
$\pi_{B}$ $=\frac{(1-\delta)p_{01}+\delta p_{01}(m)}{p_{10}(m)+(1-\delta)p_{01}+\delta p_{01}(m)}$

Finally the throughput:

> [!Important] Result - Two-State Model Equivalent to the Three-State Model
> **Statement:** The merged two-state semi-Markov model gives:
>
> $$
> \eta=\frac{(1-\delta)p_{10}(m)}{(1-\delta+m\delta)p_{10}(m)+m[(1-\delta)p_{01}+\delta p_{01}(m)]}.
> $$
>
> In the i.i.d. data-error case with probability $\epsilon$:
>
> $$
> \eta_{iid}=\frac{(1-\delta)(1-\epsilon)}{(1-\delta)(1-\epsilon)+m[1-(1-\delta)(1-\epsilon)]}.
> $$
>
> **Intuition:** The two-state and three-state models describe the same protocol; merging states moves uncertainty from the state label into the reward/time distributions.

$\eta$ $=\frac{\pi_{G}R_{G}+\pi_{B}R_{B}}{\pi_{G}T_{G}+\pi_{B}T_{B}}=\frac{(1-\delta)\pi_{G}}{(1-\delta+m\delta)\pi_{G}+m(1-\pi_{G})}=$
$=\frac{(1-\delta)p_{10}(m)}{(1-\delta+m\delta)p_{10}(m)+m[(1-\delta)p_{01}+\delta p_{01}(m)]}$

that is equal to (6.11), as expected: two models that represent the same system must return the same values, despite they might be different.
If we consider the case where also errors in data channel are i.i.d. with probability $\epsilon$, we replace $p_{01}$ and $p_{01}(m)$ with $\epsilon$, and $p_{10}(m)$ with $1-\epsilon$, then throughput becomes:

$\eta_{iid}$ $=\frac{(1-\delta)(1-\epsilon)}{(1-\delta+m\delta)(1-\epsilon)+m[(1-\delta)\epsilon+\delta\epsilon]}$
$=\frac{(1-\delta)(1-\epsilon)}{(1-\delta)(1-\epsilon)+m[1-(1-\delta)(1-\epsilon)]}$

Comparing this last result with (6.4), we recognize that a system with i.i.d. errors in both directions with probabilities of success $1-\epsilon$ and $1-\delta$, respectively, is equivalent to a system with error-free feedback in which the success probability on the direct channel is the product of the two,


i.e. $(1-\epsilon)(1-\delta)$. In other words, if we have i.i.d. errors in both directions, as long as the product of the two rates is the same, then the specific probabilities are not important. We can therefore assign "all" the error rate to a direction, and set it equal to the product computed before. Doing so, we obtain a system that is equivalent. We can even slightly change the weights of probabilities and find an other equivalent system, as long as the product remains constant.

## 6.1 Counting processes and their statistics

We will now study a new argument that may seem unrelated from what we have just seen up to now. However, coming to a conclusion, we will note that our topics will be very similar to Markov models with metrics: this will allow us to use results we already know for renewal and semi-Markov processes.

We would like now to find the statistics of the number of successful slots up to time $n$. We assume the process is Markovian and binary, and so we denote:

$$
0 = \text{correct transmission} \quad 1 = \text{erroneous transmission}
$$

In other words we observe a sequence of $n$ consecutive states, and see how many of them are successful and how many are not.

Let us define the conditional probability that we observe $k$ good slots in time horizon of length $n$, and moreover we observe that the process is at state $j$ at time $n$ given it started in state $i$. We have four variables: $i$ sets the condition of where the chain started at time 0, whereas $j$ indicates the destination state at time $n$. The other two quantities introduced are $n$ that counts the total number of transitions we are considering, and $k$ which corresponds to how many visits we have made to the successful state. Formally:

$$
\phi_{ij}(k,n) = P[k \text{ good slots in } 0,1,...,n-1, \text{ } j \text{ in } n \mid i \text{ in } 0] \tag{6.13}
= P \left[ \sum_{m=0}^{n-1} \mathbb{1}\{X_m = 0\} = k, X_n = j \mid X_0 = i \right]
$$

where we count the number of visits in state 0 thanks to the indicator function.

We can solve it recursively, using a similar argument to the one we used for first-step analysis: we can exploit the Markov property to write recursive relationships. First we need to condition on last transition, and so at time $n-1$. We then try to find how a chain starting from state $i$ can visit at time $n$ the $j$-th state, having visited the 0 state a certain amount of times. By conditioning we mean that we must take into account that last state can be either $j \in \{0,1\}$.

In the first case, the last transition is a success and happens with probability $p_{0j}$, hence at time $n-1$ there must have been only $k-1$ visits to state 0 in order to reach the total of $k$ successes, and from this argument the factor $\phi_{i0}(k-1,n-1)$. On the other hand, if the last transition is to state 1


(i.e. a failure) with probability $p_{1j}$, at the very previous time step we must have visited the state $0$ all the times we are asked for, namely $k$, and the term $\phi_{i1}(k,n-1)$ follows.

In formulas:

> [!Important] Definition - Counting Distribution for Good Slots
> **Statement:** The quantity $\phi_{ij}(k,n)$ is the joint probability of seeing $k$ good slots in $0,1,\ldots,n-1$ and ending in state $j$ at time $n$, given initial state $i$.
>
> $$
> \phi_{ij}(k,n)
> =P\left[\sum_{m=0}^{n-1}\mathbb{1}\{X_m=0\}=k,\ X_n=j\mid X_0=i\right].
> $$
>
> **Intuition:** This augments the Markov-chain state distribution with a reward counter: state $0$ contributes one success, state $1$ contributes zero.

$\phi_{ij}(k,n)=\phi_{i0}(k-1,n-1)p_{0j}+\phi_{i1}(k,n-1)p_{1j}\quad n>0,\ k\leqslant n$ (6.14)

that is valid for all $n>0$ and for $k\leqslant n$ since we cannot have more successes than transitions.

We have found now the statistics at the $n$-th time step, i.e. $\phi_{ij}(k,{\bf n})$, in function of a similar statistics at the $n-1$-th time step, i.e. $\phi_{i0}(k-1,{\bf n-1})$ and $\phi_{i1}(k,{\bf n-1})$. This is indeed a recursive relation that allows us to go back in time up to the very first time step, where we hit the boundary condition. The boundary condition, for $n=0$, describes the situation where no transition can occur and so initial and ending states coincide. Therefore:

$$
\phi_{ij}(k,0)=\begin{cases}1&\text{for }i=j,k=0,n=0\\
0&\text{otherwise}\end{cases}=\delta_{ij}\delta(n)\delta(k)
$$

that tells us that the probability is $1$ only if states $i$ and $j$ coincide, meaning that no transition occurred ($n=0$) and consequently no success ($k=0$) as well.

We can rewrite this argument using Kronecker’s delta $\delta_{ij}$ and Dirac’s delta ($\delta(n)$ , $\delta(k)$) formalism, as stated above.

Moreover it holds that:

$$
\phi_{ij}(k,n)=0\qquad k<0\quad\text{or}\quad n<0\quad\text{or}\quad k>n
$$

because clearly it does not have any sense to make a negative number of transitions/successes, or have a number of successes larger than the number of transitions. Hence (6.14)+(6.15)+(6.16) completely define the statistics that we are looking for. First we note that (6.14) is zero for $n=0$, while (6.15) is not and so only the latter applies. Whereas when $n>0$ (6.14) applies, the other ones do not, being all of them $0$. We can sum them, since they refer to different cases, in order to consider all possible values for $n$:

$$
\phi_{ij}(k,n)=\phi_{i0}(k-1,n-1)p_{0i}+\phi_{i1}(k,n-1)p_{1j}+\delta_{ij}\delta(n)\delta(k)
$$

or taking into account that $i\in\{0,1\}$ and $j\in\{0,1\}$, we can arrange the $\phi_{ij}(k,n)$ in matricial form:

$$
\phi(k,n)=\begin{pmatrix}\phi_{00}(k,n)&\phi_{01}(k,n)\\
\phi_{10}(k,n)&\phi_{11}(k,n)\end{pmatrix}
$$

that in turn can be rewritten as the matrix equation, where we consider all possible combinations of values for $i$ and $j$ for the expression $\phi_{ij}(k,n)$


$\phi_{ij}(k,n)=\phi(k-1,n-1)\begin{pmatrix}p_{00}&p_{01}\cr 0&0\end{pmatrix}+\phi(k,n-1)\begin{pmatrix}0&0\cr p_{10}&p_{11}\end{pmatrix}+\delta(n)\delta(k)\hbox{\rm 1\hskip-2.84526pt1}_{2}$

Let us define the two following matrices:

$\mathbf{P}(0)=\begin{pmatrix}0&0\cr p_{10}&p_{11}\end{pmatrix}\qquad\mathbf{P}(1)=\begin{pmatrix}p_{00}&p_{01}\cr 0&0\end{pmatrix}$

And finally:

$\phi_{ij}(k,n)=\phi(k-1,n-1)\mathbf{P}(0)+\phi(k,n-1)\mathbf{P}(1)+\delta(n)\delta(k)\hbox{\rm 1\hskip-2.84526pt1}_{2}\qquad n\geqslant 0$ (6.18)

where we note that $\mathbf{P}(1)$ contains the *good* transitions that start from $0$, whereas $\mathbf{P}(0)$ contains the *bad* transitions that start from $1$.

Matrix $\mathbf{P}(i)$ through the index $i$ therefore counts the number of successes, that is $1$ for $i=1$ and $0$ for $i=0$. $\phi_{ij}(k,n)$ can be split into two terms: one where we have $k-1$ successes at the time step before and the remaining success is provided by $\mathbf{P}(1)$, whereas if we have already $k$ successes, no more are needed and $\mathbf{P}(0)$ follows.

We can apply the same analysis to *any finite-state* Markov chain where we want to distinguish between two types of transitions. In other words we can *divide all possible transitions, whose number is finite, into two groups according to some criterion*. After, we pick one group and write all its transitions into a matrix setting to zero the other ones, and finally we do the same with the other group. We thus obtain two matrices of the same kind of $\mathbf{P}(i)$, whose sum is the general transition probabilities matrix $\mathbf{P}$. By doing this, we are essentially counting the transitions of the type $\mathbf{P}(1)$. Obviously this argument can be generalized to a generic transition *counting* or *labelling*, by using the same machinery.

The analysis we have made so far is very similar to first-step analysis, but the condition we set on the *last* transition and not on the *first* one. If we did this way:

$\phi_{0j}(k,n)$ $=p_{00}\phi_{0j}(k-1,n-1)+p_{01}\phi_{1j}(k,n-1)+\delta_{0j}\delta(n)\delta(k)$
$\phi_{1j}(k,n)$ $=p_{10}\phi_{0j}(k-1,n-1)+p_{11}\phi_{1j}(k,n-1)+\delta_{1j}\delta(n)\delta(k)$

Where for the first expression, having we started in the *good* state, we have already counted one success and therefore we need $k-1$ successes in the elapsing $n-1$ time steps. Conversely, if we start in $1$ state the first transition is *bad*, and so regardless the destination of the following transition we need to count $k$ successes in the next $n-1$ time steps.

In matrix form:

$\phi(k,n)=\mathbf{P}(1)\phi(k-1,n-1)+\mathbf{P}(0)\phi(k,n-1)+\delta(n)\delta(k)\hbox{\rm 1\hskip-2.84526pt1}_{2}\qquad n\geqslant$


Comparing the last result with (6.18) we can see that the terms are actually the same ones, and so expressions are equal including the same boundary conditions, except for the order of the matrix products that is reversed. This is what we expected, being them two models describing the same quantities, and obviously they must provide a unique result.

We started from a counting problem, where we wanted to count the visits to a given state in a Markov chain, and found the recursive relation (6.18) that we are going to solve.

### 6.1.1 Transform methods for recursive equations

The equation:

> [!Important] Method - Two-Dimensional Transform for Recursive Counting Equations
> **Statement:** The recursive counting equation can be solved with the transform
>
> $$
> \varphi(s,z)=\sum_{k=0}^{+\infty}s^k\sum_{n=0}^{+\infty}z^n\phi(k,n),
> $$
>
> yielding:
>
> $$
> \varphi(s,z)=[\mathbb{1}-z(\mathbf{P}(1)s+\mathbf{P}(0))]^{-1}.
> $$
>
> For fixed $n$:
>
> $$
> \varphi(s,n)=\left(\mathbf{P}(1)s+\mathbf{P}(0)\right)^n.
> $$
>
> **Proof:** The transform derivation and inversion with respect to $z$ are transcribed below.
>
> **Intuition:** The variable $z$ counts transitions, while $s$ counts rewards/successes. The transform converts the recursion into a matrix inverse.

$\phi(k,n)=\mathbf{P}(1)\phi(k-1,n-1)+\mathbf{P}(0)\phi(k,n-1)+\delta(n)\delta(k)\mathbb{1}_{2}\qquad n\geqslant$ (6.19)

can be solved either by computing the solution recursively, where we compute the quantities pointed out in the equations for increasing $n$, or using the transform method. This can be done because we are dealing with relations of the kind $\phi(k,n)=f(\phi(k-1,n-1))$, and so they can be mapped into an other domain where they are easier to solve.

We apply a transform, which is similar to $z$-transform, to our $\phi(k,n)$ noting that it must be done in a two dimensional domain:

$\varphi(s,z)=\sum_{k=0}^{+\infty}s^{k}\sum_{n=0}^{+\infty}z^{n}\phi(k,n)$

Note as the only difference from the $z$-transform is the sign of the exponential. Using this formalism, whenever we have a time shift (i.e. in the original variable $n\to n+1$), we only need to multiply the transform by the correspondent variable to the power that points out the time difference. Specifically the transform version for (6.19):

$\varphi(s,z)=\varphi(s,z)\mathbf{P}(1)sz+\varphi(s,z)\mathbf{P}(0)z+\mathbb{1}$ (6.20)

where we applied, with regards to initial condition, the fact that the transform of $\delta(n)$, $\delta(k)$ is 1. Solving for $\varphi(s,z)$:

$\varphi(s,z)=[\mathbb{1}-\mathbf{P}(1)sz-\mathbf{P}(0)z]^{-1}=[\mathbb{1}-z(\mathbf{P}(1)s+\mathbf{P}(0))]^{-1}$
$=\sum_{n=0}^{+\infty}\left[\mathbf{P}(1)s+\mathbf{P}(0)\right]^{n}z^{n}$ (6.21)

where in the last passage we use an equivalent formulation of the scalar geometric sum, that is $\sum_{k=0}^{+\infty}u=(1-a)^{-1}$. This formula can be rewritten in matricial form, where it holds that:

$\sum_{k=0}^{+\infty}\mathbb{A}^{k}=[\mathbb{1}-\mathbb{A}]^{-1}$


and $\mathbb{A}=z(\mathbf{P}(1)s+\mathbf{P}(0))$.

Comparing this last result (6.21) with the definition (6.20), we can easily invert transform with respect to $z$. Therefore:

$\varphi(s,n)=\sum_{k=0}^{+\infty}s^{k}\phi(k,n)=\text{transform over $k$ for a fixed $n=\left(\mathbf{P}(1)s+\mathbf{P}(0)\right)^{n}$}$ (6.22)

Now we want to make the second step, i.e. find the coefficients for $s^{k}$. This can be done in principle, by expanding $\left(\mathbf{P}(1)s+\mathbf{P}(0)\right)^{n}$ the $n$-th grade polynomial and finding the matrix coefficient for $s$. Matrix coefficient for $s^{k}$ will be $\phi(k,n)$, according to transform definition.


Let us study an example using the results we have just obtained. We want to find the average number of good slots in $0,1,2,...,n-1$ given an initial state $i$. We can recall the definition (6.13) of $\phi_{ij}(k,n)$, where we focus only on the number of good slots and not on the final state. In order to do so, we need to sum (i.e.) over all possible $j$. Therefore it is needed to sum up the first row of matrix (6.17), so obtaining :

$\varphi_{i0}(s,n)+\varphi_{i1}(s,n)$ (6.23)

which is the transform of the statistics of the number of successes, given the initial state. In addition, the latter is the generating function of the number visits to state $0$ in a fixed time $0,1,2,...,n-1$ and given we start in $i$, and can be obtained by computing (6.22).

We want to stress another time that we need to sum over $j$, otherwise we would have the joint distribution where we would take into account the different landing states. The average number of successes can be obtained by deriving one time (6.23) and finally setting $s=1$:

$\varphi^{\prime}(1,n)=\frac{d\varphi(s,n)}{s}\Big{|}_{s=1}$

Recall that now we are dealing with matrices where order of multiplication does matter.

When we compute the first derivative for (6.21), we can not apply the "plain" rule for scalars i.e. $f^{\prime}([ax+b]^{n})=an(ax+b)^{n-1}$: in the intermediate passage we would end up with $n$ addends of the kind $a(ax+b)^{n-1}$ that are actually the same one. We need indeed to take into account now that deriving the $k$-th term of the product may return different result from the other $k-1$-th or $k+1$-th, because they are matrices. So we obtain:

$\varphi^{\prime}(1,n)=\frac{d\varphi(s,n)}{s}\Big{|}_{s=1}=\sum_{k=0}^{n-1}\Big{(}\mathbf{P}(1)s+\mathbf{P}(0)\Big{)}^{k}\mathbf{P}(1)\Big{(}\mathbf{P}(1)s)+\mathbf{P}(0)\Big{)}^{n-1-k}\Big{|}_{s=1}=$


$$
= \sum_{k=0}^{n-1} \mathbf{P}^k \mathbf{P}(1) \mathbf{P}^{n-1-k}
$$

where we used the fact that $\mathbf{P}(0) + \mathbf{P}(1) = \mathbf{P}$. What we want to compute is given by the sum of each row in the matrices shown in the last expression. Formally, in matrix notation, this is represented by:

$\varphi'(1,n)\left( \begin{array}{c}1\\ 1 \end{array} \right) = \text{we sum the elements of each row, i.e. over the final state } j =$

$$
= \sum_{k=0}^{n-1} \mathbf{P}^k \mathbf{P}(1) \mathbf{P}^{n-1-k} \left( \begin{array}{c} 1 \\ 1 \end{array} \right) = \sum_{k=0}^{n-1} \mathbf{P}^k \mathbf{P}(1) \left( \begin{array}{c} 1 \\ 1 \end{array} \right) =
$$

where we used the fact that $\mathbf{P}^{n-1-k}$ is a transition probability matrix, and therefore all rows sum to 1. Consequently the product $\mathbf{P}^{n-1-k} \begin{pmatrix} 1 \\ 1 \end{pmatrix}$ returns $\begin{pmatrix} 1 \\ 1 \end{pmatrix}$ itself.

Recalling $\mathbf{P}(1) = \begin{pmatrix} p_{00} & p_{01} \\ 0 & 0 \end{pmatrix}$, the product $\begin{pmatrix} p_{00} & p_{01} \\ 0 & 0 \end{pmatrix} \begin{pmatrix} 1 \\ 1 \end{pmatrix} = \begin{pmatrix} 1 \\ 0 \end{pmatrix}$.

Consequently:

$$
= \sum_{k=0}^{n-1} \mathbf{P}^k \left( \begin{array}{c} 1 \\ 1 \end{array} \right) = \left( \begin{array}{c} \sum_{k=0}^{n-1} \mathbf{P}_{00}^{<k>} \\ \sum_{k=0}^{n-1} \mathbf{P}_{10}^{<k>} \end{array} \right) \tag{6.24}
$$

where we "keep" only the first column of $\mathbf{P}$, and get the average over $k$ steps. Another way to see it, is that we want to compute:

$$
\begin{pmatrix}
\mathbb{E}[\# \text{successes in } 0, ..., n-1 \mid X_0 = 0] \\
\mathbb{E}[\# \text{successes in } 0, ..., n-1 \mid X_0 = 1]
\end{pmatrix}
=
\begin{pmatrix}
\varphi_{00}'(1, n) + \varphi_{01}'(1, n) \\
\varphi_{10}'(1, n) + \varphi_{11}'(1, n)
\end{pmatrix}
=
\varphi'(1, n) \begin{pmatrix} 1 \\ 1 \end{pmatrix}
$$

That is what we have just obtained. Note that we found this result by using the transform formalism. For the result (6.24) by the way, we can use the "old" and simple one:

$$
\begin{aligned}
\mathbb{E}[\# \text{of visits to } 0 \mid X_0 = i] &= \mathbb{E}\left[ \sum_{k=0}^{n-1} \mathbb{1}\{X_k = 0\} \mid X_0 = i \right] = \\
&= \sum_{k=0}^{n-1} \mathbb{E}\left[ \mathbb{1}\{X_k = 0\} \mid X_0 = i \right] = \sum_{k=0}^{n-1} P[X_k = 0 \mid X_0 = i]
\end{aligned}
$$

where the last one is the $k$-step transition probability from 0 to $i$, that is the result (6.24).

242</k></k>

### 6.1.2 Generalization

Recalling now the equation:

$$
\phi(k,n)=\phi(k-1,n-1)\mathbf{P}(1)+\mathbf{P}(0)\phi(k,n-1)+\delta(n)\delta(k)\mathbf{\mathbb{1}}_{2}\qquad n\geqslant
$$

we see as $\phi(k,n)$ has been rewritten as the sum of two transition types: the one where we have a success $\mathbf{\mathbb{P}}(1)$ term, and the other one $\mathbf{\mathbb{P}}(0)$ where no successes occur.

Now we want to study a more general case, where we associate an integer metric to each transition. Let $\mathbf{P}(l)$ be the matrix that contains all elements of $\mathbf{P}$ that correspond to a reward of the deterministic metric $l$. We have that:

> [!Important] Generalization - Transition Generating Matrix $\psi(s)$
> **Statement:** If $\mathbf{P}(l)$ contains the transition probabilities associated with metric value $l$, then:
>
> $$
> \psi(s)=\sum_{l=0}^{+\infty}\mathbf{P}(l)s^l,
> \qquad
> \varphi(s,n)=[\psi(s)]^n.
> $$
>
> For multiple metrics $\vec{s}$:
>
> $$
> \psi_{ij}(\vec{s})=\sum_{A\in\varepsilon(i,j)}P[A]\vec{s}(A).
> $$
>
> **Intuition:** $\psi$ packages both transition probabilities and metric distributions. Setting $\vec{s}=\vec{1}$ recovers the transition matrix; differentiating recovers average rewards or times.

$$\phi(k,n)=\sum_{l=0}^{+\infty}\phi(k-l,n-1)\mathbf{P}(l)+\delta(n)\delta(k)\mathbf{\mathbb{1}}_{2}$$ (6.25)

Where we note that in order to accumulate $k$ total reward at time $n$, we must have accumulated $k-l$ total reward up to time $n-1$. Moreover, in this generalization, the condition $k\leqslant n$ does not apply any more. Transforming (6.25) we obtain:

$$
\varphi(s,z)=\varphi(s,z)\psi(s)z+\mathbf{\mathbb{1}}
$$

where $z$ factor is due to the time delay $n-1$, and where we have introduced:

$$
\psi(s)=\sum_{l=0}^{+\infty}\mathbf{P}(l)s^{l}
$$

This is indeed not surprising at all: $\phi(k-l,n-1)\mathbf{P}(l)$ can be seen as a discrete convolution in $k,l$, and so the sum over all possible values of $l$ returns the product of the convolution.

As we did before, we can solve for $\varphi(s,z)$ keeping in mind that $\psi(s)$ is now a polynomial in $s$:

$$
\varphi(s,z)=[\mathbf{\mathbb{1}}-\psi(s)z]^{-1}
$$

Now we can retrieve the transform for $\phi(k,n)$ and fixed $n$, so being able to write:

$$
\varphi(s,n)=[\psi(s)]^{n}
$$

in a similar way we did before, where the only values for $l\in\{0,1\}$.

Let us discuss a little what we have found up to now by pointing out some facts:

- we still can find the average number of rewards in $0,1,...,n-1$ as before, that was a particular case where $\psi(s)=\mathbf{P}(0)+\mathbf{P}(1)s$. That is to say we can compute it by finding the first derivative of the generating function in $s=1$, noting that this function is composed by a linear combination of all possible initial states.


- the 2-d transform $\varphi(s,z)$ is a linear combination of some matrices multiplied by the product of $s$ and $z$ to a certain power. These matrices describe the probabilities for a certain transition to occur. More specifically, $s$ labels the successes/rewards, while $z$ the number of transitions.
- each transition $i\to j$ has a "label" $\psi_{ij}(s)$. Indeed $\psi(s)$ is a matrix of polynomial, of which every element corresponds to a specific transition that can be labelled accordingly.
- nothing forces us to have a random metric for each transition, contrary to what we have done up to now. In other words, for a specific transition we may have a reward that changes with different probability. That is, we can have:

$\psi_{ij}(s)=\sum_{l=0}^{+\infty}P_{ij}(l)s^{l}$

where $P_{ij}(l)$ is the *joint* probability of transition $i\to j$ *and* that the value of the metric is $l$.
Consequently for each transition we have a probability distribution that tells us how much reward we obtain.

Properties of $\psi_{ij}(s)$:

1. $\psi_{ij}(1)=P_{ij}\qquad\psi(1)=\mathbf{P}$

when $s=1$ we can sum over all $l$ possible rewards, and so *remove its dependence in the joint probability* $P_{ij}(l)$. In this way $\psi(1)$ becomes the transition probability matrix $\mathbf{P}$ of the chain
2. $\frac{\psi_{ij}(s)}{p_{ij}}$ is the generating function of the distribution of the metric, once we have *fixed* the *transition* $i\to j$. Note that for $s=1$, this ratio becomes $1$, and so it is moreover *normalized*
3. $\psi_{ij}^{\prime}(s)=\frac{d\psi_{ij}}{ds}\Big{|}_{s=1}=P_{ij}\cdot\text{average metric on }i\to j$
4. if the metric is the reward, recalling the definition of the average reward for a visit to state $i$, then $R_{i}=\sum_{j}P_{ij}R_{ij}$ that we have already computed in 2), and so $R_{i}=\sum_{j}\psi_{ij}^{\prime}(1)$.
- We can define multiple metrics, i.e. $s$ could be vector $\vec{s}=(s_{1},s_{2},...)$ instead of a single variable. Each of its component will therefore counts a different metric. In this case, the average becomes:

$p_{ij}\cdot\text{average of the }k\text{-th metric on }i\to j=\frac{\partial\psi_{ij}(s_{1},s_{2},...)}{\partial s_{k}}\Big{|}_{\vec{s}=\vec{1}}$
- How to compute $\psi_{ij}(\vec{s})$.
First we state that there is a Markov model underlying transitions $i\to j$. Then:


1. let $\varepsilon(i,j)$ be the set of all events that correspond to a transition from state $i \to j$
2. let each event $A$ in this set have the probability $P[A]$
3. let each event $A$ correspond to a different value for the metric, that is equivalent to state that we define $A$ as a possible value for the joint probability $\vec{s}(A) = s_1^{l_1(a)} s_2^{l_2(a)}$ ..., where $l_k(A)$ is the value of the metric that corresponds to event $A$
4. under all these assumptions, it holds that:

$$
\psi_{ij}(\vec{s}) = \sum_{A \in \varepsilon(i,j)} P[A] \vec{s}(A)
$$

thus it becomes a counting exercise: we should need to make a list of all possible events and each with its own probability and value of the metric, and then group the these elements according to the transition they produce. Each of them will be an entry for the matrix $\psi$.

Note that:

$$
\psi_{ij}(\vec{s} = \vec{1}) = \sum_{A \in \varepsilon(i,j)} P[A] = P_{ij}
$$

Now, recall that we have just found that the average $k$-th metric times the probability $i \to j$:

$$
R_{ij}^{(k)} P_{ij} = \left. \frac{\partial \psi_{ij}(\vec{s})}{\partial s_k} \right|_{\vec{s} = 1} = \psi_{ij}^{(k)} \, {}' (s)
$$

and, summing over $j$:

$$
\sum_j R_{ij}^{(k)} P_{ij} = \sum_j \psi_{ij}^{(k)} \, {}' (s) = R_i^{(k)} \tag{6.26}
$$

that is the average $k$-th reward accumulated so far.

From the renewal reward theory we have found that with probability 1:

$$
\lim_{t \to \infty} \frac{R^{(1)}(t)}{R^{(2)}(t)} = \frac{\sum_i \pi_i R_i^{(1)}(t)}{\sum_i \pi_i R_i^{(2)}(t)} = \frac{\sum_i \pi_i \sum_j \psi_{ij}^{(1)} \, {}' (1)}{\sum_i \pi_i \sum_j \psi_{ij}^{(2)} \, {}' (1)} =
$$

where we replaced $R_i^{(1)}(t)$ and $R_i^{(2)}(t)$ using (6.26) and by right multiplying it time $\vec{1}$: when we right multiply a matrix by a vector of $\vec{1}$, we obtain a column vector where each element is the sum of the corresponding row of the matrix.

$$
= \frac{\sum_{i} \pi_i \left. \frac{\partial \psi_{ij}(\vec{s})}{\partial s_1} \right|_{\vec{s} = 1} \cdot \vec{1}}{\sum_{i} \pi_i \left. \frac{\partial \psi_{ij}(\vec{s})}{\partial s_2} \right|_{\vec{s} = 1} \cdot \vec{1}} = \frac{ \overbrace{\vec{\pi}}^{\text{row}} \cdot \overbrace{ \left. \frac{\partial \psi_{ij}(\vec{s})}{\partial s_1} \right|_{\vec{s} = 1} \cdot \vec{1} }^{\text{column}} }{ \underbrace{ \vec{\pi} \cdot \left. \frac{\partial \psi_{ij}(\vec{s})}{\partial s_2} \right|_{\vec{s} = 1} \cdot \vec{1} }_{\text{scalar}} }
$$


We should have recognized that the sum over the  $i$ -th component of the product  $\pi_i$  and the column vector  $\left.\frac{\partial\psi_{ij}(\vec{s})}{\partial s_k}\right|_{\vec{s} = 1}\cdot \vec{1}$  is the definition of the scalar product, and therefore the last expression follows.

Note that we have just found the average value of metric 1 per unit of metric 2 in the limit as  $t \to \infty$ . In order to compute it, all we need is the matrix  $\psi(\vec{s})$ : it contains both the transition probability matrix and the information needed for the metric. In fact we can obtain  $\mathbf{P} = \psi(\vec{s} = \vec{1})$  and, from this, compute the limiting distribution of the chain  $\vec{\pi} = \vec{\pi}\mathbf{P}$ . Whereas in order to compute the  $R^{(k)}$  it is sufficient to compute the first partial derivative of  $\psi(\vec{s})$  wrt  $s_k$  and set  $\vec{s} = \vec{1}$ .

It is important to point out that once we have defined our system, computing  $\psi_{ij}(\vec{s})$  for all transitions, in the way we stated above, we can obtain for example the ratio  $\lim_{t\to \infty}\frac{R^{(1)}(t)}{R^{(2)}(t)}$  thanks to a standard procedure. Obviously this does not take into account technical difficulties that may arise during calculations, that are unbounded from the theoretical result we have just written.

One other important result is that if we consider matricial operations, such as the ones in the ratio above, the number of states is not important. We can therefore have so many states as we want, as long as we are able to find the matrix  $\psi_{ij}\vec{s}$ , and the theory we have just gone through will give us the correct result. This is indeed a general result.

## 6.1.3 GoBackN protocol - Transform approach

As a concrete example of the generalization for computing the matrix  $\psi_{ij}(\vec{s})$ , we will now study the GoBackN protocol with i.i.d. feedback errors with probability  $\delta$ . Recalling its transition diagram.

![[Stochastic_Processes_2020_p246_img92.jpeg]]
*Figure 6.6 - Representation of the embedded Markov chain for the 2-states model for GoBackN protocol, where feedback errors are i.i.d. with probability  $\delta$ .*

We want in fact to build a model for the protocol shown in (fig 6.6), in order to achieve some results using the formalism we have just introduced. According to the list we have written above, in order to compute  $\psi_{ij}\vec{s}$  we have to proceed through the following steps: define the set  $\varepsilon(i,j)$  of all events, then find both the probability for each event, namely  $P[A]$ , and the corresponding metrics, finally grouping what we have just computed by which transition they refer to.

Now recall that our reward is different from zero, and so the time slot reward is 1, only when we both start from a good state and the acknowledgement is correct. The only rows of the table (???) that satisfy to these requirements are the first two.

This is indeed a very simple model, and so we can deal with the whole list


|  from | to | probability | reward | time  |
| --- | --- | --- | --- | --- |
|  G | G | (1-δ)p00 | 1 | 1  |
|  G | B | (1-δ)p01 | 1 | 1  |
|  G | G | δp00(m) | 0 | m  |
|  G | B | δp01(m) | 0 | m  |
|  B | G | (1-δ)p10(m) | 0 | m  |
|  B | B | (1-δ)p11(m) | 0 | m  |
|  B | G | δp10(m) | 0 | m  |
|  B | B | δp11(m) | 0 | m  |

*Table 6.1 - Table depicting all possible combinations for good/bad transmission and good/bad acknowledgement. We have 4 possible transitions between states  $B, G$ , with probability  $p_{ij}$  that corresponds to the correctness of transmission, times the two possible outcomes for the feedback that might be correct with probability  $1 - \delta$  or wrong with probability  $\delta$ . Hence the total number of entries, i.e. rows, is 8.*

manually. If it had been more complicated, then we would have found some algorithm in order to compute it automatically for example being helped by a software.

We need to group all the entries in the  $(\ref{eq:1})$  by transition, and we can see that there are actually 4 of them:  $G \to G, B \to G, G \to B, B \to B$ . If we pick as an example all rows that belong to  $G \to G$  transition, they will result in the same  $\psi_{GG}$  and the consequent sum will be over only two events. Of course this applies to all the remaining transitions.

The final step, in order to define  $\psi_{ij}(\vec{s})$ , is to compute the product  $P[A_k]\vec{s}[A_k]$  for each event that belongs to a certain group. The sum will consist in two terms, that are the two distinct events  $A_1, A_2$ , are the product of the probability of each event times  $s_1^{l_1}s_2^{l_2}$ , where  $s_i$  denotes the which metric we are referring to, and  $l_i$  the metric value. Each element of the following matrix will be the result of the just mentioned computation for all possible states:

| ψ(s1,s2) = | (ψGGψGB) | $(1-δ)p_{00}s_1s_2+δp_{00}(m)s_{2m}$ | $(1-δ)p_{01}s_1s_2+δp_{01}(m)s_{2m}$ |
| ---------- | -------- | ------------------------------------ | ------------------------------------ |
|            | ψBGψBB)  |                                      |                                      |

We will show now that this matrix contains all the information about the model. Transition probability matrix can be obtained as:

|  P = ψ(1,1) = | (1-δ)p00 + δp00(m) | (1-δ)p01 + δp01(m)  |
| --- | --- | --- |
|   | p10(m) | p11  |

and consequently the limiting probabilities:

|  πG = p10(m)/p10(m) + (1-δ)p01 + δp01(m) | πB = 1 - πG = (1-δ)p01 + δp01(m)/p10(m) + (1-δ)p01 + δp01(m)  |
| --- | --- |


While $P_{ij}R_{ij}$ are the elements of:

$$
\left. \frac {\partial \psi}{\partial s _ {1}} \right| _ {s _ {1} = s _ {2} = 1} = \left( \begin{array}{c c} (1 - \delta) p _ {0 0} & (1 - \delta) p _ {0 1} \\ 0 & 0 \end{array} \right)
$$

and $P_{ij}T_{ij}$ are the elements of:

$$
\left. \frac {\partial \psi}{\partial s _ {2}} \right| _ {s _ {1} = s _ {2} = 1} = \left( \begin{array}{c c} (1 - \delta) p _ {0 0} + m \delta p _ {0 0} (m) & (1 - \delta) p _ {0 1} + m \delta p _ {0 1} (m) \\ m p _ {1 0} & m p _ {1 1} \end{array} \right)
$$

Consequently $\vec{R}$ and $\vec{T}$, i.e. the column vectors associated to the states found by summing over rows:

$$
\vec {R} = \left. \frac {\partial \psi}{\partial s _ {1}} \right| _ {s _ {1} = s _ {2} = 1} \cdot \left( \begin{array}{c} 1 \\ 1 \end{array} \right) = \left( \begin{array}{c} 1 - \delta \\ 0 \end{array} \right)
\vec {T} = \left. \frac {\partial \psi}{\partial s _ {2}} \right| _ {s _ {1} = s _ {2} = 1} \cdot \left( \begin{array}{c} 1 \\ 1 \end{array} \right) = \left( \begin{array}{c} 1 - \delta + m \delta \\ m \end{array} \right)
$$

Finally, we can compute the **throughput** having all the information we need:

> [!Important] Result - Throughput from the Transition Generating Matrix
> **Statement:** For the GoBackN two-state model with i.i.d. feedback errors, the matrix $\psi(s_1,s_2)$ contains enough information to recover the embedded transition matrix, reward vector, time vector, and throughput:
>
> $$
> \text {throughput} = \frac {(1 - \delta) p _ {1 0} (m)}{(1 - \delta + m \delta) p _ {1 0} (m) + m [ (1 - \delta) p _ {0 1} + \delta p _ {0 1} (m) ]}.
> $$
>
> **Intuition:** $s_1$ counts successful packets and $s_2$ counts consumed slots; differentiating $\psi$ with respect to these variables gives the numerator and denominator of throughput.

$$
\text {throughput} = \frac {\pi_ {G} R _ {G} + \pi_ {B} R _ {B}}{\pi_ {G} T _ {G} + \pi_ {B} T _ {B}} = \frac {(1 - \delta) p _ {1 0} (m)}{(1 - \delta + m \delta) p _ {1 0} (m) + m [ (1 - \delta) p _ {0 1} + \delta p _ {0 1} (m) ]}
$$

that is the same result we have computed before.

We have just shown that the matrix $\psi(s_1, s_2)$ contains all the information we need in order to compute the statistical quantities we are usually interested in. It is indeed a very useful and powerful tool, moreover matricial notation is more compact and, very important, independent of the size of the system.

## 6.1.4 GoBackN protocol - Generalization

We could have computed the throughput, and consequently all the statistics, the other way around using the original approach.

We therefore split $\mathbf{P} = \mathbf{P}_S + \mathbf{P}_F$, that are respectively the transition matrices for successes and failures. Note that we used to call these matrices $\mathbf{P}(1)$ and $\mathbf{P}(0)$, when we were considering the feedback with no error. Now instead we need to pay attention to which transition probabilities between states $G, B$ of the matrix $\mathbf{P}$ belong to $\mathbf{P}_S$ and which to $\mathbf{P}_F$, they can be indeed split in turn. Thus write:

$$
\mathbf {P} _ {S} = \text {transition matrix for successes} = \left( \begin{array}{c c} (1 - \delta) p _ {0 0} & (1 - \delta) p _ {0} 1 \\ 0 & 0 \end{array} \right)
\mathbf {P} _ {F} = \text {transition matrix for failures} = \left( \begin{array}{c c} \delta p _ {0 0} (m) & \delta p _ {0 1} (m) \\ \delta p _ {1 0} (m) & \delta p _ {1 1} (m) \end{array} \right)
$$


and moreover:

$\psi(s_{1},s_{2})=\mathbf{P}_{S}s_{1}s_{2}+\mathbf{P}_{F}s_{2}^{m}$

where we have chosen the metric according to whether we have a success or not.
We can write recursive relations as we did before, but taking into account that metrics are now 2:

$\phi(k_{1},k_{2},n)=\phi(k_{1}-1,k_{2}-1,n)\mathbf{P}_{S}+\phi(k_{1},k_{2}-m,n)\mathbf{P}_{F}+\mathbb{1}\delta(n)\delta(k_{1})\delta(k_{2})\qquad n\geqslant 0$

Note that if the last transition $n-1\to n$ is a success, then we need at the previous time step the metrics $k_{1}-1$ and $k_{2}-1$. Conversely, if it is a failure, at the previous time step we must have $k_{1}$ for rewards and $k_{2}-m$ for time slots. To the initial condition we apply the same argument we already discussed.
By transforming the last equation we find:

$\varphi(s_{1},s_{2},z)=\varphi(s_{1},s_{2},z)[\mathbf{P}_{S}s_{1}s_{2}z+\mathbf{P}_{F}s_{2}^{m}z]+\mathbb{1}$

and solving for $\varphi(s_{1},s_{2},z)$:

$\varphi(s_{1},s_{2},z)=[\mathbb{1}-(\mathbf{P}_{S}s_{1}s_{2}+\mathbf{P}_{F}s_{2}^{m})z]^{-1}$

and fixing the number of transitions $n$:

$\varphi(s_{1},s_{2},n)=[\mathbf{P}_{S}s_{1}s_{2}+\mathbf{P}_{F}s_{2}^{m}]^{n}=[\psi(s_{1},s_{2})]^{n}$

If we take the partial derivatives we can compute the averages. With respect to the first variable:

$\frac{\partial\varphi(s_{1},s_{2},n)}{\partial s_{1}}=\sum_{k=0}^{n-1}\Big{(}\mathbf{P}_{S}s_{1}s_{2}+\mathbf{P}_{F}s_{2}^{m}\Big{)}^{k}\mathbf{P}_{2}s_{2}\Big{(}\mathbf{P}_{S}s_{1}s_{2}+\mathbf{P}_{F}s_{2}^{m}\Big{)}^{n-1-k}$
$\frac{\partial\varphi(s_{1},s_{2},n)}{\partial s_{1}}\Big{|}=\sum_{k=0}^{n-1}\mathbf{P}^{k}\mathbf{P}_{S}\mathbf{P}^{n-1-k}$

That is a result already found before.
We want to stress out once again that taking the transform, fixing $n$, and summing over columns, namely:

$\sum_{j}\varphi_{ij}(s_{1},s_{2},n)$

is the *joint* generating function of the number of *successes* and the number of slots per $n$ transitions, given that the initial state is $i$.
The *marginal* generating function of successes and slots, given the initial state,


are obtained from above by setting $s_2 = 1$ and $s_1 = 1$, respectively. Therefore:

$$
\left(\mathbb {E} [ \# \text{ of successes in } 0, 1 \dots , n - 1 \mid X _ {0} = G ] \right) = \frac {\partial \varphi (\vec {s} , n)}{\partial s _ {1}} \Big | _ {\vec {s} = \vec {1}} \cdot \binom {1} {1} \tag {6.28}
$$

and

$$
\left(\mathbb {E} [ \# \text{ of slots in } 0, 1 \dots , n - 1 \mid X _ {0} = G ] \right) = \frac {\partial \varphi (\vec {s} , n)}{\partial s _ {2}} \Big | _ {\vec {s} = \vec {1}} \cdot \binom {1} {1}
$$

We want now to compute (6.28), using the results for intermediate matricial products we have computed before:

$$
\frac {\partial \varphi (\vec {s} , n)}{\partial s _ {1}} \Big | _ {\vec {s} = \vec {1}} \cdot \left( \begin{array}{c} 1 \\ 1 \end{array} \right) = \sum_ {k = 0} ^ {n - 1} \mathbf {P} ^ {k} \mathbf {P} _ {S} \mathbf {P} ^ {n - 1 - k} \cdot \left( \begin{array}{c} 1 \\ 1 \end{array} \right) = \sum_ {k = 0} ^ {n - 1} \mathbf {P} ^ {k} \cdot \vec {R}
$$

where $\vec{R} = \mathbf{P}\cdot \binom{1}{1}$. The last expression is the average number of successes in $n$ transition. If we want to compute its expected value, we take the limit:

$$
\left(\mathbb {E} [ \# \text{ of successes per transition} \mid X _ {0} = G ] \right) = \lim _ {n \to \infty} \frac {1}{n} \left(\sum_ {k = 0} ^ {n - 1} \mathbf {P} ^ {k} \cdot \vec {R}\right) =
$$

but note that $\vec{R}$ is independent of $n$, thus we can factorize:

$$
= \left(\lim _ {n \to \infty} \frac {1}{n} \sum_ {k = 0} ^ {n - 1} \mathbf {P} ^ {k}\right) \cdot \vec {R} = \left( \begin{array}{c} \vec {\pi} \cdot \vec {R} \\ \vec {\pi} \cdot \vec {R} \end{array} \right) = \left( \begin{array}{c} \pi_ {G} R _ {G} + \pi_ {B} R _ {B} \\ \pi_ {G} R _ {G} + \pi_ {B} R _ {B} \end{array} \right) =
= \left( \begin{array}{c} (1 - \delta) \pi_ {G} + 0 \cdot \pi_ {B} \\ (1 - \delta) \pi_ {G} + 0 \cdot \pi_ {B} \end{array} \right) = \left( \begin{array}{c} (1 - \delta) \pi_ {G} \\ (1 - \delta) \pi_ {G} \end{array} \right)
$$

where the limit will have all rows equal, and more precisely equal to $\pi$. Note as the last result is the same one for both $X_0 = G$ and $X_0 = B$, and so independent of the initial state as expected.

Similarly for the number of slots:

$$
\varphi (s _ {1}, s _ {2}, n) = [ \mathbf {P} _ {S} s _ {1} s _ {2} + \mathbf {P} _ {F} s _ {2} ^ {m} ] ^ {n}
$$

When computing the second derivative we obtain a slightly different term, that is:

$$
\frac {\partial \varphi (s _ {1} , s _ {2} , n)}{\partial s _ {2}} = \sum_ {k = 0} ^ {n - 1} \left(\mathbf {P} _ {S} s _ {1} s _ {2} + \mathbf {P} _ {F} s _ {2} ^ {m}\right) ^ {k} \left(\mathbf {P} _ {S} s _ {1} + m \mathbf {P} _ {F} s _ {2} ^ {m - 1}\right) \left(\mathbf {P} _ {S} s _ {1} s _ {2} + \mathbf {P} _ {F} s _ {2} ^ {m}\right) ^ {n - 1 - k}
$$


and setting  $\vec{s} = \vec{1}$ :

$$
\frac {\partial \varphi (s _ {1} , s _ {2} , n)}{\partial s _ {2}} \Big | _ {\vec {s} = \vec {1}} = \sum_ {k = 0} ^ {n - 1} \mathbf {P} ^ {k} (\mathbf {P} _ {S} + m \mathbf {P} _ {F}) \mathbf {P} ^ {n - 1 - k} = \sum_ {k = 0} ^ {n - 1} \mathbf {P} ^ {k} (\mathbf {P} _ {S} + m (\mathbf {P} - \mathbf {P} _ {S})) \mathbf {P} ^ {n - 1 - k} =
\sum_ {k = 0} ^ {n - 1} \mathbf {P} ^ {k} (m \cdot \mathbf {P} - (m - 1) \mathbf {P} _ {S}) \mathrm {)} \mathbf {P} ^ {n - 1 - k} = m \sum_ {k = 0} ^ {n - 1} \mathbf {P} ^ {n} - (m - 1) \sum_ {k = 0} ^ {n - 1} \mathbf {P} ^ {k} \mathbf {P} _ {S} \mathbf {P} ^ {n - 1 - k}
$$

where we just made the computation and split the expression into two factors. Note that the second term is common with the other partial derivative wrt  $s_1$ . If we then right multiply the last expression by the vector  $\vec{1}$ :

$$
\begin{array}{l} \frac {\partial \varphi (s _ {1} , s _ {2} , n)}{\partial s _ {2}} \cdot \left( \begin{array}{c} 1 \\ 1 \end{array} \right) = \left(m \sum_ {k = 0} ^ {n - 1} \mathbf {P} ^ {n} - (m - 1) \sum_ {k = 0} ^ {n - 1} \mathbf {P} ^ {k} \mathbf {P} _ {S} \mathbf {P} ^ {n - 1 - k}\right) \cdot \left( \begin{array}{c} 1 \\ 1 \end{array} \right) = \\ = m \underbrace {\sum_ {k = 0} ^ {n - 1} \mathbf {P} ^ {n}} _ {n \cdot \vec {1}} \cdot \left( \begin{array}{c} 1 \\ 1 \end{array} \right) - (m - 1) \underbrace {\sum_ {k = 0} ^ {n - 1} \mathbf {P} ^ {k} \mathbf {P} _ {S} \mathbf {P} ^ {n - 1 - k} \cdot \left( \begin{array}{c} 1 \\ 1 \end{array} \right)} _ {\sum_ {k = 0} ^ {n - 1} \mathbf {P} ^ {k} \cdot \vec {R} \text { as we computed before}} = \\ \end{array}
$$

where the first term is the sum of  $n$  vectors all equal to  $\vec{1}$ . Finally:

$$
= m \cdot n \cdot \left( \begin{array}{c} 1 \\ 1 \end{array} \right) - (m - 1) \sum_ {k = 0} ^ {n - 1} \mathbf {P} ^ {k} \cdot \vec {R}
$$

We can compute, as before:

$$
\left( \begin{array}{l} \mathbb {E} [ \# \text { of slots per transition} \mid X _ {0} = G ] \\ \mathbb {E} [ \# \text { of slots per transition} \mid X _ {0} = B ] \end{array} \right) = \lim  _ {n \to \infty} \frac {1}{n} \left(m \cdot n \left( \begin{array}{l} 1 \\ 1 \end{array} \right) - (m - 1) \sum_ {k = 0} ^ {n - 1} \mathbf {P} ^ {k} \cdot \vec {R}\right) =
$$

with similar calculations to what we did before for the successes:

$$
= \left( \begin{array}{c} m - (m - 1) \vec {\pi} \cdot \vec {R} \\ m - (m - 1) \vec {\pi} \cdot \vec {R} \end{array} \right) = \left( \begin{array}{c} \vec {\pi} \cdot \vec {R} + m (1 - \vec {\pi} \cdot \vec {R}) \\ \vec {\pi} \cdot \vec {R} + m (1 - \vec {\pi} \cdot \vec {R}) \end{array} \right)
$$

In this case as well the two rows are the same, being the asymptotic result independent of the initial state.

Finally the throughput of the system is:

$$
\lim _ {n \to \infty} \frac {\# \mathrm {o f s u c c e s s e s i n} 0 , . . . , n - 1}{\# \mathrm {o f s l o t s i n} 0 , . . . , n - 1} = \frac {(\# \mathrm {o f s u c c e s s e s i n} 0 , . . . , n - 1) / n}{(\# \mathrm {o f s l o t s i n} 0 , . . . , n - 1) / n} =
$$

that with probability 1, for the law of large numbers:

$$
\frac {\mathbb {E} [ \# \text { of successes per transition} ]}{\mathbb {E} [ \# \text { of slots per transition} ]} = \frac {(1 - \delta) \pi_ {G}}{(1 - \delta) \pi_ {G} + m (1 - (1 - \delta) \pi_ {G})} = \frac{(1-\delta)p_{10}(m)}{(1-\delta)p_{10}(m)+m[(1-\delta)p_{01}+\delta p_{01}(m)+\delta p_{10}(m)]}
$$

here we replaced the expectation values per transition with the values we have just computed and remembering that $\vec{\pi}\cdot\vec{R}=(1-\delta)\pi_{G}$. Note that we do not have a condition on the initial state, being this result asymptotic. By replacing with the values of the limiting probabilities $\pi_{G}$ and $\pi_{B}$ from (6.27), we can rewrite the throughput as above, as we found before in (6.11).
We have thus shown that we can use different approaches to study our problem. These are either the probabilistic approach linked to the recursive technique, or the transform method to solve the recursion, or this last approach based on the $\psi$, where we combine together into "transition functions" the transition probabilities as well as the statistics of the related metrics. Obviously, the results we find must be the same ones.


Bibliography

- [1] M.A. Pinsky and S. Karlin. An introduction to stochastic modeling. 4th ed. Academic Press, 2011. isbn: 0233814167.
- [2] M. Zorzi. “Stochastic Processes course at University of Padua”. Handwritten notes. 2020.
- [3] S. Karlin and H. Taylor. A first course in stochastic processes. 2nd ed. Academic Press, 1975. isbn: 0123985536.
- [4] S. Ross. Applied probability models with optimization applications. 2nd ed. Dover, 1996. isbn: 0486673146.


## Analytical Index

|  C |   | Total probability | 7  |
| --- | --- | --- | --- |
|  Chain | 7 |  |   |
|  Correlation | 10 | M |   |
|  F |   | Markov |   |
|   |  | Process | 27  |
|  Function |  | Mean | 9  |
|  Cumulative distribution | 8 | Moment |   |
|  Probability density | 8 | Central | 9  |
|  G |   | S |   |
|  Generating function |  | States |   |
|  Probability | 12 | communication | 70  |
|   |  | periodicity | 72  |
|  I |  | recurrent and transient | 74  |
|  Independence | 7 | Stochastic process | 6  |
|  Irreducibility | 71 |  |   |
|  L |   | V |   |
|  Law |  | Variance | 9  |

---

## Summary Table

| Concept | Definition / Formula | Conditions / Notes |
|---|---|---|
| **GoBackN protocol** | Retransmits from the first corrupted/lost packet and then all following packets in order | Receiver accepts packets only in order; skipped packets are not throughput opportunities |
| **Round-trip time** | $m$ slots | If an error occurs at slot $t$, retransmission occurs at $t+m$ |
| **Throughput** | $\eta=\lim_{t\to\infty}R(t)/t$ | Average accepted successful packets per transmitted slot |
| **Error-free feedback model** | $\eta=\dfrac{p_{10}(m)}{p_{10}(m)+mp_{01}}$ | Data errors follow a two-state Markov chain; feedback has no errors |
| **i.i.d. data errors** | $\eta_{iid}=\dfrac{1-\epsilon}{1-\epsilon+m\epsilon}$ | Special case of the error-free feedback model |
| **Four-state bidirectional model** | $\eta=\dfrac{\pi_{(0,0)}}{\pi_{(0,0)}+m(1-\pi_{(0,0)})}$ | Data and feedback channels both have Markov errors |
| **Three-state feedback model** | $\eta=\dfrac{(1-\delta)p_{10}(m)}{[(1-\delta)p_{01}+\delta p_{01}(m)+\delta p_{10}(m)]m+(1-\delta)p_{10}(m)}$ | Feedback errors are i.i.d.; good data state is split into $G_0,G_1$ |
| **Two-state feedback model** | Same throughput as the three-state model | State uncertainty is moved into reward/time distributions |
| **Counting distribution** | $\phi_{ij}(k,n)=P[\sum_{m=0}^{n-1}\mathbf{1}\{X_m=0\}=k,\ X_n=j\mid X_0=i]$ | Counts good slots and final state jointly |
| **Transition split** | $\mathbf{P}=\mathbf{P}(0)+\mathbf{P}(1)$ | $\mathbf{P}(1)$ contains success transitions; $\mathbf{P}(0)$ contains failure transitions |
| **Transform method** | $\varphi(s,z)=[\mathbb{1}-z(\mathbf{P}(1)s+\mathbf{P}(0))]^{-1}$ | $s$ counts successes, $z$ counts transitions |
| **Fixed-$n$ transform** | $\varphi(s,n)=(\mathbf{P}(1)s+\mathbf{P}(0))^n$ | Coefficients of $s^k$ give $\phi(k,n)$ |
| **General metric matrix** | $\psi(s)=\sum_l\mathbf{P}(l)s^l$ | Encodes transition probabilities and integer metric rewards |
| **Multiple metrics** | $\psi_{ij}(\vec{s})=\sum_{A\in\varepsilon(i,j)}P[A]\vec{s}(A)$ | Different variables count different metrics, such as reward and time |
| **Metric mean from $\psi$** | $R_i^{(k)}=\sum_j\left.\partial\psi_{ij}(\vec{s})/\partial s_k\right|_{\vec{s}=1}$ | Row sums of derivatives give expected metric per visit to state $i$ |
| **Reward ratio** | $\lim_{t\to\infty}R^{(1)}(t)/R^{(2)}(t)=\dfrac{\vec{\pi}\,\partial_{s_1}\psi(\vec{1})\,\vec{1}}{\vec{\pi}\,\partial_{s_2}\psi(\vec{1})\,\vec{1}}$ | Requires the stationary distribution of $\psi(\vec{1})$ |
| **GoBackN transform model** | $\psi(s_1,s_2)=\mathbf{P}_S s_1s_2+\mathbf{P}_F s_2^m$ | $s_1$ counts successes; $s_2$ counts slots |
