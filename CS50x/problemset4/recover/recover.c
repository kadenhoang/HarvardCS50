#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>

int main(int argc, char *argv[])
{
 //accept only 1 command-line, else remind
    if (argc != 2)
    {
        printf("Usage: ./recover FILE\n");
        return 1;
    }

    uint8_t buffer[512];
    FILE *img = NULL;
    char filename[8];
    int file_count = 0;

    FILE *card = fopen(argv[1], "r");
     //if the image cannot be open,inform
    if (card == NULL)
    {
        printf("Could not open file.\n")
        return 1;
    }
    while(fread(buffer,1,512,card) == 512)
    {
        if (buffer[0] == 0xff &&
            buffer[1] == 0xd8 &&
            buffer[2] == 0xff &&
            (buffer[3] & 0xf0) == 0xe0)

        {
            if (img != NULL)
            {
                fclose(img);
            }
            sprintf(filename, "%03i.jpg", file_count++);
            img = fopen(filename,"w");
        }

        if (img != NULL)
        {
            fwrite(buffer,1,512,img);
        }
    }
    if ( img != NULL)
    {
        fclose(img);
    }
    fclose(card);

    return 0;
}
