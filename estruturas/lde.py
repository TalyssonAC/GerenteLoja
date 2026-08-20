from nodo import DNodo
import os

def limpar_terminal():
    os.system("cls")

class LDE:
    def __init__(self):
        self.header = DNodo(None)
        self.trailer = DNodo(None)
        self.quantidade_itens = 0

    def is_empty(self):
        return self.header.proximo == None and self.trailer.anterior == None and self.quantidade_itens == 0

    def inserir_inicio(self, valor):
        if self.is_empty():
            novo_nodo = DNodo(valor)
            novo_nodo.anterior = self.header
            novo_nodo.proximo = self.trailer
            self.header.proximo = novo_nodo
            self.trailer.anterior = novo_nodo
            self.quantidade_itens += 1
            return

        novo_nodo = DNodo(valor)
        atual_primeiro = self.header.proximo
        atual_primeiro.anterior = novo_nodo
        novo_nodo.proximo = atual_primeiro
        novo_nodo.anterior = self.header
        self.header.proximo = novo_nodo

        self.quantidade_itens += 1

    def inserir_fim(self, valor):
        if self.is_empty():
            novo_nodo = DNodo(valor)
            novo_nodo.anterior = self.header
            novo_nodo.proximo = self.trailer
            self.header.proximo = novo_nodo
            self.trailer.anterior = novo_nodo
            self.quantidade_itens += 1
            return

        novo_nodo = DNodo(valor)
        atual_ultimo = self.trailer.anterior
        atual_ultimo.proximo = novo_nodo
        novo_nodo.anterior = atual_ultimo
        novo_nodo.proximo = self.trailer
        self.trailer.anterior = novo_nodo

        self.quantidade_itens += 1

    def remover_inicio(self):
        if self.is_empty():
            print("Nao há dados para remover")
            return

        if self.quantidade_itens == 1:
            unico_dado = self.header.proximo
            unico_dado.anterior = None
            unico_dado.proximo = None
            self.header.proximo = None
            self.trailer.anterior = None
            self.quantidade_itens -= 1
            return

        dado_removido = self.header.proximo
        novo_primeiro_dado = dado_removido.proximo

        dado_removido.anterior = None
        dado_removido.proximo = None
        self.header.proximo = novo_primeiro_dado
        novo_primeiro_dado.anterior = self.header
        self.quantidade_itens -= 1
        

    def remover_fim(self):
        if self.is_empty():
            print("Nao há dados para remover")
            return

        if self.quantidade_itens == 1:
            unico_dado = self.trailer.anterior
            unico_dado.anterior = None
            unico_dado.proximo = None
            self.header.proximo = None
            self.trailer.anterior = None
            self.quantidade_itens -= 1
            return

        dado_removido = self.trailer.anterior
        novo_ultimo_dado = dado_removido.anterior

        dado_removido.anterior = None
        dado_removido.proximo = None
        self.trailer.anterior = novo_ultimo_dado
        novo_ultimo_dado.proximo = self.trailer
        self.quantidade_itens -= 1

    def imprimir(self):
        if self.is_empty():
            print("Nao há dados para imprimir")
            return

        item = self.header
        while item is not None:
            if item == self.header:
                print(f"HEADER -> {item.proximo}")
                item = item.proximo
                continue

            if item == self.trailer:
                print(f"{item.anterior} <- TRAILER")
                break

            print(f"Anterior: {item.anterior} - ({item}) - Próximo: {item.proximo}")
            item = item.proximo
    

    def remover_especifico(self, identificador):
        if self.is_empty():
            print("Nao há dados para imprimir")
            return

        item = self.header
        deletou = False
        while item is not None:

            if item == self.header or item == self.trailer:
                item = item.proximo
                continue

            if item.valor.get_identificador_unico() == identificador:
                deletou = True
                dado_deletado = item
                dado_deletado_anterior = item.anterior
                dado_deletado_proximo = item.proximo

                dado_deletado.proximo = None
                dado_deletado.anterior = None

                dado_deletado_anterior.proximo = dado_deletado_proximo
                dado_deletado_proximo.anterior = dado_deletado_anterior
                self.quantidade_itens -= 1
                break
            
            item = item.proximo
        
        if deletou == False:
            print("Dado nao encontrado para remover")
        else:
            print("Dado deletado com sucesso")

class Cliente:
    def __init__(self, codigo, nome):
        self.codigo = codigo
        self.nome = nome

    def get_identificador_unico(self):
        return self.codigo

    def __str__(self):
        return f"Cliente {self.codigo} - {self.nome}"

limpar_terminal()
cadastros_cliente = LDE()
cadastros_cliente.inserir_inicio(Cliente(1, "Augusto"))
cadastros_cliente.inserir_inicio(Cliente(2, "Joao"))
cadastros_cliente.inserir_fim(Cliente(3, "Maria"))
cadastros_cliente.imprimir()
# cadastros_cliente.remover_inicio()
cadastros_cliente.remover_especifico(1)
print("===========================")
cadastros_cliente.imprimir()
