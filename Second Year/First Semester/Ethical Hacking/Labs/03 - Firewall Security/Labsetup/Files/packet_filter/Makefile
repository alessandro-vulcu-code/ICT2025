obj-m += seedFilter.o

KDIR ?= /lib/modules/$(shell uname -r)/build

.PHONY: all clean ins rm

# Kbuild requires the absolute external module path to contain no spaces.
all:
	@set -eu; \
	build_dir=$$(mktemp -d /tmp/seed-filter.XXXXXXXX); \
	trap 'rm -r -- "$$build_dir"' EXIT; \
	cp Makefile seedFilter.c "$$build_dir/"; \
	$(MAKE) -C "$(KDIR)" M="$$build_dir" modules; \
	cp "$$build_dir/seedFilter.ko" .

clean:
	$(RM) seedFilter.ko

ins:
	sudo dmesg -C
	sudo insmod seedFilter.ko

rm:
	sudo rmmod seedFilter

