class DNodo:
    """Nodo usado pela lista duplamente encadeada."""

    def __init__(self, valor):
        self.valor = valor
        self.anterior = None
        self.proximo = None

    def __str__(self):
        return str(self.valor)
