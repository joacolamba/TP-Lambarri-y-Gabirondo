import math
    
def Ordenamiento(archivo, bloque_inicial):
    with open('datos.txt', 'r+') as archivo: #Abrimos el archivo en modo lectura para conocer la longitud del mismo
        tl = sum(1 for line in archivo) #Suma de a 1 todas las lineas del archivo
        archivo.seek(0) # Posicionamos el puntero al comiezo del archivo  
        if bloque_inicial<1:
            raise Exception("El tamaño bloque inicial debe ser un número entero mayor a 0")
        bloque = bloque_inicial # creamos esta variable para no modificar el valor brindado por el usuario
        while bloque<tl:   
            Particion(archivo,bloque)
            Fusion(archivo,bloque)
            bloque = 2*bloque

                       
            
def Particion(archivo,bloque):
    with open('datos.txt', 'r+') as archivo: #Abrimos el archivo en modo lectura para conocer la longitud del mismo
        tl = sum(1 for line in archivo) #Suma de a 1 todas las lineas del archivo
     #Creamos dos archivos auxiliares
    with open('datos.txt', 'r') as archivo,open('ArchiA.txt', 'w') as archiA, open('ArchiB.txt', 'w') as archiB :           
        m = 0
        while m <= tl:
            k = 0
            l = 0
            while k < bloque:  #Leemos los datos restantes del archivo y los copiamos en el archivo auxiliar A
                R = archivo.readline()
                archiA.write(R)
                k +=1
                m +=1            
            while l < bloque:   #Leemos los datos restantes del archivo y los copiamos en el archivo auxiliar B
                R = archivo.readline()
                archiB.write(R)
                l +=1
                m +=1       
        
            
def Fusion(archivo,bloque):
        with open('archiA.txt', 'r+') as archiA, open('archiB.txt', 'r+') as archiB: #Abrimos el archivo en modo lectura para conocer la longitud del mismo
            tl1 = sum(1 for line in archiA)
            tl2 = sum(1 for line in archiB)
        with open('datos.txt', 'w') as archivo,open('ArchiA.txt', 'r') as archiA,open('ArchiB.txt', 'r') as archiB :                     
            r1 = archiA.readline()        
            r2 = archiB.readline()              
            m = 2
            while m <= tl1+tl2:
                k=0
                l=0
                while k < bloque and l < bloque:                    
                    if r1 <= r2:
                       archivo.write(r1)                     
                       k+=1                      
                       r1 = archiA.readline()  
                       m +=1                      
                    else:
                        archivo.write(r2)
                        l+=1                       
                        r2 = archiB.readline() 
                        m +=1                  
                while k < bloque:
                    archivo.write(r1)
                    k +=1                   
                    r1 = archiA.readline()
                    m +=1
                while l < bloque:
                    archivo.write(r2)                    
                    l +=1                   
                    r2 = archiB.readline()
                    m +=1
                                
            
if __name__=='__main__':

    Ordenamiento('datos.txt',1)