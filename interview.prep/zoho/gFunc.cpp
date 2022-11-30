#include <stdio.h>

int G(int x)
{
    static int y = 4;
    y += -1;
    return (y+x);
}

int F(int x)
{
    int y;
    y = G(x);
    return (y);
}

int main()
{
    int x=5, y=3, count;
    for (count=1; count<=2; ++count)
    {
        y += F(x) + G(x);
        printf("%d", y);
    }
}