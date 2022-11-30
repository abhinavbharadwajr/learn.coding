#include <stdio.h>

int func(int i,int j)
{
    return i++ * --j;
}

int main()
{
    int result = 0, loop = 5;
    while (loop--)
    {
        result = result + func(loop, loop);
    }
    printf("%d", result);
}