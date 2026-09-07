from datetime import datetime
from models.item_venda import ItemVenda

class Venda:
    def __init__(self, codigo, codigo_cliente, data=None, itens=None):
        self.codigo = int(codigo)
        self.codigo_cliente = int(codigo_cliente)
        self.data = data or datetime.now().astimezone().isoformat(timespec="seconds")
        self.itens = []

        if self.codigo <= 0:
            raise ValueError("O codigo da venda precisa ser maior que zero.")

        if self.codigo_cliente <= 0:
            raise ValueError("O codigo do cliente precisa ser maior que zero.")

        if itens is not None:
            for item in itens:
                self.adicionar_item(item)
            
    def get_identificador_unico(self):
        return self.codigo

    def adicionar_item(self, item):
        if not isinstance(item, ItemVenda):
            raise ValueError("O item deve ser uma instancia de ItemVenda.")

        if item.codigo_venda != self.codigo:
            raise ValueError("O codigo da venda do item não corresponde ao codigo da venda.")

        if any(item_existente.codigo_produto == item.codigo_produto for item_existente in self.itens):
            raise ValueError("O produto já foi adicionado à venda.")

        self.itens.append(item)

    def get_valor_total(self):
        return sum(item.get_valor_total() for item in self.itens)

    def possui_itens(self):
        return len(self.itens) > 0

    def __str__(self):
        return (
            f"Venda {self.codigo} - Cliente {self.codigo_cliente} - "
            f"Data: {self.data} - Total: R$ {self.get_valor_total():.2f}"
        )



