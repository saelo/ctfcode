cc = gcc
cflags = -m32 -nostdlib -Os
arch = x86

all: pwn

libc.o: libc_$(arch).S libc.c
	$(cc) $(cflags) -r -o libc.o libc_$(arch).S libc.c

pwn: pwn.c libc.o
	$(cc) $(cflags) -o pwn pwn.c libc.o
	#strip pwn
