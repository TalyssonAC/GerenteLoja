from estruturas.dnodo import DNodo


class LDE:
    """Lista duplamente encadeada usada para armazenar produtos."""

    def __init__(self):
        self.header = DNodo(None)
        self.trailer = DNodo(None)
        self.header.proximo = self.trailer
        self.trailer.anterior = self.header
        self.quantidade_itens = 0

    def is_empty(self):
        return self.quantidade_itens == 0

    def inserir_fim(self, valor):
        if valor is None:
            raise ValueError("Valores nulos nao podem ser adicionados.")
        ultimo = self.trailer.anterior
        novo_nodo = DNodo(valor)
        ultimo.proximo = novo_nodo
        novo_nodo.anterior = ultimo
        novo_nodo.proximo = self.trailer
        self.trailer.anterior = novo_nodo
        self.quantidade_itens += 1

    def buscar(self, codigo):
        codigo = int(codigo)
        atual = self.header.proximo
        while atual is not self.trailer:
            if atual.valor.get_identificador_unico() == codigo:
                return atual.valor
            atual = atual.proximo
        return None

    def remover(self, codigo):
        codigo = int(codigo)
        atual = self.header.proximo
        while atual is not self.trailer:
            if atual.valor.get_identificador_unico() == codigo:
                atual.anterior.proximo = atual.proximo
                atual.proximo.anterior = atual.anterior
                atual.anterior = None
                atual.proximo = None
                self.quantidade_itens -= 1
                return atual.valor
            atual = atual.proximo
        return None

    def listar(self):
        valores = []
        atual = self.header.proximo
        while atual is not self.trailer:
            valores.append(atual.valor)
            atual = atual.proximo
        return valores

    def listar_inverso(self):
        valores = []
        atual = self.trailer.anterior
        while atual is not self.header:
            valores.append(atual.valor)
            atual = atual.anterior
        return valores

    def __len__(self):
        return self.quantidade_itens
