#include <stdio.h>

int fun(int a, int b)
{
    if(b==0)
        return a;
    if(a%2 == 0)
        fun(a+1, b-1);
        
    return fun(a/2, b/2);
}

int main()
{
    int x=20, y=7;
    int z =fun(x,y);
    printf("%d", z);
    return 0;
}