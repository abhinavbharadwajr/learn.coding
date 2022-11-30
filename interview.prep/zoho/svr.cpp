#include <stdio.h>

int main()
{
    int a=400, i, b, sum=10, j, val, rem;
    b=a;
    for(i=0; b>0; b=b/10)
    {
        rem = b/5;
        for(j=i, val=2; j>=0; --j)
        {
            val *= 10;
        }
        if(rem<100)
            rem += b;
        sum = sum + val + rem;
    }
    
    printf("%d", sum);
    
}