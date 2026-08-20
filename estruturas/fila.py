
class Fila:
    def __init__(self):
        self._lista_de_valores = []

    def enqueue(self, item):
        self._lista_de_valores.append(item)

    def dequeue(self):
        if len(self._lista_de_valores) == 0:
            raise IndexError("Não há dados para desinfileirar!")

        return self._lista_de_valores.pop(0)

    def front(self):
        if len(self._lista_de_valores) == 0:
            raise IndexError("Não há dados na fila!")

        return self._lista_de_valores[0]

    def is_empty(self): 
        return len(self._lista_de_valores) == 0

    def size(self):
        return len(self._lista_de_valores)

    def __len__(self):
        return len(self._lista_de_valores)

fila = Fila()
fila.enqueue(10)