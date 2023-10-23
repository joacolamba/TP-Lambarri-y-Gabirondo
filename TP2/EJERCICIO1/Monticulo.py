class MonticuloBinario:
    
    def __init__(self):
        self.listaMonticulo = [0]
        self.tamanoActual = 0
    
    def infiltArriba(self,item):
        while item//2 >0:
            if self.listaMonticulo[item] < self.listaMonticulo[item // 2]:
                tmp = self.listaMonticulo[item // 2]
                self.listaMonticulo[item // 2] = self.listaMonticulo[item]
                self.listaMonticulo[item] = tmp
            item = item // 2
            
    def insertar(self, k):
        self.listaMonticulo.append(k)
        self.tamanoActual = self.tamanoActual + 1
        self.infiltArriba(self.tamanoActual)
    
    def infiltAbajo(self, item):

        while(item*2) <= self.tamanoActual:
            hm = self.hijoMin(item)
            if self.listaMonticulo[item] > self.listaMonticulo[hm]:
                tmp = self.listaMonticulo[item]
                self.listaMonticulo[item] = self.listaMonticulo [hm]
                self.listaMonticulo[hm] = tmp
            item = hm

    def hijoMin(self, item):
        if item*2 + 1 > self.tamanoActual:
            return item*2
        else:
            if self.listaMonticulo[item*2] < self.listaMonticulo[item*2 + 1]:
                return item*2
            else:
                return item*2 + 1

    def eliminarMin(self):
 
        valorExtraido = self.listaMonticulo[1] #Raiz
        self.listaMonticulo[1] = self.listaMonticulo[self.tamanoActual] #se lleva el ultimo elemento insertado temp a la raiz
        self.tamanoActual = self.tamanoActual -1
        self.listaMonticulo.pop()
        self.infiltAbajo(1)
        return valorExtraido
    

    def __iter__(self):
        for i in self.listaMonticulo:
            yield i
    
    def __str__(self):
        return str(self.listaMonticulo)
    
    def __len__(self):
        return self.tamanoActual
        
      