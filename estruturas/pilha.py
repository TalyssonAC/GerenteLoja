class Pilha:
    """Pilha LIFO usada pelo sistema para desfazer operacoes."""

    def __init__(self):
        self._valores = []

    def push(self, valor):
        self._valores.append(valor)

    def pop(self):
        if self.is_empty():
            raise IndexError("A pilha esta vazia.")
        return self._valores.pop()

    def peek(self):
        if self.is_empty():
            raise IndexError("A pilha esta vazia.")
        return self._valores[-1]

    def is_empty(self):
        return len(self._valores) == 0

    def __len__(self):
        return len(self._valores)
