#include <stdio.h>

int main()
{
    int num=8;
    int i=63;
    while(i>num)
    {
        switch(num%9)
        {
            case 0 :
                num = num + 4;
            case 1 :
                num = num + 7;
            case 2 :
                num = num + 9;
            default :
                num = num + 10;
        }
        i--;
    }
    
    printf("%d %d", num, i);
    return 0;
}