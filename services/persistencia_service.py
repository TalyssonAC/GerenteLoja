import csv
from pathlib import Path


class PersistenciaService:
    def __init__(self, diretorio=None):
        if diretorio is None:
            diretorio = Path(__file__).resolve().parent.parent / "data"

        self._diretorio = Path(diretorio)

    def salvar_clientes(self, cliente_repository):
        linhas = [
            cliente_repository.para_linha_csv(cliente)
            for cliente in cliente_repository.listar()
        ]
        self._salvar(
            "clientes.csv",
            ["codigo", "nome"],
            linhas,
        )

    def carregar_clientes(self, cliente_repository):
        for linha in self._carregar("clientes.csv"):
            cliente_repository.adicionar(cliente_repository.de_linha_csv(linha))

    def salvar_produtos(self, produto_repository):
        linhas = [
            produto_repository.para_linha_csv(produto)
            for produto in produto_repository.listar()
        ]
        self._salvar(
            "produtos.csv",
            [
                "codigo",
                "nome",
                "preco",
                "quantidade_estoque",
                "estoque_minimo",
            ],
            linhas,
        )

    def carregar_produtos(self, produto_repository):
        for linha in self._carregar("produtos.csv"):
            produto_repository.adicionar(produto_repository.de_linha_csv(linha))

    def salvar_movimentacoes(self, movimentacao_repository):
        linhas = [
            movimentacao_repository.para_linha_csv(movimentacao)
            for movimentacao in movimentacao_repository.listar()
        ]
        self._salvar(
            "movimentacoes.csv",
            ["codigo", "codigo_produto", "tipo", "quantidade", "data"],
            linhas,
        )

    def carregar_movimentacoes(self, movimentacao_repository):
        for linha in self._carregar("movimentacoes.csv"):
            movimentacao = movimentacao_repository.de_linha_csv(linha)
            movimentacao_repository.adicionar(movimentacao)

    def salvar_vendas(self, venda_repository):
        linhas_vendas = []
        linhas_itens = []

        for venda in venda_repository.listar():
            linhas_vendas.append(venda_repository.para_linha_csv(venda))

            for item in venda.itens:
                linhas_itens.append(venda_repository.item_para_linha_csv(item))

        self._salvar(
            "vendas.csv",
            ["codigo", "codigo_cliente", "data"],
            linhas_vendas,
        )
        self._salvar(
            "itens_venda.csv",
            ["codigo_venda", "codigo_produto", "quantidade", "valor_unitario"],
            linhas_itens,
        )

    def carregar_vendas(self, venda_repository):
        vendas = {}

        for linha in self._carregar("vendas.csv"):
            venda = venda_repository.de_linha_csv(linha)
            vendas[venda.codigo] = venda

        for linha in self._carregar("itens_venda.csv"):
            item = venda_repository.item_de_linha_csv(linha)
            venda = vendas.get(item.codigo_venda)

            if venda is None:
                raise ValueError("Item de venda sem venda correspondente.")

            venda.adicionar_item(item)

        for venda in vendas.values():
            venda_repository.adicionar(venda)

    def _salvar(self, nome_arquivo, cabecalho, linhas):
        self._diretorio.mkdir(parents=True, exist_ok=True)
        caminho = self._diretorio / nome_arquivo

        with caminho.open("w", newline="", encoding="utf-8") as arquivo:
            escritor = csv.writer(arquivo)
            escritor.writerow(cabecalho)
            escritor.writerows(linhas)

    def _carregar(self, nome_arquivo):
        caminho = self._diretorio / nome_arquivo

        if not caminho.exists():
            return []

        with caminho.open("r", newline="", encoding="utf-8") as arquivo:
            return list(csv.DictReader(arquivo))
