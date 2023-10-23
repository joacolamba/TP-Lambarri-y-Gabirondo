from Arbol import ArbolAVL , Iterador
from datetime import datetime 


class Temperaturas_DB:
    
    def __init__(self):
        self.mediciones = ArbolAVL()
        self.tamano = 0
        
    def __str__(self):
        lista=[]
        for nodo in self.mediciones:
            lista.append([str(nodo.clave.date()), nodo.valor]) #date() retorna solo el formato fecha, no el formato hora
        return str(lista)

    def __iter__(self):
        return str(self.mediciones)

    def guardar_temperatura(self,fecha,temperatura):
        convertir_fecha = datetime.strptime(fecha,"%d/%m/%Y")
        self.mediciones.agregar(convertir_fecha,temperatura)
        self.tamano += 1
        
    def devolver_temperatura(self,fecha):
        convertir_fecha = datetime.strptime(fecha,"%d/%m/%Y")
        temp = self.mediciones.obtener(convertir_fecha)
        return temp
    
    def max_temp_rango(self,fecha1, fecha2):
        f_uno = datetime.strptime(fecha1, "%d/%m/%Y")
        f_dos = datetime.strptime(fecha2, "%d/%m/%Y")
        temp_max = self.mediciones.obtener(f_uno)  #O(log n)
        
        iterador = Iterador(self.mediciones,f_uno)
        for i in iterador:
            if i.clave <= f_dos and i.clave >= f_uno:
                if i.valor > temp_max:
                    temp_max = i.valor
            else:
                break
        return temp_max
    
    def min_temp_rango(self,fecha1, fecha2):
        f_uno = datetime.strptime(fecha1, "%d/%m/%Y")
        f_dos = datetime.strptime(fecha2, "%d/%m/%Y")
        temp_min = self.mediciones.obtener(f_uno)
        iterador = Iterador(self.mediciones,f_uno)
        for i in iterador:
            if i.clave <= f_dos:
                if i.valor < temp_min:
                    temp_min = i.valor 
            else:
                break
        return temp_min

    def temp_extremos_rango(self,fecha1,fecha2):
        min_ = self.min_temp_rango(fecha1, fecha2)
        max_ = self.max_temp_rango(fecha1, fecha2)
        return min_,max_
    
    def borrar_temperatura(self,fecha):
        fecha_conv = datetime.strptime(fecha, "%d/%m/%Y")
        self.mediciones.eliminar(fecha_conv) 
        self.tamano -= 1
    
    def mostrar_temperaturas(self,fecha1,fecha2):
        f_uno = datetime.strptime(fecha1, "%d/%m/%Y") 
        f_dos = datetime.strptime(fecha2, "%d/%m/%Y") 
        iterador = Iterador(self.mediciones,f_uno) 
        lista=[]
        for i in iterador:
            if i.clave <= f_dos:
                    lista.append((str(i.clave.date()),i.valor))
            else:
                break
        return(lista) 

    def mostrar_cantidad_muestras(self):
        return self.tamano
    

