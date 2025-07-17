#include "helpers.h"
#include <math.h>


// Convert image to grayscale
void grayscale(int height, int width, RGBTRIPLE image[height][width])
{
    //loop through the rows and the columns
    for(int i = 0; i < height; i ++)
        {
            for(int j = 0, j < width; j ++)
            {
                //fine the avarage value of RGB
                float avg = (image[i][j].rgbtRed + image[i][j].rgbtBlue + image[i][j].rgbtGreen) / 3;
                //round the result
                int roundedavg = round(avg);
                //update pixel value
                image[i][j].rgbtRed = image[i][j].rgbtBlue = image[i][j].rgbtGreen = roundedavg;

            }
        }
    return;
}

// Convert image to sepia
void sepia(int height, int width, RGBTRIPLE image[height][width])
{
    return;
}

// Reflect image horizontally
void reflect(int height, int width, RGBTRIPLE image[height][width])
{
    return;
}

// Blur image
void blur(int height, int width, RGBTRIPLE image[height][width])
{
    return;
}
