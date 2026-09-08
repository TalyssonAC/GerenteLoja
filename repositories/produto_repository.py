from models.produto import Produto
from estruturas.lde import LDE

class ProdutoRepository:
	def __init__(self):
		self._produtos = LDE()

	def adicionar(self, produto):
		self._validar_produto(produto)

		if self.buscar_por_codigo(produto.codigo) is not None:
			raise ValueError("Ja existe um produto com esse codigo.")

		self._produtos.inserir_fim(produto)

	def buscar_por_codigo(self, codigo):
		return self._produtos.buscar(codigo)

	def listar(self):
		return self._produtos.listar()

	def listar_inverso(self):
		return self._produtos.listar_inverso()

	def listar_abaixo_estoque_minimo(self):
		return [produto for produto in self._produtos.listar() if produto.esta_abaixo_estoque_minimo()]

	def atualizar(self, produto):
		self._validar_produto(produto)

		if self._produtos.remover(produto.codigo) is None:
			raise ValueError("Produto nao encontrado.")
		self._produtos.inserir_fim(produto)
		return produto

	def remover(self, codigo):
		return self._produtos.remover(codigo) is not None

	def para_linha_csv(self, produto):
		self._validar_produto(produto)
		return [
			produto.codigo,
			produto.nome,
			produto.preco,
			produto.quantidade_estoque,
			produto.estoque_minimo,
		]

	def de_linha_csv(self, linha):
		return Produto(
			linha["codigo"],
			linha["nome"],
			linha["preco"],
			linha["quantidade_estoque"],
			linha["estoque_minimo"],
		)

	@staticmethod
	def _validar_produto(produto):
		if not isinstance(produto, Produto):
			raise TypeError("O valor deve ser uma instancia de Produto.")
