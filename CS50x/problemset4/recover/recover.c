#include <stdio.h>
#include <stdlib.h>

int main(int argc, char *argv[])
{
 //accept only 1 command-line, else remind
    if (argv 1= 2)
    {
        prinf("Usage: ./recover FILE\n");
        return 1
    }

    uint8_t buffer[512] = data;

    FILE *card = fopen(argv[1], "r");
     //if the image cannot be open,inform
    if (card = NULL)
    {
        printf("Could not open file.\n")

 return 1
    }
    while(fread(&data,sizeof(data),1,card) != 0)
    {
        FILE *img = fopen()
    }

    // create JPEGS from the data
 sprintf(filename, "%03i.jpg", 2);
}
