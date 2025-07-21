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
     for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            int originalRed =  image[i][j].rgbtRed;
            int originalGreen = image[i][j].rgbtGreen;
            int originalBlue =  image[i][j].rgbtBlue
            // Compute sepia values

            int sepiaRed = round(0.393 * originalRed + 0.769 * originalGreen + 0.189 * originalBlue);
            int sepiaGreen = round(0.349 * originalRed + 0.686 * originalGreen + 0.168 * originalBlue);
            int sepiaBlue = round(0.272 * originalRed + 0.534 * originalGreen + 0.131 * originalBlue);

            //limit values to 225
            if (sepiaRed > 255)
            {
                sepiaRed = 255;
            }
            if (sepiaGreen > 255)
            {
                sepiaGreen = 255;
            }
            if (sepiaBlue > 255)
            {
                sepiaBlue = 255;
            }

            // Update pixel with sepia values
            image[i][j]rgbtRed = sepiaRed;
            image[i][j]rgbtGreen = sepiaGreen;
            image[i][j]rgbtBlue = sepiaBlue;


        }

    return;
}
}


// Reflect image horizontally
void reflect(int height, int width, RGBTRIPLE image[height][width])
{
    for (int i = 0; i < height; i ++)
    {
        for(int j = 0; j < width; j++)
        {
            
        }
    }
    return;
}

// Blur image
void blur(int height, int width, RGBTRIPLE image[height][width])
{
    return;
}
