# Defanging an IP Address problem

from typing import List

class Solution:
    def defangIPaddr(self, address: str) -> str:

        # Índices
        i = 0
        j = 0

        # Lista auxiliar
        listaAuxAdress = []

        # String Final
        stringFinal = ""

        for i in range(len(address)):

            if(address[i] == '.'):
                listaAuxAdress.append('[')
                listaAuxAdress.append('.')
                listaAuxAdress.append(']')
            else:
                listaAuxAdress.append(address[i])

        for j in range(len(listaAuxAdress)):

            stringFinal += (str)(listaAuxAdress[j])

        
        return stringFinal