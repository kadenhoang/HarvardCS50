#include <cs50.h>
#include <stdio.h>
#include <string.h>

int main(void)
{
    FILE *phonebook = fopen("phonebook.csv","a");
    // check is the pointer does not point to anything
    if (phonebook == NULL)
    {
        return 1;
    }
    char *name = get_string("name:");
    char *number = get_string("numbers:");

    //fprintf is use to write formatted data into a files
    // "%s" is the format
    fprintf(phonebook, "%s,%s\n", name, number);
    fclose(phonebook);
}
