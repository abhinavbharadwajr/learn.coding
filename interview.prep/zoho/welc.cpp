#include <stdio.h>

int main()
{
    int y = 10;
    while(y != 2)
    {
        for(int i=y; i>y; i+=1)
        {
            if (i%2 == 0)
                printf("Welcome\n");
            y = y-3;
            printf("Welcome\n");
        }
        y = --y-1;
        printf("Welcome\n");
    }
}