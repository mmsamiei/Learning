#include <stdio.h>

void sumAndSub(int a,int b, int *sum,int *sub);

int main(){

    int a = 5 ;
    int b = 8;

    int sum;
    int sub;
    sumAndSub( a, b, &sum, &sub);

    printf("sum is %d",sum);
    printf("sub is %d",sub);

}

void sumAndSub(int a, int b, int *sum, int *sub){
    *sum = a + b;
    *sub = a - b;
}
