#include <stdio.h>

int main()
{
    int i, j;
    i = j = 3;
    while(--i && j++)
        printf("%d%d", i, j);
    return 0;    
}