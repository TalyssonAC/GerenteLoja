
class MovimentacaoEstoque:
    TIPOS_VALIDOS = ("ENTRADA", "SAIDA")

    def __Init__(self, codigo, codigo_produto, tipo, quantidade, data):
        self.codigo = int(codigo)
        self.codigo_produto = int(codigo_produto)
        self.tipo = str(tipo).strip().upper()
        self.quantidade = int(quantidade)
        self.data = str(data).strip()

        if self.codigo <= 0:
            raise ValueError("O codigo da movimentaçao precisa ser maior que zero.")

        if self.codigo_produto <= 0:
            raise ValueError("O codigo do produto precisa ser maior que zero.")

        if self.tipo not in self.TIPOS_VALIDOS:
            raise ValueError("O tipo da movimentação deve ser ENTRADA ou SAIDA.")

        if self.quantidade <= 0:
            raise ValueError("A quantidade precisa ser maior que zero.")

        if self.data =="":
            raise ValueError("Informe a data da movimentação.")

    def get_identificador_unico(self):
        return self.codigo

    def to_csv_row(self):
        return [
            self.codigo,
            self.codigo_produto,
            self.tipo,
            self.quantidade,
            self.data,
        ]

    def __str__(self):
        return (
            f"Movimentação {self.codigo} - Produto {self.codigo_produto} - "
            f"{self.tipo}: {self.quantidade} - Data: {self.data}"
        )


def movimentacao_estoque_from_csv_row(row):
    return MovimentacaoEstoque(
        row["codigo"],
        row["codigo_produto"],
        row["tipo"],
        row["quantidade"],
        row["data"],
    )  
