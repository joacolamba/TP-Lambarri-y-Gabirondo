#from LISTAENLAZADA import ListaDobleEnlazada
from Cartas import Carta
from Mazo import Mazo
import random as rd


class JuegoGuerra:

    def __init__(self, random_seed):
        self.mazo_mesa = Mazo()
        self.mazo_jugador_1 = Mazo()
        self.mazo_jugador_2 = Mazo()
        self.semilla = random_seed
        self.turnos_jugados = 0
        self.ganador = ""
        self.empate = "empate"       

    def armar_mazo(self):
        valores = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
        palos = ['♠', '♥', '♦', '♣']

        lista = []
        for valor in valores:
            for palo in palos:
                lista.append((Carta(valor, palo)))
        
        rd.seed(self.semilla)
        rd.shuffle(lista)

        for carta in lista:
            self.mazo_mesa.poner_arriba(carta)
        return self.mazo_mesa
    
    
    def repartir(self):
        for posicion, carta in enumerate(self.mazo_mesa):  
            
            if posicion%2 == 0:                          # si el resto de pos div 2 = 0:
                self.mazo_jugador_1.poner_arriba(carta)   # agregar al mazo 1
            else:                          # si el resto de pos div 2 ≠ 0:
                self.mazo_jugador_2.poner_arriba(carta)   # agrego al mazo 2
                
        return "Mazo repartido completamente.", "\n","Mazo 1: ",(self.mazo_jugador_1),"\n","Mazo 2:" ,  (self.mazo_jugador_2)

    def iniciar_juego(self):
        self.armar_mazo()
        self.repartir()
        print("-------------------------------------------------")
        cartas_mesa = []
        guerra = False
        while self.turnos_jugados < 10000:
            if guerra == False:
                try: 
                    carta_1 = self.mazo_jugador_1.sacar_arriba()
                    cartas_mesa.append(carta_1)
                    carta_2 = self.mazo_jugador_2.sacar_arriba() 
                    cartas_mesa.append(carta_2)
                    self.turnos_jugados += 1
                except IndexError:
                    if len(self.mazo_jugador_1) == 0:
                        self.ganador = "Jugador 2"
                        return self.ganador
                    elif len(self.mazo_jugador_2) == 0:
                        self.ganador = "Jugador 1"
                        return self.ganador
                print ("Turno número:", self.turnos_jugados)
                
                for carta in cartas_mesa:
                    carta.estado = "a"
                    print(carta)
                print("-------------------")
                print("\n")
                
                if cartas_mesa[-2] > cartas_mesa[-1]:
                    for i in cartas_mesa:
                        self.mazo_jugador_1.poner_abajo(i)
                    
                    cartas_mesa = []
                    print("Jugador 1:")
                    print(self.mazo_jugador_1)
                    print("\n", "Jugador2:", "\n")
                    print(self.mazo_jugador_2, "\n")
                    
                    if guerra == True:
                        guerra = False
                elif cartas_mesa [-1] > cartas_mesa [-2]:
                    for i in cartas_mesa:
                        self.mazo_jugador_2.poner_abajo(i)
                    
                    cartas_mesa = []
                    
                    print("Jugador 1:")
                    print(self.mazo_jugador_1)
                    print("\n", "Jugador2:", "\n")
                    print(self.mazo_jugador_2, "\n")
                    
                    if guerra == True:
                        guerra = False
                
                elif cartas_mesa[-1] == cartas_mesa [-2]:
                    if guerra == False:
                        guerra = True
                        try:
                            print("***GUERRA***")
                            for carta in range (0,3):
                                carta_3 = self.mazo_jugador_1.sacar_arriba("Boca Abajo") 
                                cartas_mesa.append(carta_3)
                                carta_4 = self.mazo_jugador_2.sacar_arriba("Boca Abajo")
                                cartas_mesa.append(carta_4)
                            carta_1 = self.mazo_jugador_1.sacar_arriba()
                            cartas_mesa.append(carta_1)
                            carta_2 = self.mazo_jugador_2.sacar_arriba()
                            cartas_mesa.append(carta_2)
                            
                        except IndexError:
                            print("Fin del juego")
                            if len(self.mazo_jugador_1) == 0:
                                self.ganador = "Jugador 2"
                                return self.ganador
                            elif len(self.mazo_jugador_2) == 0:
                                self.ganador = "Jugador 1"
                                return self.ganador
                    print("Cartas en juego")
                    for carta in cartas_mesa:
                        print(carta)
    
            else:
                if cartas_mesa [-2] > cartas_mesa [-1]:
                    for i in cartas_mesa:
                        self.mazo_jugador_1.poner_abajo(i)
                  
                    cartas_mesa = []
                   
                    print(self.mazo_jugador_1, "\n", "--------", "\n")
                    print(self.mazo_jugador_2, "\n")
                   
                    if guerra == True:
                        guerra = False
                  
                elif cartas_mesa [-1] > cartas_mesa [-2]:
                    for i in cartas_mesa:
                        self.mazo_jugador_2.poner_abajo(i)
                   
                    cartas_mesa = []
                   
                    print(self.mazo_jugador_1, "\n", "---------", "\n")
                    print(self.mazo_jugador_2, "\n")
                   
                    if guerra == True:
                        guerra = False
                       
                elif cartas_mesa [-1] == cartas_mesa [-2]:
                    if guerra == False:
                        guerra = True
                    try:
                        print("***GUERRA***")
                        for carta in range(0,3):
                            carta_3 = self.mazo_jugador_1.sacar_arriba("Boca") 
                            cartas_mesa.append(carta_3)
                            carta_4 = self.mazo_jugador_2.sacar_arriba("Boca")
                            cartas_mesa.append(carta_4)
                        carta_1 = self.mazo_jugador_1.sacar_arriba()
                        cartas_mesa.append(carta_1)
                        carta_2 = self.mazo_jugador_2.sacar_arriba()
                        cartas_mesa.append(carta_2)
                           
                    except IndexError:
                        if len(self.mazo_jugador_1) == 0:
                            self.ganador = "Jugador 2"
                            break
                       
                        else:
                            if len(self.mazo_jugador_2) == 0:
                                self.ganador = "Jugador 1"
                                break
                                
                    print("Cartas en juego")
                   
                    for carta in cartas_mesa:
                        print(carta)
                          

        if self.mazo_jugador_1 and self.mazo_jugador_2:
            return (self.empate)


