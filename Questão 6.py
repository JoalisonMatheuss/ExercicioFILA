class queue:
    def __init__(self):
        self.itens = []

    def enqueue(self):
      elemento = int(input("Adicionar Avi�o: "))
      self.itens.append(elemento)

    def dequeue(self):
        if (not(self.isEmpty())):
          self.itens.pop(0)

    def lenght(self):
      #Letra A 
      return print("N�mero de avi�es aguardando na fila de decolagem: %d \n"%(len(self.itens)))
    
    
    def isEmpty(self):
      return len(self.itens) == 0

fila = queue()
fila.enqueue()
print("========================= LETRA E =========================")
print(fila.itens," --> o 1- Blackbird � o avi�o mais r�pido do mundo")
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
print("Avi�es na fila de espera: \n",fila.itens,"\n" )
fila.enqueue()
#Letra D
print("========================= LETRA D =========================")
print("Avi�es na fila de espera:",fila.itens)
