class NodoArbol:
    
    def __init__(self,clave,carga_util,izquierdo=None,derecho=None,padre=None):

        self.clave = clave
        self.carga_util = carga_util
        self.izq = izquierdo
        self.der = derecho
        self.padre = padre
        self.factorEquilibrio = 0
        
    def __str__(self):
        return f"NodoArbol(clave={self.clave}, carga_util={self.carga_util})"

    def __repr__(self):
        return f"NodoArbol(clave={self.clave}, carga_util={self.carga_util}, izquierdo={self.izq}, derecho={self.der})"
    
    def __iter__(self):
        if self:
            if self.tieneHijoIzquierdo():
                    for elem in self.hijoIzquierdo:
                        yield elem
            yield self.clave
            if self.tieneHijoDerecho():
                    for elem in self.hijoDerecho:
                        yield elem


    def reemplazar_dato_de_nodo(self,clave,carga_util,hizq,hder):
        self.clave = clave
        self.carga_util = carga_util
        self.izq = hizq
        self.der = hder
        if self.tiene_izq():                        
            self.izq.padre = self
        if self.tiene_der():
                self.der.padre = self
           
    def encontrarMin(self):
      actual = self
      while actual.tiene_hijo_izquierdo():
          actual = actual.izq
      return actual 
           
    def encontrarSucesor(self):
      suc = None
      if self.tiene_hijo_derecho():
          suc = self.der.encontrarMin()
      else:
          if self.padre:
                 if self.eshijo_izquierdo():
                     suc = self.padre
                 else:
                     self.padre.der = None
                     suc = self.padre.encontrarSucesor()
                     self.padre.der = self
      return suc
  
    def empalmar(self):
       if self.esHoja():
           if self.eshijo_izquierdo():
                  self.padre.izq = None
           else:
                  self.padre.der = None
       elif self.tieneAlgunHijo():
           if self.tiene_hijo_izquierdo():
                  if self.eshijo_izquierdo():
                     self.padre.izq = self.izq 
                  else:
                     self.padre.der = self.izq
                  self.izq.padre = self.padre
           else:
                  if self.eshijo_izquierdo():
                     self.padre.izq = self.der
                  else:
                     self.padre.der = self.der
                  self.der.padre = self.padre
    
    def tiene_hijo_izquierdo(self):
       return self.izq

    def tiene_hijo_derecho(self):
       return self.der

    def eshijo_izquierdo(self):
       return self.padre and self.padre.izq == self

    def eshijo_derecho(self):
       return self.padre and self.padre.der == self

    def es_raiz(self):
       return not self.padre

    def esHoja(self):
       return not (self.der or self.izq)

    def tieneAlgunHijo(self):
       return self.der or self.izq

    def tieneAmminimomosHijos(self):
       return self.der and self.izq 
               
