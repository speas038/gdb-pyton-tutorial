
CFLAGS=-I/usr/include/glib-2.0 -I/usr/lib/x86_64-linux-gnu/glib-2.0/include -lglib-2.0

all:
	gcc $(CFLAGS) gdb-test.c -o gdb-test
