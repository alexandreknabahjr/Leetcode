# Two Sum problem

from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        # Índices do vetor
        i = 0
        j = 1

        while i < len(nums):

            while j < len(nums):

                if((nums[i] + nums[j]) != target):
                    j += 1
                else:
                    numsAux = i, j
                    return numsAux
                
            i = i + 1
            j = i + 1