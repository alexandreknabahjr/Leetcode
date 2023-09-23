# Power of Two problem

from typing import List


class Solution:
    def isPowerOfTwo(self, n: int) -> bool:

        # Contador
        count = 0

        # Auxiliar
        nAux = n

        while (n != 1):

            n = n / 2
            count += 1
            if(n == 0):
                break

        if(2**count == nAux):
            return True
        else:
            return False