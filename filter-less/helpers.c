#include "helpers.h"
#include <math.h>

// Convert image to grayscale
void grayscale(int height, int width, RGBTRIPLE image[height][width])
{
    //Initialize variable average
    int average = 0;
    //Loop around rows and columns
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            //Create new variables and assign them to the image[i][j].rgbt variables for shorter code
            int red = image[i][j].rgbtRed;
            int blue = image[i][j].rgbtBlue;
            int green = image[i][j].rgbtGreen;

            //Calculate the average
            average = round((red + blue + green) / 3.0);
            //Assign average values to original col and row variables
            image[i][j].rgbtRed = average;
            image[i][j].rgbtBlue = average;
            image[i][j].rgbtGreen = average;
        }
    }
    return;
}

// Convert image to sepia
void sepia(int height, int width, RGBTRIPLE image[height][width])
{
    //Initialize sepia variables
    int sepiaRed, sepiaGreen, sepiaBlue = 0;
    //Loop around rows and columns
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            //Create new variables and assign them to the image[i][j].rgbt variables for shorter code
            int red = image[i][j].rgbtRed;
            int blue = image[i][j].rgbtBlue;
            int green = image[i][j].rgbtGreen;

            //Sepia conversion
            sepiaRed = round(.393 * red + .769 * green + .189 * blue);
            sepiaGreen = round(.349 * red + .686 * green + .168 * blue);
            sepiaBlue = round(.272 * red + .534 * green + .131 * blue);

            //Setting limits to the sepia values
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
            //Assign sepia values to original col and row variables
            image[i][j].rgbtRed = sepiaRed;
            image[i][j].rgbtGreen = sepiaGreen;
            image[i][j].rgbtBlue = sepiaBlue;
        }
    }
    return;
}

// Reflect image horizontally
void reflect(int height, int width, RGBTRIPLE image[height][width])
{
    //Loop round rows and columns
    for (int i = 0; i < height; i++)
    {
        //Make loop to be < 1/2 of the width in order to indicate a stopping point
        for (int j = 0 ; j < width / 2; j++)
        {
            //Declare a temp variable for swap
            RGBTRIPLE temp =  image[i][j];
            //Swap array values
            image[i][j] = image[i][width - (j + 1)];
            image[i][width - (j + 1)] = temp;
        }
    }
    return;
}

// Blur image
void blur(int height, int width, RGBTRIPLE image[height][width])
{
    //Create copy of image
    RGBTRIPLE temp[height][width];
    //Loop round variables
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            temp[i][j] = image[i][j];
        }
    }

    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            int red = 0;
            int green = 0;
            int blue = 0;
            float counter = 0.00;

            //Look out for neighboring pixels
            for (int x = -1; x < 2; x++)
            {
                for (int y = -1; y < 2; y++)
                {
                    int totalX = i + x;
                    int totalY = j + y;
                    //Check validity of neighboring pixels
                    if (totalX < 0 || totalX > (height - 1) || totalY < 0 || totalY > (width - 1))
                    {
                        continue;
                    }

                    red += image[totalX][totalY].rgbtRed;
                    green += image[totalX][totalY].rgbtGreen;
                    blue += image[totalX][totalY].rgbtBlue;

                    counter++;
                }

                temp[i][j].rgbtRed = round(red / counter);
                temp[i][j].rgbtGreen = round(green / counter);
                temp[i][j].rgbtBlue = round(blue / counter);
            }
        }
    }
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            image[i][j].rgbtRed = temp[i][j].rgbtRed;
            image[i][j].rgbtGreen = temp[i][j].rgbtGreen;
            image[i][j].rgbtBlue = temp[i][j].rgbtBlue;
        }
    }
    return;
}