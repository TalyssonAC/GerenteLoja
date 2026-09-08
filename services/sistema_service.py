from algoritimos.busca_binaria import buscar_produto_por_codigo
from algoritimos.ordenacao import ordenar_produtos_por_id
from estruturas.pilha import Pilha
from repositories.cliente_repository import ClienteRepository
from repositories.movimentacao_estoque_repository import MovimentacaoEstoqueRepository
from repositories.produto_repository import ProdutoRepository
from repositories.venda_repository import VendaRepository
from services.cliente_service import ClienteService
from services.estoque_service import EstoqueService
from services.persistencia_service import PersistenciaService
from services.produto_service import ProdutoService
from services.venda_service import VendaService


class SistemaService:
    """Coordena o caso de uso completo e mantem as estruturas obrigatorias."""

    def __init__(self, diretorio_dados=None):
        self.clientes_repository = ClienteRepository()
        self.produtos_repository = ProdutoRepository()
        self.movimentacoes_repository = MovimentacaoEstoqueRepository()
        self.vendas_repository = VendaRepository()
        self.persistencia = PersistenciaService(diretorio_dados)
        self.clientes = ClienteService(self.clientes_repository)
        self.produtos = ProdutoService(self.produtos_repository)
        self.estoque = EstoqueService(self.produtos_repository, self.movimentacoes_repository)
        self.vendas = VendaService(
            self.vendas_repository,
            self.clientes_repository,
            self.produtos_repository,
            self.estoque,
        )
        self.historico = Pilha()
        self.carregar_dados()

    def carregar_dados(self):
        self.persistencia.carregar_clientes(self.clientes_repository)
        self.persistencia.carregar_produtos(self.produtos_repository)
        self.persistencia.carregar_movimentacoes(self.movimentacoes_repository)
        self.persistencia.carregar_vendas(self.vendas_repository)

    def salvar_dados(self):
        self.persistencia.salvar_clientes(self.clientes_repository)
        self.persistencia.salvar_produtos(self.produtos_repository)
        self.persistencia.salvar_movimentacoes(self.movimentacoes_repository)
        self.persistencia.salvar_vendas(self.vendas_repository)

    @staticmethod
    def _proximo_codigo(registros):
        return max((registro.codigo for registro in registros), default=0) + 1

    def cadastrar_cliente(self, nome):
        cliente = self.clientes.cadastrar(self._proximo_codigo(self.clientes.listar()), nome)
        self.historico.push(("cliente", cliente.codigo))
        self.salvar_dados()
        return cliente

    def cadastrar_produto(self, nome, preco, quantidade, estoque_minimo=0):
        produto = self.produtos.cadastrar(
            self._proximo_codigo(self.produtos.listar()),
            nome, preco, quantidade, estoque_minimo,
        )
        self.historico.push(("produto", produto.codigo))
        self.salvar_dados()
        return produto

    def atualizar_estoque(self, codigo, nova_quantidade):
        produto = self.produtos.buscar_por_codigo(codigo)
        if produto is None:
            raise ValueError("Produto nao encontrado.")
        anterior = produto.quantidade_estoque
        atualizado = self.produtos.atualizar(
            codigo, produto.nome, produto.preco, nova_quantidade, produto.estoque_minimo
        )
        self.historico.push(("estoque", atualizado.codigo, anterior))
        self.salvar_dados()
        return atualizado

    def remover_cliente(self, codigo):
        cliente = self.clientes.buscar_por_codigo(codigo)
        if cliente is None:
            return False
        self.clientes.remover(codigo)
        self.historico.push(("cliente_removido", cliente))
        self.salvar_dados()
        return True

    def remover_produto(self, codigo):
        produto = self.produtos.buscar_por_codigo(codigo)
        if produto is None:
            return False
        self.produtos.remover(codigo)
        self.historico.push(("produto_removido", produto))
        self.salvar_dados()
        return True

    def realizar_venda(self, codigo_cliente, itens):
        codigos_antes = {m.codigo for m in self.estoque.listar_movimentacoes()}
        venda = self.vendas.registrar(
            self._proximo_codigo(self.vendas.listar()), codigo_cliente, itens
        )
        codigos_movimentacoes = [
            m.codigo for m in self.estoque.listar_movimentacoes()
            if m.codigo not in codigos_antes
        ]
        self.historico.push(("venda", venda.codigo, codigos_movimentacoes))
        self.salvar_dados()
        return venda

    def listar_produtos_ordenados(self):
        return ordenar_produtos_por_id(self.produtos.listar())

    def buscar_produto_binario(self, codigo):
        return buscar_produto_por_codigo(self.listar_produtos_ordenados(), codigo)

    def valor_total_estoque(self):
        return sum(p.preco * p.quantidade_estoque for p in self.produtos.listar())

    def valor_total_vendas(self):
        return sum(v.get_valor_total() for v in self.vendas.listar())

    def cliente_que_mais_gastou(self):
        if not self.vendas.listar():
            return None
        gastos = self.clientes_e_valores_gastos()
        return max(gastos, key=lambda par: par[1], default=None)

    def clientes_e_valores_gastos(self):
        resultado = []
        for cliente in self.clientes.listar():
            total = sum(v.get_valor_total() for v in self.vendas.listar_por_cliente(cliente.codigo))
            resultado.append((cliente, total))
        return resultado

    def produto_mais_vendido(self):
        quantidades = {}
        for venda in self.vendas.listar():
            for item in venda.itens:
                quantidades[item.codigo_produto] = quantidades.get(item.codigo_produto, 0) + item.quantidade
        if not quantidades:
            return None
        codigo = max(quantidades, key=quantidades.get)
        return self.produtos.buscar_por_codigo(codigo), quantidades[codigo]

    def desfazer_ultima_operacao(self):
        operacao = self.historico.pop()
        tipo = operacao[0]
        if tipo == "cliente":
            self.clientes.remover(operacao[1])
        elif tipo == "cliente_removido":
            self.clientes_repository.adicionar(operacao[1])
        elif tipo == "produto":
            self.produtos.remover(operacao[1])
        elif tipo == "produto_removido":
            self.produtos_repository.adicionar(operacao[1])
        elif tipo == "estoque":
            produto = self.produtos.buscar_por_codigo(operacao[1])
            self.produtos.atualizar(produto.codigo, produto.nome, produto.preco, operacao[2], produto.estoque_minimo)
        elif tipo == "venda":
            venda = self.vendas.buscar_por_codigo(operacao[1])
            if venda is not None:
                for item in venda.itens:
                    produto = self.produtos.buscar_por_codigo(item.codigo_produto)
                    self.produtos.atualizar(produto.codigo, produto.nome, produto.preco, produto.quantidade_estoque + item.quantidade, produto.estoque_minimo)
                self.vendas_repository.remover(venda.codigo)
                for codigo_movimentacao in operacao[2]:
                    self.movimentacoes_repository.remover(codigo_movimentacao)
        self.salvar_dados()
        return tipo
