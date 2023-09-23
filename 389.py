# Find the Difference problem

from typing import List

class Solution:
    def findTheDifference(self, s: str, t: str) -> str:

        # Índices
        i = 0
        j = 0
        k = 0
        l = 0

        # Lista auxiliar
        listaAuxS = []
        listaAuxT = []

        # Letra
        letter = ''

        # Caso base
        if(s == ''):
            return t


        while i < len(s):

            listaAuxS.append(s[i])
            i += 1

        listaAuxS.sort()

        while j < len(t):

            listaAuxT.append(t[j])
            j += 1

        listaAuxT.sort()
        
        while k < len(listaAuxT):
            
            while l < len(listaAuxS):

                if(listaAuxT[k] == listaAuxS[l]):
                    listaAuxT.remove(listaAuxT[k])

                l += 1

            k += 1
            l = 0

        letter = listaAuxT[0]

        return letter