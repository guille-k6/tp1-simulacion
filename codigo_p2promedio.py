import matplotlib.pyplot as plt
import random
from statistics import mean
import statistics

numeros0 = [] # arreglo de numeros aleatorios
numeros1 = []
numeros2 = []
numeros3 = []
numeros4 = []

promedios0 = [] # valor promedio
promedios1 = []
promedios2 = []
promedios3 = []
promedios4 = []


lineaPromedio = [] 

def Promedio(l):
    prom = mean(l)
    return prom


for x in range(0,31):
    num = (random.randint(0,36))
    numeros0.append(num)
    promedios0.append(Promedio(numeros0))
    lineaPromedio.append(18.0)

for x in range(0,31):
    num = (random.randint(0,36))
    numeros1.append(num)
    promedios1.append(Promedio(numeros1))

for x in range(0,31):
    num = (random.randint(0,36))
    numeros2.append(num)
    promedios2.append(Promedio(numeros2))

for x in range(0,31):
    num = (random.randint(0,36))
    numeros3.append(num)
    promedios3.append(Promedio(numeros3))

for x in range(0,31):
    num = (random.randint(0,36))
    numeros4.append(num)
    promedios4.append(Promedio(numeros4))
    

plt.title("Promedio de las tiradas")
plt.plot(lineaPromedio, label="valor esperado")
plt.plot(promedios0)
plt.plot(promedios1)
plt.plot(promedios2)
plt.plot(promedios3)
plt.plot(promedios4)
plt.xlabel("n = número de tiradas")
plt.ylabel("valor promedio")
plt.legend(loc="upper right")