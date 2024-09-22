#include <cs50.h>
#include <stdio.h>

int main(void)
{
    //prompt for height
    int height;
    do
    {
        height = get_int("Height: ");
    }
    while (height < 1 || height > 8);
    //prompt for row
    for (int row = 0; row < height; row++)
    {
        //prompt for dot
        for (int dot = 0; dot <= height - row - 1; dot++)
        {
            printf(" ");
        }
        //prompt for column
        for (int col = 0; col < row + 1; col++)
            //final print
        {
            printf("#");
        }
        printf("\n");
    }


}