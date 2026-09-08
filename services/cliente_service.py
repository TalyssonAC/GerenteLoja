from models.cliente import Cliente


class ClienteService:
    def __init__(self, cliente_repository):
        self._cliente_repository = cliente_repository

    def cadastrar(self, codigo, nome):
        cliente = Cliente(codigo, nome)
        self._cliente_repository.adicionar(cliente)
        return cliente

    def buscar_por_codigo(self, codigo):
        return self._cliente_repository.buscar_por_codigo(codigo)

    def listar(self):
        return self._cliente_repository.listar()

    def atualizar(self, codigo, nome):
        if self.buscar_por_codigo(codigo) is None:
            raise ValueError("Cliente nao encontrado.")

        cliente = Cliente(codigo, nome)
        return self._cliente_repository.atualizar(cliente)

    def remover(self, codigo):
        return self._cliente_repository.remover(codigo)
