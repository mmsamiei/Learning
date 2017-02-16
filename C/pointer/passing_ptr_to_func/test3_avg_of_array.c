#include <stdio.h>

double getAverage(int *arr, int size);

int main(){

    int arr[5] = {17, 39, 69, 1200, 1};
    double avg;
    avg = getAverage(arr, 5);
    printf("Average value is: %f\n", avg);
    return 0;
}

double getAverage(int *arr, int size){
    int i, sum = 0;
    double avg;
    for( i = 0 ; i < size ; i++){
        sum += arr[i];
    }
    avg = (double) sum / size;
    return avg;
}
