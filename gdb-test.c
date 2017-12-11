#include <glib.h>
#include <stdio.h>

#define MY_MACRO \
    printf("this is my macro.c\n");\
    printf("Also this\n");

#define THIS_VAL 23

int main()
{

  int one = 1;
  int two = 2;
  
  GList *list = NULL;
  GList *res = NULL;

  res = g_list_append( list, &two );
  res = g_list_append( res, &one );
  
  MY_MACRO;
  
  printf( "HELLO\n" );
  return 0;

}
