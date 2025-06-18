#include <cs50.h>
#include <stdio.h>
#include <string.h>
#include <ctype.h>

int main(void)
{
 string name = get_string("Name: ");

 printf("Name in uppercase: ");

 for(int i = 0, length = strlen(name); i < length; i++)
 {
    //toupper is included in ctype.h library
    printf("%c", toupper(name[i]));
 }
 printf("\n");
}
