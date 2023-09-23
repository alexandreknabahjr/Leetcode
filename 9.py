# Palindrome Number problem

from typing import List

class Solution:
    def isPalindrome(self, x: int) -> bool:

        # Converte para string
        n = str(x)

        # Índices 
        i = 0
        j = len(n)
        k = 0
        l = 0

        # Lista auxiliar
        listaAux = []
        listaAuxPal = []

        # Contador
        count = 0

        while i < len(n):

            listaAux.append(n[i])
            listaAuxPal.append(n[j - 1])
            i += 1
            j -= 1


        while k < len(listaAux):

            if(listaAuxPal[l] == listaAux[k]):
                count += 1

            l += 1
            k += 1


        if(len(listaAux) == count):
            return True
        else:
            return False

