// Remove Duplicates from Sorted Array problem

#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int removeDuplicates(vector<int>& nums) {

        // Índices
        int i = 0;
        int j = 1;
        int k = 0;

        // Contador
        int count = 0;

        while(i < nums.size()){
            while(j < nums.size()){
                if(nums[i] == nums[j]){
                    nums[j] = 101;
                }

                j++;

            }

            i++;
            j = i + 1;
        }

        sort(nums.begin(), nums.end());

        while(k < nums.size()){
            if((nums[k] <= 100) && (nums[k] >= -100)){
                count++;
            }

            k++;
        }

        return count;
        
    }
};