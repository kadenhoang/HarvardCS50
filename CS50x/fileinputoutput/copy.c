#include <cs50.h>
#include <stdint.h>

typedef uint8_t BYTE;

int main(void)
{

FILE *src = fopen(argv[1],"r");
FILE *dst = fopen(argv[2],"w");

BYTE b; //b will be 1 byte

// give the func the address of b to store data in,
// regonize the size of b(1 byte)
// read 1 byte at a time from a source file.
while fread(&b,sizeof(b),1,src != 0)
{
    fwrite(&b,sizeof(b),1,dst);
}
fclose(dst);
fclose(scr);
}