class ArbolAVL:

    def __init__(self):
        self.raiz = None
        self.tamano = 0

    def mostrar_arbol(self):
        self._mostrar_arbol(self.raiz)

    def _mostrar_arbol(self, nodo_actual, nivel=0, prefijo="Raíz: "):
        if nodo_actual is not None:
            self._mostrar_arbol(nodo_actual.izq, nivel + 1, "Izq: ")
            print(" " * nivel * 4 + f"{prefijo}{nodo_actual.clave} ({nodo_actual.carga_util})")
            self._mostrar_arbol(nodo_actual.der, nivel + 1, "Der: ")
    
    def longitud(self):
        return self.tamano

    def __len__(self):
        return self.tamano
    
    def __iter__(self):
        return self.raiz.__iter__()


    def iterador(self):
        return self.__next__()

    
    def agregar(self,clave,carga_util):
        if self.raiz:
            self._agregar(clave,carga_util,self.raiz)
        else:
            self.raiz = NodoArbol(clave,carga_util) #crea una raíz si no la hay
        self.tamano = self.tamano + 1

    def _agregar(self,clave,carga_util,nodoActual):
        if clave < nodoActual.clave:
            if nodoActual.tiene_hijo_izquierdo():
                   self._agregar(clave,carga_util,nodoActual.izq) #subarbol izquierdo de la raiz
            else:
                   nodoActual.izq = NodoArbol(clave,carga_util,padre=nodoActual)
                   self.actualizarEquilibrio(nodoActual.izq)
        else:       
            if nodoActual.tiene_hijo_derecho():
                   self._agregar(clave,carga_util,nodoActual.der)
            else:
                   nodoActual.der = NodoArbol(clave,carga_util,padre=nodoActual)
                   self.actualizarEquilibrio(nodoActual.der)

    
    def __setitem__(self,c,v):
       self.agregar(c,v)

    def obtener(self,clave): #retorna la temperatura de un día en particular
       if self.raiz:
           res = self._obtener(clave,self.raiz)
           if res:
                  return res.carga_util
           else:
                  return None
       else:
           return None

    def _obtener(self,clave,nodoActual):
       if not nodoActual:
           return None
       elif nodoActual.clave == clave:
           return nodoActual
       elif clave < nodoActual.clave:
           return self._obtener(clave,nodoActual.izq)
       else:
           return self._obtener(clave,nodoActual.der)

    def __getitem__(self,clave):
       return self.obtener(clave)

    def __contains__(self,clave):
       if self._obtener(clave,self.raiz):
           return True
       else:
           return False

    def __delitem__(self,clave):
       self.eliminar(clave)


    def remover(self,nodoActual):
         if nodoActual.esHoja(): #suponiendo que es hoja
           if nodoActual == nodoActual.padre.izq: #hijo izq del padre
               nodoActual.padre.izq = None
           else:
               nodoActual.padre.der = None
         elif nodoActual.tieneAlgunHijo(): #interior
           suc = nodoActual.encontrarSucesor() #busca el sucesor del nodo a eliminar
           suc.empalmar()
           nodoActual.clave = suc.clave
           nodoActual.carga_util = suc.carga_util

         else: # este nodo tiene un (1) hijo
           if nodoActual.tiene_hijo_izquierdo():
             if nodoActual.eshijo_izquierdo():
                 nodoActual.izq.padre = nodoActual.padre
                 nodoActual.padre.izq = nodoActual.izq
             elif nodoActual.eshijo_derecho():
                 nodoActual.izq.padre = nodoActual.padre
                 nodoActual.padre.der = nodoActual.izq
             else:
                 nodoActual.reemplazar_dato_de_nodo(nodoActual.izq.clave,
                                    nodoActual.izq.carga_util,
                                    nodoActual.izq.izq,
                                    nodoActual.izq.der)
           else:
             if nodoActual.eshijo_izquierdo():
                 nodoActual.der.padre = nodoActual.padre
                 nodoActual.padre.izq = nodoActual.der
             elif nodoActual.eshijo_derecho():
                 nodoActual.der.padre = nodoActual.padre
                 nodoActual.padre.der = nodoActual.der
             else:
                 nodoActual.reemplazar_dato_de_nodo(nodoActual.der.clave,
                                    nodoActual.der.carga_util,
                                    nodoActual.der.izq,
                                    nodoActual.der.der)
                 
    def eliminar(self,clave):
      if self.tamano > 1:
         nodoAEliminar = self._obtener(clave,self.raiz)
         if nodoAEliminar:
             self.remover(nodoAEliminar)
             self.tamano = self.tamano-1
         else:
             raise KeyError('Error, la clave no está en el árbol')
      elif self.tamano == 1 and self.raiz.clave == clave:
         self.raiz = None
         self.tamano = self.tamano - 1
      else:
         raise KeyError('Error, la clave no está en el árbol')


    def rotar_derecha(self,rot_raiz):
        nueva_raiz = rot_raiz.izq
        rot_raiz.izq = nueva_raiz.der
        if rot_raiz.padre is None:
            self.raiz = nueva_raiz 
        else:
            if rot_raiz.eshijo_izquierdo():
                rot_raiz.padre.izq = nueva_raiz
            elif rot_raiz.es_der():
                rot_raiz.padre.der = nueva_raiz 
        nueva_raiz.der = rot_raiz 
        rot_raiz.padre = nueva_raiz
        
        rot_raiz.factorEquilibrio = rot_raiz.factorEquilibrio - 1 - max (0,nueva_raiz.factorEquilibrio)
        nueva_raiz.factorEquilibrio = nueva_raiz.factorEquilibrio - 1 + min (0,rot_raiz.factorEquilibrio)


    def rotar_izquierda(self,rot_raiz):
        nuevaRaiz = rot_raiz.der
        rot_raiz.der = nuevaRaiz.izq
        if nuevaRaiz.izq != None:
            nuevaRaiz.izq.padre = rot_raiz
        nuevaRaiz.padre = rot_raiz.padre
        if rot_raiz.es_raiz():
            self.raiz = nuevaRaiz
        else:
            if rot_raiz.eshijo_izquierdo():
                    rot_raiz.padre.izq = nuevaRaiz
            else:
                rot_raiz.padre.der = nuevaRaiz
        nuevaRaiz.izq = rot_raiz
        rot_raiz.padre = nuevaRaiz
        rot_raiz.factorEquilibrio = rot_raiz.factorEquilibrio + 1 - min(nuevaRaiz.factorEquilibrio, 0)
        nuevaRaiz.factorEquilibrio = nuevaRaiz.factorEquilibrio + 1 + max(rot_raiz.factorEquilibrio, 0)


    def reequilibrar(self,nodo):
      if nodo.factorEquilibrio < 0:
              if nodo.der.factorEquilibrio > 0:
                self.rotar_derecha(nodo.der)
                self.rotar_izquierda(nodo)
              else:
                self.rotar_izquierda(nodo)
      elif nodo.factorEquilibrio > 0:
              if nodo.izq.factorEquilibrio < 0:
                self.rotar_izquierda(nodo.izq)
                self.rotar_derecha(nodo)
              else:
                self.rotar_derecha(nodo)
                
    
    def actualizarEquilibrio(self,nodo):
        if nodo.factorEquilibrio > 1 or nodo.factorEquilibrio < -1:
            self.reequilibrar(nodo)
            return
        if nodo.padre != None:
            if nodo.eshijo_izquierdo():
                    nodo.padre.factorEquilibrio += 1
            elif nodo.eshijo_derecho():
                    nodo.padre.factorEquilibrio -= 1
    
            if nodo.padre.factorEquilibrio != 0:
                    self.actualizarEquilibrio(nodo.padre)
                    


class Iterador:
    def __init__(self, arbol, clave_inicio): 
        self.arbol = arbol 
        self.nodo_inicio = arbol._obtener(clave_inicio, self.arbol.raiz) #dentro del árbol se busca la clave
            
    def __next__(self):
        nodo_salida = self.nodo_inicio #se guarda el nodo desde donde va a iterar
        if self.nodo_inicio == None: #si el nodo no tiene ningun carga_util
            raise StopIteration
        self.nodo_inicio = self.nodo_inicio.encontrarSucesor() # actualiza carga_util del nodo. 
                                                               #recorre desde un inicio hasta el final del arbol
        return nodo_salida

    def __iter__(self):
        return self
    



if __name__ == "__main__":
    arbol = ArbolAVL()
    nodo = NodoArbol(9, 3, 4)
    arbol.agregar(10,3)
    arbol.agregar(9,6)
    arbol.agregar(8,6)
    arbol.agregar(1,3)
    # arbol.agregar(33,4)
    # arbol.agregar(5,55)
    # arbol.agregar(6,6)
    arbol.mostrar_arbol()
    print(repr(nodo))

    
    