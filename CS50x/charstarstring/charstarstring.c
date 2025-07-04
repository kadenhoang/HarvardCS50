#include <stdio.h>

int main(void)
{
    //C use char * to represent string
    //string is included in cs50 library, not in C inself
    char *s = "shut the fuck up";
    //even though string does not exits in C but %s does
    printf("%s\n", s);
}
