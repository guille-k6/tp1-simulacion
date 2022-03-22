import matplotlib.pyplot as plt
import random
from statistics import mean
import statistics

numeros0 = [] # arreglo de numeros aleatorios
numeros1 = []
numeros2 = []
numeros3 = []
numeros4 = []

lineaDesvio = [] # desvio esperado

desvio0 = [] 
desvio1 = [] 
desvio2 = [] 
desvio3 = [] 
desvio4 = [] 

for x in range(0,31):
    num = (random.randint(0,36))
    numeros0.append(num)
    desvio0.append(statistics.pstdev(numeros0))
    lineaDesvio.append(10.677)

for x in range(0,31):
    num = (random.randint(0,36))
    numeros1.append(num)
    desvio1.append(statistics.pstdev(numeros1))
    
for x in range(0,31):
    num = (random.randint(0,36))
    numeros2.append(num)
    desvio2.append(statistics.pstdev(numeros2))
    
for x in range(0,31):
    num = (random.randint(0,36))
    numeros3.append(num)
    desvio3.append(statistics.pstdev(numeros3))
    
for x in range(0,31):
    num = (random.randint(0,36))
    numeros4.append(num)
    desvio4.append(statistics.pstdev(numeros4))
    

plt.title("Desvío poblacional")
plt.plot(desvio0)
plt.plot(desvio1) 
plt.plot(desvio2)
plt.plot(desvio3)
plt.plot(desvio4)
plt.xlabel("n = número de tiradas")
plt.ylabel("desvío poblacional")
plt.plot(lineaDesvio, label="desvío esperado")
plt.legend(loc="upper right")