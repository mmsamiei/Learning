#include <stdio.h>

int main(){

    int arr[5];

    for(int i=0;i<5;i++){
        arr[i] = (i+1)*10;
    }

    char * ptr;

    ptr = &arr[0];


    printf("address %x has value %d\n",ptr,*(ptr));
    printf("address %x has value %d\n",ptr+1,*(ptr+1));
}
