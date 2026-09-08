from models.movimentacao_estoque import MovimentacaoEstoque
from models.produto import Produto


class EstoqueService:
    def __init__(self, produto_repository, movimentacao_repository):
        self._produto_repository = produto_repository
        self._movimentacao_repository = movimentacao_repository

    def registrar_entrada(self, codigo, codigo_produto, quantidade, data=None):
        return self._registrar_movimentacao(
            codigo,
            codigo_produto,
            "ENTRADA",
            quantidade,
            data,
        )

    def registrar_saida(self, codigo, codigo_produto, quantidade, data=None):
        return self._registrar_movimentacao(
            codigo,
            codigo_produto,
            "SAIDA",
            quantidade,
            data,
        )

    def buscar_movimentacao_por_codigo(self, codigo):
        return self._movimentacao_repository.buscar_por_codigo(codigo)

    def listar_movimentacoes(self):
        return self._movimentacao_repository.listar()

    def listar_movimentacoes_por_produto(self, codigo_produto):
        return self._movimentacao_repository.listar_por_produto(codigo_produto)

    def proximo_codigo_movimentacao(self):
        movimentacoes = self._movimentacao_repository.listar()

        if len(movimentacoes) == 0:
            return 1

        return max(movimentacao.codigo for movimentacao in movimentacoes) + 1

    def _registrar_movimentacao(
        self,
        codigo,
        codigo_produto,
        tipo,
        quantidade,
        data,
    ):
        movimentacao = MovimentacaoEstoque(
            codigo,
            codigo_produto,
            tipo,
            quantidade,
            data,
        )

        produto = self._produto_repository.buscar_por_codigo(codigo_produto)

        if produto is None:
            raise ValueError("Produto nao encontrado.")

        if self.buscar_movimentacao_por_codigo(codigo) is not None:
            raise ValueError("Ja existe uma movimentacao com esse codigo.")

        if tipo == "SAIDA" and produto.quantidade_estoque < movimentacao.quantidade:
            raise ValueError("Estoque insuficiente para realizar a saida.")

        quantidade_atualizada = produto.quantidade_estoque + movimentacao.quantidade

        if tipo == "SAIDA":
            quantidade_atualizada = produto.quantidade_estoque - movimentacao.quantidade

        produto_atualizado = Produto(
            produto.codigo,
            produto.nome,
            produto.preco,
            quantidade_atualizada,
            produto.estoque_minimo,
        )

        self._produto_repository.atualizar(produto_atualizado)
        self._movimentacao_repository.adicionar(movimentacao)
        return movimentacao
