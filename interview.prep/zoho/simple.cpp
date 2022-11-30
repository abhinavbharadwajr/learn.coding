#include <stdio.h>

int main()
{
    int num = 9;
    for(int i=0; i<num; i+=1)
    {
        if(num-i < 6)
            printf("%d",num-i);
        else
            printf("%d",i*i);
    }
}