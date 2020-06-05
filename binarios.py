import numpy as np
import math
print("Escriba el número que desea convertir en binario binario")
num = int(input())

valorD = num
valorM = 0 
valorBinario = []

while valorD != 0:
    binario = np.array([valorM])
    valorD = round(valorD)
    valorM = round(valorD%2)
    valorD = math.floor(valorD/2)
    #print("/",valorD)
    #print("%",valorM)
    valorBinario.append(valorM)
   
    
valorBinario.reverse()
print(valorBinario)



    






