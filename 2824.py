# Count Pairs Whose Sum is Less than Target problem

from typing import List

class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:

        # Índices 
        i = 0
        j = 1

        # Lista auxiliar
        listaAuxNums = []

        while i < len (nums):

            while j < len(nums):

                if(nums[i] + nums[j] < target):

                    listaAuxNums.append((i, j))

                
                j += 1

            i += 1
            j = i + 1

        return len(listaAuxNums)