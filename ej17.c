#include <stdio.h>
#include <math.h>

int findNumbers(int* nums, int numsSize) {

    int count = 0;

    for(int i = 0; i < numsSize; i++){
        if(nums[i]==0){
            continue;
        }
        if(((int)(floor(log10(abs(nums[i]))) + 1)%2) == 0){
            count++;
        }
    }
    return count;

}