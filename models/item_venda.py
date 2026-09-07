
class ItemVenda:
    def __init__(self, codigo_venda, codigo_produto, quantidade, valor_unitario):
        self.codigo_venda = int(codigo_venda)
        self.codigo_produto = int(codigo_produto)
        self.quantidade = int(quantidade)
        self.valor_unitario = float(valor_unitario)

        if self.codigo_venda <= 0:
            raise ValueError("O codigo da venda precisa ser maior que zero.")

        if self.codigo_produto <= 0:
            raise ValueError("O codigo do produto precisa ser maior que zero.")

        if self.quantidade <= 0:
            raise ValueError("A quantidade precisa ser maior que zero.")

        if self.valor_unitario < 0:
            raise ValueError("O valor unitario não pode ser negativo.")

    def get_identificador_unico(self):
        return (self.codigo_venda, self.codigo_produto)

    def get_valor_total(self):
        return self.quantidade * self.valor_unitario

    def to_csv_row(self):
        return [
            self.codigo_venda,
            self.codigo_produto,
            self.quantidade,
            self.valor_unitario,
        ]

    def __str__(self):
        return (
            f"Item da venda {self.codigo_venda} - Produto {self.codigo_produto} - "
            f"Quantidade: {self.quantidade} - Valor unitario: R$ {self.valor_unitario:.2f}"
        )

    def item_venda_fro_csv_row(row):
        return ItemVenda(
            row["codigo_venda"],
            row["codigo_produto"],
            row["quantidade"],
            row["valor_unitario"],
        )