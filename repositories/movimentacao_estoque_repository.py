from models.movimentacao_estoque import MovimentacaoEstoque

class MovimentacaoEstoqueRepository:
    def __init__(self):
        self._movimentacoes = []

    def adicionar(self, movimentacao):
        self._validar_movimentacao(movimentacao)

        if self.buscar_por_codigo(movimentacao.codigo) is not None:
            raise ValueError("Ja existe uma movimentacao com esse codigo.")

        self._movimentacoes.append(movimentacao)

    def buscar_por_codigo(self, codigo):
        codigo = int(codigo)

        for movimentacao in self._movimentacoes:
            if movimentacao.codigo == codigo:
                return movimentacao

        return None

    def listar(self):
        return self._movimentacoes.copy()

    def listar_por_produto(self, codigo_produto):
        codigo_produto = int(codigo_produto)
        return [
            movimentacao for movimentacao in self._movimentacoes
            if movimentacao.codigo_produto == codigo_produto
        ]

    def atualizar(self, movimentacao):
        self._validar_movimentacao(movimentacao)

        for indice, movimentacao_atual in enumerate(self._movimentacoes):
            if movimentacao_atual.codigo == movimentacao.codigo:
                self._movimentacoes[indice] = movimentacao
                return movimentacao

        raise ValueError("Movimentacao nao encontrada.")

    def remover(self, codigo):
        movimentacao = self.buscar_por_codigo(codigo)

        if movimentacao is None:
            return False

        self._movimentacoes.remove(movimentacao)
        return True

    def para_linha_csv(self, movimentacao):
        self._validar_movimentacao(movimentacao)
        return [
            movimentacao.codigo,
            movimentacao.codigo_produto,
            movimentacao.tipo,
            movimentacao.quantidade,
            movimentacao.data,
        ]

    def de_linha_csv(self, linha):
        return MovimentacaoEstoque(
            linha["codigo"],
            linha["codigo_produto"],
            linha["tipo"],
            linha["quantidade"],
            linha["data"],
        )

    @staticmethod
    def _validar_movimentacao(movimentacao):
        if not isinstance(movimentacao, MovimentacaoEstoque):
            raise TypeError(
                "O valor deve ser uma instancia de MovimentacaoEstoque."
            )