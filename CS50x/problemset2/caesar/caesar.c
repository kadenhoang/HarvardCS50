#include <cs50.h>
#include <stdio.h>
#include <string.h>
#include <ctype.h>

int string_to_int(string s);

int main(int argc, string argv[]) {

// run with just one command
    if (argc != 2)
    {
        printf("Argument not right");
        return 1;
    }

// every character in argv[1] is a digit
    for (int i = 0; i < strlen(argv[1]); i++)
    {
        if (!isdigit(argv[1][i]))
        {
        printf("Usage: ./caesar key\n");
        return 1;
        }
    }

    //convert argv[1] from 'string' to 'int'
    int key = string_to_int(argv[1]);

    //prompt user for plaintext

    string plaintext = get_string("plaintext: ");

    //for each character in the plaintext:
    printf("ciphertext: ");

    // Rotate the characgter if it's a letter
    for (int i = 0; i < strlen(plaintext); i++)
    {
        char c = plaintext[i];

         if (isupper(c))
        {
            printf("%c", (c - 'A' + key) % 26 + 'A');
        }
        else if (islower(c))
        {
            printf("%c", (c - 'a' + key) % 26 + 'a');
        }
        else
        {
            printf("%c", c);
        }
    }
    printf("\n");
    return 0;
}
int string_to_int(string s)
{
    int result = 0;
    for (int i = 0; i < strlen(s); i++)
    {
        result = result * 10 + (s[i] - '0');
    }
    return result;
}


