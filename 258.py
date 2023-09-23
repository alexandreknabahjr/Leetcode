# Add Digits problem

from typing import List

class Solution:
    def addDigits(self, num: int) -> int:

        # Converte para string
        n = str(num)

        # Índices
        i = 0
        j = 0
        k = 0
        l = 0
        m = 0
        o = 0

        # Lista auxiliar
        listaAuxNum = []
        listaAuxNum2 = []

        # Contador
        count = 0

        while i < len(n):

            listaAuxNum.append(n[i])
            listaAuxNum2.append(n[i])

            i += 1

        
        while len(listaAuxNum) >= 1:

            while j < len(listaAuxNum):

                count += int(listaAuxNum[j])

                j += 1

            n = str(count)
            listaAuxNum2.clear()

            while k < len(n):

                listaAuxNum2.append(n[k])

                k += 1

            listaAuxNum = listaAuxNum2
        
        n = str(count)
        count = 0

        while l < len(n):

            listaAuxNum.append(n[l])

            l += 1

        while m < len(listaAuxNum):

            count += int(listaAuxNum[m])

            m += 1

        if(count < 10):
            return count
        else:
            n = str(count)
            count = 0
            listaAuxNum = n[0], n[1]
            while o < len(listaAuxNum):

                count += (int)(listaAuxNum[o])

                o += 1

            return count