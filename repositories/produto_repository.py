from models.produto import Produto

class ProdutoRepository:
	def __init__(self):
		self._produtos = []

	def adicionar(self, produto):
		self._validar_produto(produto)

		if self.buscar_por_codigo(produto.codigo) is not None:
			raise ValueError("Ja existe um produto com esse codigo.")

		self._produtos.append(produto)

	def buscar_por_codigo(self, codigo):
		codigo = int(codigo)

		for produto in self._produtos:
			if produto.codigo == codigo:
				return produto

		return None

	def listar(self):
		return self._produtos.copy()

	def listar_abaixo_estoque_minimo(self):
		return [produto for produto in self._produtos if produto.esta_abaixo_estoque_minimo()]

	def atualizar(self, produto):
		self._validar_produto(produto)

		for indice, produto_atual in enumerate(self._produtos):
			if produto_atual.codigo == produto.codigo:
				self._produtos[indice] = produto
				return produto

		raise ValueError("Produto nao encontrado.")

	def remover(self, codigo):
		produto = self.buscar_por_codigo(codigo)

		if produto is None:
			return False

		self._produtos.remove(produto)
		return True

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
