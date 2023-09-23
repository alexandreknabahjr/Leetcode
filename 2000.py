# Reverse Prefix of Word problem

from typing import List

class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:

        # Lista auxiliar
        listaAuxWord = []
        listaWord = []

        # Contador
        count = 0

        # String
        stringAux = ""

        if(ch == ""):
            return word

        for j in range(len(word)):
            listaWord.append(word[j])

        if(ch not in listaWord):
            return word
        
        for i in range(len(word)):

            listaAuxWord.append(word[i])
            listaWord[i] = '-'
            count += 1

            if((word[i] == ch)):
                break

        listaAuxWord.reverse()

        for k in range(len(listaAuxWord)):

            listaWord[k] = listaAuxWord[k]

        
        for l in range(len(listaWord)):

            stringAux += (str)(listaWord[l])

        return stringAux