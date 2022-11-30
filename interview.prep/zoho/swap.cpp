#include <stdio.h>

int main()
{
    int arr[] = {-1,-5,5,4,2,-2};
    int size = 6;
    int last = arr[size-1];
    arr[size-1] = -1;
    for(int i=size-2; i>=0; i=i-1)
    {
        int temp = arr[i];
        arr[i] = last;
        if(last<temp)
        {
            last = temp;
        }
    }
    for(int i=0; i<last; ++i)
    {
        printf("%d",arr[i]);
    }
}