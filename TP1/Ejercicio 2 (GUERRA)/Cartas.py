class Carta:
    valores_cartas = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7,'8': 8, '9': 9, '10': 10, 'J': 11, 'Q': 12,'K': 13, 'A': 14}

    def __init__(self, valor, palo, estado="Boca Abajo"):
        self.valor = valor
        self.palo = palo
        self.estado = estado
        
    def __str__(self):
        if self.estado == "Boca Abajo":
            return "-X"    #pregunta si la carta está boca abajo, no la muestra, caso contrario muestra el palo y el valor 
        else:
            return str(self.valor)+ str(self.palo)
        
    def __repr__(self):
        if self.estado == "Boca Abajo":
            return "-X"    #pregunta si la carta está boca abajo, no la muestra, caso contrario muestra el palo y el valor 
        else:
            return str(self.valor)+ str(self.palo)

    def __eq__(self, otro):
        return self.valores_cartas[self.valor] == self.valores_cartas[otro.valor]
         
    def __gt__(self, otro):
        if self.valores_cartas[self.valor] > self.valores_cartas[otro.valor]:
            return True
        else:
            return False
    
    def valor(self):
        return self.valor
    def palo(self):
        return self.palo
    def estado(self):
        return self.estado
