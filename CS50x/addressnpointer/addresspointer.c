#include <stdio.h>

int main(void)
{
    // char * is string of C
    char *n = "Hello";

// * = pointer that get the value in the address
//& = show address of smt

    printf("%p\n", n );
    printf("%p\n", &n[0]);
    printf("%p\n", &n[1]);
    printf("%p\n", &n[2]);
}
