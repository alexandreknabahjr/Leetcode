# Smallest Even Multiple problem

class Solution:
    def smallestEvenMultiple(self, n: int) -> int:

        # Índice
        i = n

        while(True):

            if((i % 2 == 0) and (i % n == 0)):
                return i

            i += 1