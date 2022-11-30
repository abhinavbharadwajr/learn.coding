#include <stdio.h>

int main()
{
    int i, j, ch = 'X';
    for(i=5; i>=1; --i)
    {
        for(j=0; j<i && i==3; ++j)
            printf("%c", (ch+j));
    }
    return 0;
}