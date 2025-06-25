#include <cs50.h>
#include <stdio.h>

int main(void)
{
    int number [] = {5, 2 ,3 ,8 ,6};
    int n = get_int("Enter a ineger:");

    for (int i = 0; i < number[i]; i ++)
    {
        if (number[i] == n)
        {
            printf("found\n");
            return 0;
        }
    }
    printf("Not found\n");
    return 1;
}
