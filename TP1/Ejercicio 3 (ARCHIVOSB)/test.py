
import os 
import unittest

from generador_de_datos_10MB import crear_archivo_de_datos
from Mezcla_Directa import Ordenamiento

class test_Mezcla_Directa(unittest.TestCase):
    
    def setUp(self):
        crear_archivo_de_datos("datos.txt")
        self.bytes_iniciales = os.stat('datos.txt').st_size
      
    def verificar_ordenado(self):
        verificar_ordenado = True
        archivo = open("datos.txt", "r")
        linea_anterior = archivo.readline()
        archivo.seek(0)
        for linea_siguiente in archivo:
            if linea_siguiente < linea_anterior:
                verificar_ordenado = False
                break
            linea_anterior = linea_siguiente
        return verificar_ordenado


    
    def test_tamanio(self):
        self.assertEqual(self.bytes_iniciales, os.path.getsize('datos.txt'))
        #verifico si ambos bytes son iguales 
        
        
    def test_ordenado(self):
        Ordenamiento("datos.txt",1)
        self.assertEqual(self.verificar_ordenado(), True)
        
        
if __name__ == "__main__":
    unittest.main()