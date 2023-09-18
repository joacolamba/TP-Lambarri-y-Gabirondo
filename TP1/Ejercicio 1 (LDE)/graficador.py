from LISTAENLAZADA import ListaDobleEnlazada
import random
import time
import matplotlib.pyplot as plt



valores_n = range(100,1000,100)
tiempo = []

for n in valores_n:
    LDE=ListaDobleEnlazada()
    for i in range(n):
        LDE.agregar(random.randint(-100,100))
    tic = time.perf_counter()
    LDE.ordenar()
    toc = time.perf_counter()
    tiempo.append(toc-tic) 
    


plt.clf()
plt.plot(valores_n, tiempo, label="Ordenamiento por burbuja")

#plt.yscale('log')
plt.xlabel("Tamaño de la lista")
plt.ylabel("Tiempo del algoritmo")
plt.title("Tiempo en fn. del nro de elementos")
plt.legend()