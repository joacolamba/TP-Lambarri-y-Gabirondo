class Vertice:
   
    def __init__(self,clave,dist=0):
        self.id = clave
        self.conectado_a = {}
        self.dist = dist
        self.predecesor = None
        
    def asignar_distancia(self,valor):
        self.dist = valor
        
    def obtener_distancia(self):
        return self.dist
    
    def agregar_vecino(self,vecino,ponderacion):      
        self.conectado_a[vecino] = ponderacion

    def __str__(self):
        return str(self.id) + ' conectado_a: ' + str([x.id for x in self.conectado_a]) + str([self.obtener_ponderacion(v) for v in self.conectado_a])

    def obtener_conexiones(self):
        return self.conectado_a.keys()
        #devuelve una lista con todas las claves que estén conectadas al vértice

    def obtener_id(self):
        return self.id

    def obtener_ponderacion(self,vecino):
        return self.conectado_a[vecino]
    
    def asignar_predecesor(self, predecesor):
        self.predecesor = predecesor
        
    def __lt__(self, otro):
        return True
