# Roman to Integer problem

from typing import List

class Solution:
    def romanToInt(self, s: str) -> int:

        # Índices
        i = 0
        j = 0

        # Lista auxiliar
        listaAuxS = []

        # Contador
        count = 0

        while i < len(s):

            listaAuxS.append(s[i])

            i += 1

        if("IV" in s):
            count -= 2

        if("IX" in s):
            count -= 2

        if("XL" in s):
            count -= 20

        if("XC" in s):
            count -= 20

        if("CD" in s):
            count -= 200

        if("CM" in s):
            count -= 200

        while j < len(listaAuxS):

            if(listaAuxS[j] == 'I'):

                count += 1

            if(listaAuxS[j] == 'V'):

                count += 5

            if(listaAuxS[j] == 'X'):

                count += 10

            if(listaAuxS[j] == 'L'): 

                count += 50

            if(listaAuxS[j] == 'C'):

                count += 100

            if(listaAuxS[j] == 'D'):

                count += 500

            if(listaAuxS[j] == 'M'):

                count += 1000

            j += 1

        return count

