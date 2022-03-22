import matplotlib.pyplot as plt
import random
from statistics import mean
import statistics

def frec(arra):
    cantDe8 = arra.count(8)
    fr = cantDe8 / len(arra)
    return fr

numeros0 = [] # arreglo de numeros aleatorios
numeros1 = []
numeros2 = []
numeros3 = []
numeros4 = []

lineaFrecRel = [] # Frecuencia relativa esperada

frecRel80 = [] # Frecuencia relativa
frecRel81 = []
frecRel82 = []
frecRel83 = []
frecRel84 = []

for x in range(0,100):
    num = (random.randint(0,36))
    numeros0.append(num)
    lineaFrecRel.append(1/37)
    frecRel80.append(frec(numeros0))

    
for x in range(0,100):
    num = (random.randint(0,36))
    numeros1.append(num)
    frecRel81.append(frec(numeros1))

    
for x in range(0,100):
    num = (random.randint(0,36))
    numeros2.append(num)
    frecRel82.append(frec(numeros2))

    
for x in range(0,100):
    num = (random.randint(0,36))
    numeros3.append(num)
    frecRel83.append(frec(numeros3))
    
for x in range(0,100):
    num = (random.randint(0,36))
    numeros4.append(num)
    frecRel84.append(frec(numeros4))
    
plt.title("Frecuencia relativa")
plt.plot(frecRel80)
plt.plot(frecRel81) 
plt.plot(frecRel82)
plt.plot(frecRel83)
plt.plot(frecRel84)
plt.xlabel("n = número de tiradas")
plt.ylabel("frecuencia relativa")
plt.plot(lineaFrecRel, label="fr del 8 esperada")
plt.legend(loc="upper right")