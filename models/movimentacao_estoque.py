from datetime import datetime

class MovimentacaoEstoque:
    TIPOS_VALIDOS = ("ENTRADA", "SAIDA")

    def __init__(self, codigo, codigo_produto, tipo, quantidade, data=None):
        self.codigo = int(codigo)
        self.codigo_produto = int(codigo_produto)
        self.tipo = str(tipo).strip().upper()
        self.quantidade = int(quantidade)
        self.data = data or datetime.now().astimezone().isoformat(timespec="seconds")

        if self.codigo <= 0:
            raise ValueError("O codigo da movimentaçao precisa ser maior que zero.")

        if self.codigo_produto <= 0:
            raise ValueError("O codigo do produto precisa ser maior que zero.")

        if self.tipo not in self.TIPOS_VALIDOS:
            raise ValueError("O tipo da movimentação deve ser ENTRADA ou SAIDA.")

        if self.quantidade <= 0:
            raise ValueError("A quantidade precisa ser maior que zero.")

    def get_identificador_unico(self):
        return self.codigo

    def __str__(self):
        return (
            f"Movimentação {self.codigo} - Produto {self.codigo_produto} - "
            f"{self.tipo}: {self.quantidade} - Data: {self.data}"
        )
