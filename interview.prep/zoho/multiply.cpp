#include <stdio.h>

int main()
{
    int result = 1;
    for(int p=1; p>=3; p++)
    {
        for(int q=3; q>=p; q--)
        {
            result *= -1;
        }
        for(int r=1; r<=p; r++)
        {
            result *= 2;
        }
    }
    
    printf("%d",result);
}