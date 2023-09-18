class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None
        self.anterior = None
    
    
    def __str__(self):
        return str(self.dato)
    
    def __eq__(self, otro):
      return self._dato == otro._dato
  
    def __lt__(self,otro):
        return self._dato < otro._dato
        
    def __gt__(self,otro):
        return self._dato > otro._dato

class ListaDobleEnlazada:
    
    def __init__(self):
        self.cabeza = None
        self.cola = None
        self.tamanio = 0
    
    def __len__(self):
        return self.tamanio
    
    def esta_vacia(self):
        return self.tamanio == 0
    
    def tamanio(self):
        return self.tamanio

    def agregar_al_inicio(self, item):
        nuevo_nodo = Nodo(item)

        if self.esta_vacia():
            self.cabeza = nuevo_nodo
            self.cola = nuevo_nodo
        else:
            nuevo_nodo.siguiente = self.cabeza
            self.cabeza.anterior = nuevo_nodo
            self.cabeza = nuevo_nodo
            if self.cabeza.anterior is not None:
                self.cabeza.anterior = None
        self.tamanio += 1

    def agregar_al_final(self, item):
        nuevo_nodo = Nodo(item)

        if self.esta_vacia():
            self.cabeza = nuevo_nodo
            self.cola = nuevo_nodo
        else:
            self.cola.siguiente = nuevo_nodo
            nuevo_nodo.anterior = self.cola
            self.cola = nuevo_nodo
            if self.cabeza.anterior is not None:
                self.cabeza.anterior = None
        self.tamanio += 1

    def insertar(self, item, posicion=None):
        nuevo_nodo = Nodo(item)
    
        if self.esta_vacia():
            self.cabeza = nuevo_nodo
            self.cola = nuevo_nodo
        elif posicion is None or posicion >= self.tamanio:
            self.cola.siguiente = nuevo_nodo
            nuevo_nodo.anterior = self.cola
            self.cola = nuevo_nodo
        elif posicion == 0:
            nuevo_nodo.siguiente = self.cabeza
            self.cabeza.anterior = nuevo_nodo
            self.cabeza = nuevo_nodo
        else:
            nodo_actual = self.cabeza
            for _ in range(posicion - 1):
                nodo_actual = nodo_actual.siguiente
    
            nuevo_nodo.siguiente = nodo_actual.siguiente
            nuevo_nodo.anterior = nodo_actual
            nodo_actual.siguiente.anterior = nuevo_nodo
            nodo_actual.siguiente = nuevo_nodo
    
        
        self.tamanio += 1


    def extraer(self, posicion=None):
        if posicion is not None and (posicion < -1 or posicion >= self.tamanio):
            raise IndexError("Índice fuera de rango")
    
        if self.esta_vacia():
            return None
    
        if posicion is None or posicion == self.tamanio - 1:
            nodo_eliminar = self.cola
    
            if self.tamanio == 1:
                self.cabeza = None
                self.cola = None
            else:
                self.cola.anterior.siguiente = None
                self.cola = self.cola.anterior
        elif posicion == 0:
            nodo_eliminar = self.cabeza
    
            if self.tamanio == 1:
                self.cabeza = None
                self.cola = None
            else:
                self.cabeza.siguiente.anterior = None
                self.cabeza = self.cabeza.siguiente
        elif posicion == -1:
            nodo_eliminar = self.cola
    
            if self.tamanio == 1:
                self.cabeza = None
                self.cola = None
            else:
                self.cola.anterior.siguiente = None
                self.cola = self.cola.anterior
        else:
            nodo_actual = self.cabeza
            for _ in range(posicion):
                nodo_actual = nodo_actual.siguiente
    
            nodo_eliminar = nodo_actual
            nodo_actual.anterior.siguiente = nodo_actual.siguiente
            nodo_actual.siguiente.anterior = nodo_actual.anterior
    
        self.tamanio -= 1
        return nodo_eliminar.dato


    def copiar(self):
        copia_lista = ListaDobleEnlazada()
        nodo_actual = self.cabeza
        while nodo_actual is not None:
            copia_lista.agregar_al_final(nodo_actual.dato)
            nodo_actual = nodo_actual.siguiente
        return copia_lista

    def invertir(self):
        
        nodo_actual = self.cabeza
        while nodo_actual is not None:
            siguiente_nodo = nodo_actual.siguiente
            nodo_actual.siguiente = nodo_actual.anterior
            nodo_actual.anterior = siguiente_nodo
            nodo_actual = siguiente_nodo
        
        self.cabeza, self.cola = self.cola, self.cabeza
        return self


    def ordenar(self):
        """
        Ordena los elementos de la lista de menor a mayor.
        """
        if self.tamanio <= 1:
            return self
    
        nodo_actual = self.cabeza
        while nodo_actual is not None:
            nodo_siguiente = nodo_actual.siguiente
            while nodo_siguiente is not None:
                if nodo_actual.dato > nodo_siguiente.dato:
                    nodo_actual.dato, nodo_siguiente.dato = nodo_siguiente.dato, nodo_actual.dato  # noqa: E501
                nodo_siguiente = nodo_siguiente.siguiente
            nodo_actual = nodo_actual.siguiente
    
        return self


    def concatenar(self, lista):
        temp = lista.cabeza

        for i in range(lista.tamanio):
            self.agregar_al_final(temp.dato)
            temp = temp.siguiente 
        return self


    def __add__(self,lista):
        lista_retorno = self.copiar()
        return lista_retorno.concatenar(lista)
    

    def __iter__(self):
        nodo_actual = self.cabeza
        while nodo_actual is not None:
            yield nodo_actual.dato
            nodo_actual = nodo_actual.siguiente
            
    def __str__(self):
        return str([nodo for nodo in self])
    
    
    




if __name__ == "__main__":
    lista1 = ListaDobleEnlazada()
    
    lista1.agregar_al_inicio(1)
    lista1.agregar_al_inicio(5)
    lista1.agregar_al_inicio(15)
    lista1.agregar_al_final(-5)
    lista1.agregar_al_final(-10)
    lista1.insertar(2,7)
    print(lista1)
    
    lista2 = ListaDobleEnlazada()
    lista2.agregar_al_inicio(67)
    lista2.agregar_al_inicio(7)
    lista2.agregar_al_inicio(55)
    lista2.agregar_al_final(-99)
    lista2.agregar_al_final(-1)
    print(lista2)
    
    # lista3 =lista2.ordenar()
    # print(lista3)
    
    
    lista3= lista1.concatenar(lista2)
    print(lista3)
    
    print(lista1+lista2)
    # posicion = 2

    # if posicion < 0 or posicion >= lista3.tamanio:
    #     print("La posición está fuera de rango.")
    # else:
    #     nodo_actual = lista3.cola
    #     # for _ in range(posicion):
    #     #     nodo_actual = nodo_actual.siguiente
        
    #     # valor = nodo_actual.siguiente.dato
    #     # print("Valor en la posición", posicion, ":", valor)



    #     while nodo_actual is not None:
    #         siguiente_nodo = nodo_actual.anterior
    #         print(siguiente_nodo)
    #         nodo_actual = siguiente_nodo
    #print(nodo_actual)
    # print(lista3.invertir())
    
    # lista_copia = lista1.copiar()
    
    # print(lista_copia)
    # print(lista1.invertir())
    