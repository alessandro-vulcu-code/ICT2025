obj-m += hello.o

KDIR ?= /lib/modules/$(shell uname -r)/build

.PHONY: all clean

# Kbuild requires the absolute external module path to contain no spaces.
all:
	@set -eu; \
	build_dir=$$(mktemp -d /tmp/seed-hello.XXXXXXXX); \
	trap 'rm -r -- "$$build_dir"' EXIT; \
	cp Makefile hello.c "$$build_dir/"; \
	$(MAKE) -C "$(KDIR)" M="$$build_dir" modules; \
	cp "$$build_dir/hello.ko" .

clean:
	$(RM) hello.ko

