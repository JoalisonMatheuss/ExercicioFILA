#Questão 3

class queue:
    def __init__(self):
        self.itens = []
        self.valorMaximo = 0

    def enqueue(self):
        
        for i in range( 21 ) :
          nome = input("Qual o nome do paciente? ")
          print("Paciente tem o código %d"%(i))
          print("==============================")
          if len(self.itens) == 20:
            print("A FILA ATINGIU O VALOR MAXIMO!!!!!")
            print("\n")
            self.valorMaximo = 1

          if self.valorMaximo == 0:
            self.itens.append(i)
          self.valorMaximo = 0



    def dequeue(self):
        if (not(self.isEmpty())):
            self.itens.pop(0)

    def lenght(self):
        return len(self.itens)
    
    def isEmpty(self):
        return len(self.itens) == 0
    
fila = queue()
for i in range(21):
    fila.enqueue()
fila.dequeue()

print(fila.itens)

