#include <stdio.h>

int main(){

    int var = 20;

    int* ptr ;
    int ** ptr_to_ptr;

    ptr = &var;
    ptr_to_ptr = &ptr;

    printf("value of var is%d \n",var);
    printf("value at ptr is%d \n",*ptr);
    printf("value at **ptr_to_ptr %d \n",**ptr_to_ptr);

    return 0;


}
