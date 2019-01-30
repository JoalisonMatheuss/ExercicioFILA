class queue:
    def __init__(self):
        self.itens = []

    def enqueue(self, valor):
        self.itens.append(valor)

    def dequeue(self):
        if (not(self.isEmpty())):
            self.itens.pop(0)

    def lenght(self):
        return len(self.itens)
    
    def isEmpty(self):
        return len(self.itens) == 0
     
