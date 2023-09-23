# Plus One problem

from typing import List

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:

        # Índices
        k = len(digits) - 1
        l = 0

        # Lista auxiliar
        listaAuxDigits = []
        listaAux = []

        # Contador
        count = 0
        power = 0

        # String
        stringDigits = ""

        for i in range(len(digits)):

            listaAuxDigits.append((str)(digits[k]))

            k -= 1

        
        for j in range(len(listaAuxDigits)):

            power = 10 ** j
            count += (int)(listaAuxDigits[j]) * power

        
        count = count + 1

        stringDigits = str(count)

        while l < len(stringDigits):
            
            listaAux.append((int)(stringDigits[l]))

            l += 1

        return listaAux