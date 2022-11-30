#include <stdio.h>

int main()
{
    int i;
    int a[6] = {4,7,3,9,5,11};
    int b[6] = {0,0,0,0,0,0};
    
    for(i=4; i>=0; i--)
    {
        if(i%2!=0 && (i+1 <= 6))
        {
            b[i+1] = a[i]++;
            b[i] = a[i+1];
        }
    }
    
    for(i=0; i<6; i++)
        printf("%d", b[i]);
}