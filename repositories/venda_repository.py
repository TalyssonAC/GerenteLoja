from models.item_venda import ItemVenda
from models.venda import Venda

class VendaRepository:
	def __init__(self):
		self._vendas = []

	def adicionar(self, venda):
		self._validar_venda(venda)

		if self.buscar_por_codigo(venda.codigo) is not None:
			raise ValueError("Ja existe uma venda com esse codigo.")

		self._vendas.append(venda)

	def buscar_por_codigo(self, codigo):
		codigo = int(codigo)

		for venda in self._vendas:
			if venda.codigo == codigo:
				return venda

		return None

	def listar(self):
		return self._vendas.copy()

	def listar_por_cliente(self, codigo_cliente):
		codigo_cliente = int(codigo_cliente)
		return [
			venda for venda in self._vendas
			if venda.codigo_cliente == codigo_cliente
		]

	def atualizar(self, venda):
		self._validar_venda(venda)

		for indice, venda_atual in enumerate(self._vendas):
			if venda_atual.codigo == venda.codigo:
				self._vendas[indice] = venda
				return venda

		raise ValueError("Venda nao encontrada.")

	def remover(self, codigo):
		venda = self.buscar_por_codigo(codigo)

		if venda is None:
			return False

		self._vendas.remove(venda)
		return True

	def para_linha_csv(self, venda):
		self._validar_venda(venda)
		return [venda.codigo, venda.codigo_cliente, venda.data]

	def de_linha_csv(self, linha):
		return Venda(linha["codigo"], linha["codigo_cliente"], linha["data"])

	@staticmethod
	def item_para_linha_csv(item):
		if not isinstance(item, ItemVenda):
			raise TypeError("O valor deve ser uma instancia de ItemVenda.")

		return [
			item.codigo_venda,
			item.codigo_produto,
			item.quantidade,
			item.valor_unitario,
		]

	@staticmethod
	def item_de_linha_csv(linha):
		return ItemVenda(
			linha["codigo_venda"],
			linha["codigo_produto"],
			linha["quantidade"],
			linha["valor_unitario"],
		)

	@staticmethod
	def _validar_venda(venda):
		if not isinstance(venda, Venda):
			raise TypeError("O valor deve ser uma instancia de Venda.")
