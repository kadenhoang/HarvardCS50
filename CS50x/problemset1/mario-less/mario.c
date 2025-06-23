#include <cs50.h>
#include <stdio.h>

void print_row(int spaces, int bricks);

int main(void)
{
    //promt the user for the pyramid's height
    int h;
    do
    {
        h = get_int("Height: ");
    }
    while (h < 1);

    //print the pyramid
    for (int i = 0; i < h; i++)
    {
        int spaces = h - i - 1;
        int bricks = i + 1;
        print_row(spaces, bricks);
    }
}
void print_row(int spaces, int bricks)
{
    for ( int i = 0; i < spaces; i++)
    {
        printf(" ");
    }
    for ( int i = 0; i < bricks; i++)
    {
        printf("#");
    }
    printf("\n");

}
