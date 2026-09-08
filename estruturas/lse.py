from estruturas.nodo import Nodo


class LSE:
    """Lista simplesmente encadeada usada para armazenar clientes."""

    def __init__(self):
        self._head = None
        self._tail = None
        self._quantidade_itens = 0

    def is_empty(self):
        return self._head is None

    def inserir_fim(self, valor):
        if valor is None:
            raise ValueError("Valores nulos nao podem ser adicionados.")
        novo_nodo = Nodo(valor)
        if self.is_empty():
            self._head = novo_nodo
            self._tail = novo_nodo
        else:
            self._tail.proximo = novo_nodo
            self._tail = novo_nodo
        self._quantidade_itens += 1

    def buscar(self, codigo):
        atual = self._head
        while atual is not None:
            if atual.valor.get_identificador_unico() == int(codigo):
                return atual.valor
            atual = atual.proximo
        return None

    def remover(self, codigo):
        codigo = int(codigo)
        anterior = None
        atual = self._head
        while atual is not None:
            if atual.valor.get_identificador_unico() == codigo:
                if anterior is None:
                    self._head = atual.proximo
                else:
                    anterior.proximo = atual.proximo
                if atual is self._tail:
                    self._tail = anterior
                atual.proximo = None
                self._quantidade_itens -= 1
                return atual.valor
            anterior = atual
            atual = atual.proximo
        return None

    def listar(self):
        valores = []
        atual = self._head
        while atual is not None:
            valores.append(atual.valor)
            atual = atual.proximo
        return valores

    def __len__(self):
        return self._quantidade_itens
