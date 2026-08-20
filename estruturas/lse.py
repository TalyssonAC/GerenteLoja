from nodo import Nodo

class LSE:

    def __init__(self):
        self._head = None 
        self._tail = None
        self._quantidade_itens = 0

    def is_empty(self):
        return self._head is None and self._tail is None and self._quantidade_itens == 0

    def inserir_inicio(self, dado_a_ser_inserido):
        if dado_a_ser_inserido is None:
            raise ValueError("Valores nulos não podem ser adicionados.")

        nodo_a_ser_inserido = Nodo(dado_a_ser_inserido)

        if self.is_empty():
            self._head = nodo_a_ser_inserido
            self._tail = nodo_a_ser_inserido
            self._quantidade_itens += 1
            return

        nodo_a_ser_inserido.proximo = self._head
        self._head = nodo_a_ser_inserido

        self._quantidade_itens += 1

    def inserir_fim(self, dado_a_ser_inserido):
        if dado_a_ser_inserido is None:
            raise ValueError("Valores nulos não podem ser adicionados.")

        nodo_a_ser_inserido = Nodo(dado_a_ser_inserido)

        if self.is_empty():
            self._head = nodo_a_ser_inserido
            self._tail = nodo_a_ser_inserido
            self._quantidade_itens += 1
            return

        self._tail.proximo = nodo_a_ser_inserido
        self._tail = nodo_a_ser_inserido

        self._quantidade_itens += 1

    def buscar(self, codigo):
        if self.is_empty():
            return None

        item = self._head

        while item is not None:
            if item.valor.codigo == codigo:
                return item.valor

            item = item.proximo

        return None

    def remover(self, codigo):
        if self.is_empty():
            return None

        if self._head.valor.codigo == codigo:
            return self.remover_inicio()

        item_anterior = self._head
        item_atual = self._head.proximo

        while item_atual is not None:
            if item_atual.valor.codigo == codigo:
                musica_removida = item_atual.valor
                item_anterior.proximo = item_atual.proximo

                if item_atual == self._tail:
                    self._tail = item_anterior

                item_atual.proximo = None
                self._quantidade_itens -= 1
                return musica_removida

            item_anterior = item_atual
            item_atual = item_atual.proximo

        return None

    def remover_inicio(self):
        if self.is_empty():
            print("Não há músicas para remover.")
            return None

        if self._head == self._tail and self._quantidade_itens == 1:
            musica_removida = self._head.valor
            self._tail = None
            self._head = None
            self._quantidade_itens -= 1
            return musica_removida

        nodo_removido = self._head
        self._head = nodo_removido.proximo
        nodo_removido.proximo = None

        self._quantidade_itens -= 1

        return nodo_removido.valor

    def remover_fim(self):
        if self.is_empty():
            print("Não há músicas para remover.")
            return None

        if self._head == self._tail and self._quantidade_itens == 1:
            musica_removida = self._tail.valor
            self._tail = None
            self._head = None
            self._quantidade_itens -= 1
            return musica_removida

        item = self._head

        while item is not None:
            if item.proximo == self._tail:
                nodo_removido = item.proximo
                item.proximo = None
                self._tail = item
                self._quantidade_itens -= 1
                return nodo_removido.valor

            item = item.proximo

        return None

    def imprimir_lista_completa(self):
        if self.is_empty():
            print("Não há músicas na playlist.")
            return

        print("===== PLAYLIST COMPLETA =====")

        item = self._head
        contador = 1

        while item is not None:
            print(f"{contador} - {item.valor}")
            item = item.proximo
            contador += 1

    def imprimir_lista(self):
        self.imprimir_lista_completa()

    def imprimir_lado_a_lado(self):
        saida = ""

        item = self._head
        while item is not None:
            if item == self._head and item == self._tail:
                saida += f"(HEAD) {item.valor} (TAIL)"
                break

            if item == self._head:
                saida += f"(HEAD) {item.valor} -> "
                item = item.proximo
                continue

            if item == self._tail:
                saida += f"{item.valor} (TAIL)"
                item = item.proximo
                continue

            saida += f"{item.valor} -> "

            item = item.proximo

        print(saida)

    def get_quantidade_de_dados(self):
        return self._quantidade_itens