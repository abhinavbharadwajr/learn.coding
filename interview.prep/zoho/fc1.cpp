#include <stdio.h>

int main()
{
    int N = 371, T=N, S = 0;
    
    while(T>0)
    {
        int D = T%10;
        int P = D*D*D;
        S = P + S;
        T = T/10;
    }
    
    if(S == N)
        printf("%d", S*2);
    else
        printf("%d", S);
}