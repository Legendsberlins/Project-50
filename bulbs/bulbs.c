#include <cs50.h>
#include <stdio.h>
#include <string.h>

const int BITS_IN_BYTE = 8;

void print_bulb(int bit);

int main(void)
{
    //get text
    string text = get_string("Text: ");
    //convert the indexes of the text to decimal ASCII
    int len = strlen(text);
    for (int i = 0; i < len; i++)
    {
        int decimal = text[i];
        int binary[] = {0, 0, 0, 0, 0, 0, 0, 0};
        int j = 0;
        while (decimal > 0)
            //convert the decimal to binary(8 bits)
        {
            binary[j] = decimal % 2;
            decimal = decimal / 2;
            j++;
        }
        //print for 0's and 1's in 8 bits
        for (int k = BITS_IN_BYTE - 1; k >= 0; k--)
        {
            print_bulb(binary[k]);
        }
        printf("\n");
    }
}

void print_bulb(int bit)
{
    if (bit == 0)
    {
        // Dark emoji
        printf("\U000026AB");
    }
    else if (bit == 1)
    {
        // Light emoji
        printf("\U0001F7E1");
    }
}




