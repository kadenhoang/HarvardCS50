#include "helpers.h"
#include <math.h>


// Convert image to grayscale
void grayscale(int height, int width, RGBTRIPLE image[height][width])
{
    //loop through the rows and the columns
    for(int i = 0; i < height; i ++)
        {
            for(int j = 0; j < width; j ++)
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
            int originalBlue =  image[i][j].rgbtBlue;
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
            image[i][j].rgbtRed = sepiaRed;
            image[i][j].rgbtGreen = sepiaGreen;
            image[i][j].rgbtBlue = sepiaBlue;


        }

}
}


// Reflect image horizontally
void reflect(int height, int width, RGBTRIPLE image[height][width])
{
    for (int i = 0; i < height; i ++)
    {
        for(int j = 0; j < width; j++)
        {
            RGBTRIPLE temp = image[i][j];
            image[i][j] = image[i][width - 1 - j];
            image[i][width - 1 - j] = temp;


        }
    }
}

// Blur image
void blur(int height, int width, RGBTRIPLE image[height][width])
{
       RGBTRIPLE copy[height][width];
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            copy[i][j] = image[i][j];
        }
    }

    // Apply blur
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            int redSum = 0;
            int greenSum = 0;
            int blueSum = 0;
            int count = 0;

            // Loop over 3x3 grid around pixel (i, j)
            for (int di = -1; di <= 1; di++)
            {
                for (int dj = -1; dj <= 1; dj++)
                {
                    int ni = i + di;
                    int nj = j + dj;

                    // Check bounds
                    if (ni >= 0 && ni < height && nj >= 0 && nj < width)
                    {
                        redSum   += copy[ni][nj].rgbtRed;
                        greenSum += copy[ni][nj].rgbtGreen;
                        blueSum  += copy[ni][nj].rgbtBlue;
                        count++;
                    }
                }
            }

            // Compute average
            image[i][j].rgbtRed   = round((float) redSum / count);
            image[i][j].rgbtGreen = round((float) greenSum / count);
            image[i][j].rgbtBlue  = round((float) blueSum / count);
        }
    }
}
