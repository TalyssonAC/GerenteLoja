class Fila:
    """Fila FIFO usada para armazenar vendas na ordem em que ocorreram."""

    def __init__(self):
        self._valores = []

    def enqueue(self, item):
        if item is None:
            raise ValueError("Valores nulos nao podem ser adicionados.")
        self._valores.append(item)

    def dequeue(self):
        if self.is_empty():
            raise IndexError("Nao ha dados para remover da fila.")
        return self._valores.pop(0)

    def front(self):
        if self.is_empty():
            raise IndexError("Nao ha dados na fila.")
        return self._valores[0]

    def is_empty(self):
        return len(self._valores) == 0

    def listar(self):
        return list(self._valores)

    def __len__(self):
        return len(self._valores)
