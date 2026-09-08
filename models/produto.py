
class Produto:
    def __init__(self, codigo, nome, preco, quantidade_estoque, estoque_minimo):
        self.codigo = int(codigo)
        self.nome = str(nome).strip()
        self.preco = float(preco)
        self.quantidade_estoque = int(quantidade_estoque)
        self.estoque_minimo = int(estoque_minimo)

        if self.codigo <= 0:
            raise ValueError("O codigo do produto precisa ser maior que zero.")

        if self.nome == "":
            raise ValueError("O nome do produto não pode ser vazio.")

        if self.preco <= 0:
            raise ValueError("O preco do produto precisa ser maior que zero.")

        if self.quantidade_estoque < 0:
            raise ValueError("A quantidade em estoque do produto não pode ser negativa.")

        if self.estoque_minimo < 0:
            raise ValueError("O estoque minimo do produto não pode ser negativo.")

    def get_identificador_unico(self):
        return self.codigo

    def esta_abaixo_estoque_minimo(self):
        return self.quantidade_estoque < self.estoque_minimo

    def to_csv_row(self):
        return [
            self.codigo,
            self.nome,
            self.preco,
            self.quantidade_estoque,
            self.estoque_minimo,
        ]

    def __str__(self):
        return (
            f"Produto {self.codigo} - {self.nome} - Preco: R$ {self.preco:.2f} - "
            f"Estoque: {self.quantidade_estoque} - Estoque minimo: {self.estoque_minimo}"
        )