if __name__ == "__main__":
    
    obj = JuegoGuerra(random_seed= 150)
    # obj.armar_mazo() 
    # obj.repartir()
    # print(obj.mazo_jugador_1)
    # print(len(obj.mazo_jugador_1))
    # print(obj.mazo_jugador_2)
    print()
    print()
    
    print(obj.iniciar_juego())
    print(obj.turnos_jugados)













# if __name__ == "__main__":
#     # import random as rd
#     cola1 = ColaDoble()
    
#     cola1.agregar_al_frente(1)
#     cola1.agregar_al_frente(3)
#     cola1.agregar_al_frente(4)
#     cola1.agregar_al_frente(5)
#     print(cola1)
#     print(cola1.extraer_al_inicio())
#     print(cola1)
#     cola1.agregar_al_final(100)
#     print(cola1)
    
#     valores = ['2','3','4','5','6','7','8','9','10','J','Q','K','A']
#     palos = ['♠', '♥', '♦', '♣']

    # carta1 = Carta("Q",'♥', "Boca Abajo")
    # carta2 = Carta("K",'♠', 'a')
    # print(carta2)
    # print(carta1)


    # print(carta1 == carta2)
    # lista = []
    # for valor in valores:
    #     for palo in palos:
    #         lista.append(str(Carta(valor, palo, "Boca")))
           
    # print(lista)
    # rd.seed(self._semilla)
    # rd.shuffle(lista)
    
    
    

