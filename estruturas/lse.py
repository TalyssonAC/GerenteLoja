from estruturas.nodo import Nodo

class LSE:
    def __init__(self):
        self._head = None
        self._tail = None
        self._quantidade_itens = 0

    def is_empty(self):
        return self._head is None and self._tail is None

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
            if atual.valor.get_identificador_unico() == codigo:
                return atual.valor

            atual = atual.proximo

        return None

    def remover(self, codigo):
        if self.is_empty():
            return None

        if self._head.valor.get_identificador_unico() == codigo:
            return self.remover_inicio()

        anterior = self._head
        atual = self._head.proximo

        while atual is not None:
            if atual.valor.get_identificador_unico() == codigo:
                anterior.proximo = atual.proximo

                if atual == self._tail:
                    self._tail = anterior

                atual.proximo = None
                self._quantidade_itens -= 1
                return atual.valor

            anterior = atual
            atual = atual.proximo

        return None

    def remover_inicio(self):
        if self.is_empty():
            return None

        removido = self._head
        self._head = self._head.proximo

        if self._head is None:
            self._tail = None

        removido.proximo = None
        self._quantidade_itens -= 1
        return removido.valor

    def listar(self):
        valores = []
        atual = self._head

        while atual is not None:
            valores.append(atual.valor)
            atual = atual.proximo

        return valores

    def __len__(self):
        return self._quantidade_itens