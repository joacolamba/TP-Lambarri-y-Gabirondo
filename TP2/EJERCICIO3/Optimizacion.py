from ColasPrioridad import MonticuloBinarioMin
from Grafo import Grafo


def dijkstra_max(un_grafo, inicio):
    cp = MonticuloBinarioMin()
    
    for vertice in un_grafo:
        vertice.asignar_distancia(float('inf'))
    inicio.asignar_distancia(0)
    cp.construir_monticulo([(v.dist, v) for v in un_grafo])
    
    while not cp.esta_vacia():
        vertice_actual = cp.eliminar_min()

        for vertice_siguiente in vertice_actual.obtener_conexiones():
            # Aquí modificamos la ponderación para que sea 1/distancia
            nueva_distancia = max(vertice_actual.dist, 1/vertice_actual.obtener_ponderacion(vertice_siguiente))
            
            if nueva_distancia < vertice_siguiente.dist:    
                vertice_siguiente.asignar_distancia(nueva_distancia)
                vertice_siguiente.asignar_predecesor(vertice_actual)
                cp.decrementar_distancia(vertice_siguiente, nueva_distancia)



def dijkstra_min(un_grafo, inicio):
    cp = MonticuloBinarioMin()         
    
    for vertice in un_grafo:
        vertice.asignar_distancia(float('inf'))
    inicio.asignar_distancia(0)
    cp.construir_monticulo([(v.dist, v) for v in un_grafo])
    
    while not cp.esta_vacia():
        vertice_actual = cp.eliminar_min()
        
        for vertice_siguiente in vertice_actual.obtener_conexiones():
            nueva_distancia = vertice_actual.dist + vertice_actual.obtener_ponderacion(vertice_siguiente)
            
            if nueva_distancia < vertice_siguiente.dist:    
                vertice_siguiente.asignar_distancia(nueva_distancia)
                vertice_siguiente.asignar_predecesor(vertice_actual)
                cp.decrementar_distancia(vertice_siguiente, nueva_distancia)

def costo_minimo(un_grafo, ruta):
    costo_minimo = 0
    for i in range(len(ruta) - 1):
        vertice_actual = un_grafo.obtener_vertice(ruta[i])
        vertice_siguiente = un_grafo.obtener_vertice(ruta[i + 1])
        costo_minimo += vertice_actual.obtener_ponderacion(vertice_siguiente)
    return costo_minimo



