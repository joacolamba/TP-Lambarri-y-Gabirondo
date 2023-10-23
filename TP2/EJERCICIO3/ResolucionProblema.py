from Optimizacion import dijkstra_min, dijkstra_max
from Grafo import Grafo
from Fraccion import decimal_a_fraccion

with open("rutas.txt", "r") as rutas:
    ciudades = []
    datos_ciudades = []
    
    for ruta in rutas:
        ruta = ruta.rstrip()
        de, a, peso, costo = ruta.split(",")
        datos_ruta = [de, a, int(peso), int(costo)]
        datos_ciudades.append(datos_ruta)
        
        if de not in ciudades:
            ciudades.append(de)
        if a not in ciudades:
            ciudades.append(a)


print("Desde Ciudad de Buenos Aires, elija su destino: ")

print(ciudades[1:])
destino = input("Ingrese la ciudad a donde se quiera dirigir: ")

grafo_ciudades_peso = Grafo()
grafo_ciudades_costo = Grafo()

for i in range(len(datos_ciudades)):
    grafo_ciudades_peso.agregar_arista(datos_ciudades[i][0], datos_ciudades[i][1], datos_ciudades[i][2])
    grafo_ciudades_costo.agregar_arista(datos_ciudades[i][0], datos_ciudades[i][1], datos_ciudades[i][3])

dijkstra_max(grafo_ciudades_peso, grafo_ciudades_peso.obtener_vertice("CiudadBs.As."))
dijkstra_min(grafo_ciudades_costo, grafo_ciudades_costo.obtener_vertice("CiudadBs.As."))

peso_maximo = 0
for i in grafo_ciudades_peso:
    if i.id == destino:
        peso_maximo = i.dist
peso=decimal_a_fraccion(peso_maximo)

costo_minimo = 0
for i in grafo_ciudades_costo:
    if i.id == destino:
        costo_minimo = i.dist

nodo_peso = grafo_ciudades_peso.obtener_vertice(destino)
recorrido_peso = []
while nodo_peso is not None:
    recorrido_peso.append(nodo_peso.id)
    nodo_peso = nodo_peso.predecesor
recorrido_peso.reverse()

nodo_costo = grafo_ciudades_costo.obtener_vertice(destino)
recorrido_costo = []
while nodo_costo is not None:
    recorrido_costo.append(nodo_costo.id)
    nodo_costo = nodo_costo.predecesor
recorrido_costo.reverse()

print("Para llegar a", destino, ":")
print("El costo mínimo de transporte es: $", costo_minimo)
print("Y su ruta es:", recorrido_costo)
print("El peso máximo para transportar es:", peso, "kg")
print("Y su ruta es:", recorrido_peso)