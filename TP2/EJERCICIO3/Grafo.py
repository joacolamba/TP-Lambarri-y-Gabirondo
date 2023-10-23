from Vertice import Vertice
    
class Grafo:
  
    def __init__(self):
        self.lista_vertices = {}
        self.num_vertices = 0
   
    def __getitem__(self,clave):
        return self.obtener_vertice(clave)
    
    def agregar_vertice(self,clave):
        self.num_vertices = self.num_vertices + 1
        nuevo_vertice = Vertice(clave)
        self.lista_vertices[clave] = nuevo_vertice
        return nuevo_vertice

    def obtener_vertice(self,n):
        if n in self.lista_vertices:
            return self.lista_vertices[n]
        else:
            return None

    def __contains__(self,n):
        return n in self.lista_vertices

    def agregar_arista(self,de,a,ponderacion):
        if de not in self.lista_vertices:
            self.agregar_vertice(de)
        if a not in self.lista_vertices:
            self.agregar_vertice(a)
        self.lista_vertices[de].agregar_vecino(self.lista_vertices[a],ponderacion)

    def obtener_vertices(self):
        return self.lista_vertices.keys()

    def __iter__(self):
        return iter(self.lista_vertices.values())



# if __name__ == "__main__":
#     Grafo1= Grafo()
#     Grafo1.agregar_vertice("s")
#     Grafo1.agregar_vertice("a")
#     Grafo1.agregar_vertice("b")
#     Grafo1.agregar_vertice("c")
#     Grafo1.agregar_arista("s","a", 10)
#     Grafo1.agregar_arista("a","b", 20)
#     Grafo1.agregar_arista("b","c", 30)
#     Grafo1.agregar_arista("c","s", 40)
#     print(Grafo1)