#include <stdio.h>

int call(int num)
{
    int result=0;
    while(num>=1)
    {
        result = result*10 + num%10;
        num = num/10;
    }
    return result;
}

int main()
{
    int result=1, num=7531;
    result += call(num);
    printf("%d", result);
}