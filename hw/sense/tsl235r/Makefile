#Makefile used for TSL235R chip demo


UNAME := $(shell uname -m)

ifeq ($(UNAME), x86_64)
	CC := arm-none-linux-gnueabi-gcc
	INCLUDES := -I ../../RaspberryPi_LinuxKernel/include
else
	CC := gcc
	INCLUDES :=
endif
ifeq ($(UNAME), x86)
	CC := arm-none-linux-gnueabi-gcc
	INCLUDES := -I ../../RaspberryPi_LinuxKernel/include
endif

CCFLAGS = -g $(INCLUDES)
CCFLAGS_TEST = -Wall $(INCLUDES)

all:
	$(CC) $(INCLUDES) -lrt tsl_read.c -o tsl_read

test:
	$(CC) $(CCFLAGS_TEST) -lrt tsl_read.c -o tsl_read
	
debug:
	$(CC) $(CCFLAGS) -lrt tsl_read.c -o tsl_read
	
clean:
	rm -rf tsl_read

distclean:
	rm -rf tsl_read
	tar czvf tsl235r.tar.gz tsl_read.c Makefile
