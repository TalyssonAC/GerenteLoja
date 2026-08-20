
class Pilha:

    def __init__(self):
        self._lista_de_valores = [] 

    def push(self, valor): 
        
        self._lista_de_valores.insert(0, valor) 
    def is_empty(self):
        return len(self._lista_de_valores) == 0

    def pop(self):

        if self.is_empty():
            raise IndexError("A pilha está vazia, não há dados para remover")


        return self._lista_de_valores.pop(0)

    def peek(self):
  
        if self.is_empty():
            raise IndexError("A pilha está vazia, não há dados para retornar")

        return self._lista_de_valores[0]

    def __len__(self):
        return len(self._lista_de_valores)