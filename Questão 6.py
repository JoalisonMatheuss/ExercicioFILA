class queue:
    def __init__(self):
        self.itens = []

    def enqueue(self):
      elemento = int(input("Adicionar Avião: "))
      self.itens.append(elemento)

    def dequeue(self):
        if (not(self.isEmpty())):
          self.itens.pop(0)

    def lenght(self):
      #Letra A 
      return print("Número de aviões aguardando na fila de decolagem: %d \n"%(len(self.itens)))
    
    
    def isEmpty(self):
      return len(self.itens) == 0

fila = queue()
fila.enqueue()
print("========================= LETRA E =========================")
print(fila.itens," --> o 1- Blackbird é o avião mais rápido do mundo")
#Letra E
fila.enqueue()
fila.enqueue()
print("========================= LETRA A =========================")

fila.lenght()
#Letra E
print("========================= LETRA B =========================")
print("Decolagem autorizada! \n")
print("========================= LETRA C =========================")
fila.dequeue()

#Letra c 
print("Aviões na fila de espera: \n",fila.itens,"\n" )
fila.enqueue()
#Letra D
print("========================= LETRA D =========================")
print("Aviões na fila de espera:",fila.itens)
