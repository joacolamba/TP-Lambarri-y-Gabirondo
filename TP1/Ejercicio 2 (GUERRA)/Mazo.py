from LISTAENLAZADA import ListaDobleEnlazada
from Cartas import Carta

class Mazo:
    def __init__(self):
        self.mazo = ListaDobleEnlazada() 
       
    def __str__(self):
        return str(self.mazo)
    
    def __repr__(self):
        return repr(self.mazo)
    
    def __iter__(self):
        return iter(self.mazo)
    def esta_vacia(self):
        return self.mazo.esta_vacia()
    
    
    def poner_arriba(self, carta): #este metodo agrega las cartas al mazo principal
        # self.mazo.agregar_al_frente(carta)
        self.mazo.agregar_al_inicio(carta)
        
        
    def sacar_arriba(self, nuevo_estado = "a"): #dar vuelta una carta
        carta = self.mazo.extraer(0)
        return carta
    
    def dar_vuelta(self):
        for i in self:
            i.carta.estado= "a" #pone todas las cartas boca abajo
    
    def __len__(self):
         return self.mazo.__len__()

     
    def poner_abajo(self, carta): #pone abajo del mazo las cartas ganadas
         carta.estado = "Boca Abajo"
         self.mazo.agregar_al_final(carta)
         self.cola = carta
