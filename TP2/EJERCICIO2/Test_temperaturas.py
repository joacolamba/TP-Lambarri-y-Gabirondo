import unittest 
from Temperaturas_DB import Temperaturas_DB


class TestTemperaturasDB(unittest.TestCase):
    def setUp(self):
        self.temp = Temperaturas_DB()
        self.cant_temp = 0
        self.lista_fecha = ["21/10/2023","22/10/2023","23/10/2023","24/10/2023"]
        self.temperatura = [24,27,14,10]
        self.fechamin = "21/10/2023"
        self.fechamax = "24/10/2023"
        self.fecha_temp = ("23/10/2023",14)

    

    def test_guardar_temperatura(self):
        for fecha,temp in zip (self.lista_fecha,self.temperatura):
            self.temp.guardar_temperatura(fecha, temp)   
            self.cant_temp +=1
        self.assertEqual(self.temp.tamano, self.cant_temp)



    def test_devolver_temperatura(self):
        self.temp.guardar_temperatura("21/10/2023",24)
        self.temp.guardar_temperatura("22/10/2023",27)
        self.temp.guardar_temperatura("23/10/2023",14)
        self.temp.guardar_temperatura("24/10/2023",10)
        dev = self.temp.devolver_temperatura("23/10/2023")
        self.assertEqual(self.fecha_temp[1],dev)
        

    def test_max_temp_rango(self):
        mayor = 27
        self.fechamin = "21/10/2023"
        self.fechamax = "24/10/2023"
        self.temp.guardar_temperatura("21/10/2023",24)
        self.temp.guardar_temperatura("22/10/2023",27)
        self.temp.guardar_temperatura("23/10/2023",14)
        self.temp.guardar_temperatura("24/10/2023",10)

        dev = self.temp.max_temp_rango(self.fechamin, self.fechamax)
        self.assertEqual(mayor, dev)
    
    

    def test_min_temp_rango(self):
        mini = 10
        self.fechamin = "21/10/2023"
        self.fechamax = "24/10/2023"
        self.temp.guardar_temperatura("21/10/2023",24)
        self.temp.guardar_temperatura("22/10/2023",27)
        self.temp.guardar_temperatura("23/10/2023",14)
        self.temp.guardar_temperatura("24/10/2023",10)
        
        dev = self.temp.min_temp_rango(self.fechamin, self.fechamax)
        self.assertEqual(mini, dev)


    def test_temp_extremos_rango(self):
        mini = 10
        mayor = 27
        self.fechamin = "21/10/2023"
        self.fechamax = "24/10/2023"
        self.temp.guardar_temperatura("21/10/2023",24)
        self.temp.guardar_temperatura("22/10/2023",27)
        self.temp.guardar_temperatura("23/10/2023",14)
        self.temp.guardar_temperatura("24/10/2023",10)
        dev = self.temp.temp_extremos_rango(self.fechamin, self.fechamax)
        self.assertEqual(dev, (mini, mayor))


    def test_borrar_temperatura(self):
        self.temp.guardar_temperatura("21/10/2023",24)
        self.temp.guardar_temperatura("22/10/2023",27)
        self.temp.guardar_temperatura("23/10/2023",14)
        self.temp.guardar_temperatura("24/10/2023",10)
        borrar = "23/10/2023"
        self.temp.borrar_temperatura(borrar)
        buscar = self.temp.devolver_temperatura("23/10/2023")
        self.assertFalse(buscar)
        

    def test_mostrar_temperaturas(self):
        self.fechamin = "21/10/2023"
        self.fechamax = "24/10/2023"
        self.lista_temp = [("2023-10-21",24),("2023-10-22",27),
                           ("2023-10-23",14),("2023-10-24",10)]
        self.temp.guardar_temperatura("21/10/2023",24)
        self.temp.guardar_temperatura("22/10/2023",27)
        self.temp.guardar_temperatura("23/10/2023",14)
        self.temp.guardar_temperatura("24/10/2023",10)
        dev = self.temp.mostrar_temperaturas(self.fechamin, self.fechamax)
        self.assertEqual(dev,self.lista_temp)


if __name__ == "__main__":
    unittest.main()