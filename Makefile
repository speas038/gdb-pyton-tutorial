
DBGFLAGS=-gdwarf-2 -g3
CFLAGS=-I/usr/include/glib-2.0 -I/usr/lib/x86_64-linux-gnu/glib-2.0/include -lglib-2.0

all:
	gcc $(DBGFLAGS) gdb-test.c -o gdb-test $(CFLAGS)
