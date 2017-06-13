#Code for tutorial found at 
#https://www.wzdftpd.net/blog/python-scripts-in-gdb.html


class PrintGList( gdb.Command ):
    """print Glib Glist: wsd_print_glist list objecttpe

Iterate through the list if nodes in a Glist and display
a human-readable form of the objects."""

    def __init__( self ):
        
        gdb.Command.__init__( self, "wzd_print_glist", gdb.COMMAND_DATA, gdb.COMPLETE_SYMBOL, True)


    def invoke( self, arg, from_tty ):
        
        arg_list = gdb.string_to_argv( arg )

        if len( arg_list ) < 2:
            print "Usage: wzd_print_glist list objectype"
            return

        gdb.parse_and_eval( arg_list[0] )
