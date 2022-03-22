import matplotlib.pyplot as plt
import random
from statistics import mean
import statistics

#final

def Promedio(l):
    prom = mean(l)
    return prom

def frec(arra):
    cantDe8 = arra.count(8)
    fr = cantDe8 / len(arra)
    return fr

# DESVIO
numeros = [] # arreglo de numeros aleatorios
desvio = [] # desvio acumulado
lineaDesvio = [] # desvio esperado
promedios = [] # valor promedio
lineaPromedio = [] # valor promedio esperado
lineaFrecRel = [] # Frecuencia relativa esperada
frecRel8 = [] # Frecuencia relativa
linea = [] # desvio esperado
varianza = [] # varianza
lineaVar = [] # varianza esperada

for x in range(0,31):
    num = (random.randint(0,36))
    numeros.append(num)
        #DESVIO
    desvio.append(statistics.pstdev(numeros))
    lineaDesvio.append(10.677)
        #PROMEDIO
    promedios.append(Promedio(numeros))
    lineaPromedio.append(18.0)
        #FRECUENCIA RELATIVA
    lineaFrecRel.append(1/37)
    frecRel8.append(frec(numeros))
        #VARIANZA
    varianza.append(statistics.pvariance(numeros))
    lineaVar.append(114)
    
fig, axs = plt.subplots(2, 2)
axs[0, 0].plot(promedios, label="valor promedio de las tiradas")
axs[0, 0].set_title('Axis [0, 0]')
axs[0, 0].plot(lineaPromedio, label="valor promedio esperado")
axs[0, 0].set_title('Promedio')
axs[1, 0].plot(desvio, label="desvío de los valores obtenidos")
axs[1, 0].set_title('Axis [1, 0]')
axs[1, 0].plot(lineaDesvio, label="desvío esperado")
axs[1, 0].set_title('Desvio')
axs[1, 1].plot(frecRel8, label="frecuencia relativa del numero 8 con respecto a n")
axs[1, 1].set_title('Axis [1, 1]')
axs[1, 1].plot(lineaFrecRel, label="valor promedio esperado")
axs[1, 1].set_title('Frecuencia relativa')
axs[0, 1].plot(varianza, label="varianza de los valores obtenidos")
axs[0, 1].set_title('Axis [1, 1]')
axs[0, 1].plot(lineaVar, label="varianza esperada")
axs[0, 1].set_title('Varianza')

for ax in axs.flat:
    ax.set(xlabel='n = numero de tiradas', ylabel='valor')

# Hide x labels and tick labels for top plots and y ticks for right plots.
for ax in axs.flat:
    ax.label_outer()