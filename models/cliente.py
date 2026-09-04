
class Cliente:
    def __init__(self, codigo, nome):
        self.codigo = int(codigo)
        self.nome = str(nome).strip()

        if self.codigo <= 0:
            raise ValueError("O codigo do cliente precisa ser maior que zero.")

        if self.nome == "":
            raise ValueError("Informe o nome do cliente.")

    def get_identificador_unico(self):
        return self.codigo

    def to_csv_row(self):
        return [self.codigo, self.nome]

    def __str__(self):
        return f"Cliente {self.codigo} - {self.nome}"


def cliente_from_csv_row(row):
    return Cliente(row["codigo"], row["nome"])