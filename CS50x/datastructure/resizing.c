#include <stdio.h>

int main(void)
{

    int *list = malloc(3 * sizeof(int));
    if (list = NULL)
    {
        return 1;
    }


    list[0] = 1;
    list[1] = 2;
    list[2] = 3;

    //realloc helps create new storing location without
    //moving things around (create a for loop and assign list to tmp)
    int *tmp = realloc(4 * sizeof(int))
    if (tmp == NULL)
    {
        free(list);
        return 1;
    }

    tmp[3] = 4

    //free up the previous data to prevent overflow or leak
    free(list);

    list = tmp;

    for(int i = 0; i < 4; i++)
    {
        printf("%i\n", list[i]);
    }
}
