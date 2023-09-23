# Intersection of Two Arrays problem

from typing import List

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:

        # Índices
        i = 0
        j = 0

        # Lista auxiliar:
        listaAuxNums = []

        # Temp
        temp = 0
        
        if(len(nums1) >= len(nums2)):

            while i < len(nums2):

                temp = nums2[i]

                if((nums2[i] in nums1) and temp not in listaAuxNums):

                    listaAuxNums.append(temp)

                i += 1

        elif(len(nums2) >= len(nums1)):
            while i < len(nums1):

                temp = nums1[i]

                if((nums1[i] in nums2) and temp not in listaAuxNums):

                    listaAuxNums.append(temp)

                i += 1

        
        return listaAuxNums