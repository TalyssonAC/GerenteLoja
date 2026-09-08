from models.produto import Produto


class ProdutoService:
    def __init__(self, produto_repository):
        self._produto_repository = produto_repository

    def cadastrar(self, codigo, nome, preco, quantidade_estoque, estoque_minimo):
        produto = Produto(
            codigo,
            nome,
            preco,
            quantidade_estoque,
            estoque_minimo,
        )
        self._produto_repository.adicionar(produto)
        return produto

    def buscar_por_codigo(self, codigo):
        return self._produto_repository.buscar_por_codigo(codigo)

    def listar(self):
        return self._produto_repository.listar()

    def listar_inverso(self):
        return self._produto_repository.listar_inverso()

    def listar_abaixo_estoque_minimo(self):
        return self._produto_repository.listar_abaixo_estoque_minimo()

    def atualizar(self, codigo, nome, preco, quantidade_estoque, estoque_minimo):
        if self.buscar_por_codigo(codigo) is None:
            raise ValueError("Produto nao encontrado.")

        produto = Produto(
            codigo,
            nome,
            preco,
            quantidade_estoque,
            estoque_minimo,
        )
        return self._produto_repository.atualizar(produto)

    def remover(self, codigo):
        return self._produto_repository.remover(codigo)
