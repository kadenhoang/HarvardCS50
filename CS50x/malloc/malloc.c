#include <stdio.h>
#include <ctype.h>
#include <cs50.h>
#include <stdlib.h>
#include <string.h>

int main(void)
{
    char *s = get_string("s:");

    //malloc create different bits to hold value(think of empty box to hold smt)
    //I want to hold the /n so it is length of s + 1
    char *t = malloc(strlen(s)+1);

    //use for loop to assign value to empty bits
    for(int i = 0, n = strlen(s); i <= n; i++)
    {
        t[i] = s[i];
    }
    // why not copy t = s?
    //because it will copy the s location and when I change t as bellow it will change s
    //so I do this to seperate t to a different address to modify it freely
    //or I can just create a new string and assign t
    if (strlen(t) > 0)
    {
        t[0] = toupper(t[0]);
    }

    printf("%s\n",s);
    printf("%s\n",t);
}
