#include <stdio.h>

int main()
{
    int p=1, q=3, r=0, result=0;
    
    for(int idx=0; idx<10; idx++)
    {
        r = p + q;
        if(r<10)
            result += r;
        p = q;
        q = r;
    }
    
    printf("%d", result);
}