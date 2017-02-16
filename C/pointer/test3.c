#include <stdio.h>

int main(){

    int var[]={10,100,200};
    int i,*ptr;

    ptr = &var[0];

    for(i=0; i<20;i++){

        printf("Address %x has value %d\n",ptr+i,*(ptr+i));

    }

    return 0;

}
