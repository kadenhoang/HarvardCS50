#include <cs50.h>
#include <stdio.h>
#include <string.h>

typedef struct
{
    string name;
    string number;
}
person;

int main (void)
{
    person people[2];

    people[0].name = "Vu";
    people[0].number = "1";
    people[1].name = "An";
    people[1].number = "3";

    string name = get_string("name: ");

    for (int i = 0; i < 2; i++)
    {
        if(strcmp(people[i].name, name) == 0)
            {
                printf("Found %s\n", people[i].number);
                return 0;
            }
        else
            {
                printf("Not Found\n
                    ");
                return 1;
            }
    }
}

