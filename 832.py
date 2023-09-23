# Flipping an Image problem

from typing import List

class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:

        # Índices
        i = 0
        j = 0
        k = 0
        l = 0
        m = 0

        # Listas auxiliares
        listaAux = []
        listaAuxMonta = []
        listaAuxImage = []
        listaRevConcat = []
        listaFinal = []

        for i in range(len(image)):

            listaAux = image[i]
            k = len(listaAux) - 1
            
            for j in range(len(listaAux)):

                listaAuxMonta.append(listaAux[k])
                k -= 1
            
            listaAuxImage = listaAuxMonta
            listaAuxMonta = []
            listaRevConcat.append(listaAuxImage)


        listaAuxImage = []
        listaAuxMonta = []
        listaAux = []

        for l in range(len(listaRevConcat)):

            listaAux = listaRevConcat[l]

            for m in range(len(listaAux)):

                if(listaAux[m] == 1):
                    listaAuxMonta.append(0)
                else:
                    listaAuxMonta.append(1)


            listaAuxImage = listaAuxMonta
            listaAuxMonta = []
            listaFinal.append(listaAuxImage)

        return listaFinal
