from models.item_venda import ItemVenda
from models.venda import Venda
from estruturas.fila import Fila

class VendaRepository:
	def __init__(self):
		self._vendas = Fila()

	def adicionar(self, venda):
		self._validar_venda(venda)

		if self.buscar_por_codigo(venda.codigo) is not None:
			raise ValueError("Ja existe uma venda com esse codigo.")

		self._vendas.enqueue(venda)

	def buscar_por_codigo(self, codigo):
		codigo = int(codigo)
		for venda in self._vendas.listar():
			if venda.codigo == codigo:
				return venda

		return None

	def listar(self):
		return self._vendas.listar()

	def primeira(self):
		if self._vendas.is_empty():
			return None
		return self._vendas.front()

	def listar_por_cliente(self, codigo_cliente):
		codigo_cliente = int(codigo_cliente)
		return [
			venda for venda in self._vendas.listar()
			if venda.codigo_cliente == codigo_cliente
		]

	def atualizar(self, venda):
		self._validar_venda(venda)

		if not self.remover(venda.codigo):
			raise ValueError("Venda nao encontrada.")
		self._vendas.enqueue(venda)
		return venda

	def remover(self, codigo):
		codigo = int(codigo)
		vendas_restantes = []
		removida = False
		for venda in self._vendas.listar():
			if venda.codigo == codigo:
				removida = True
			else:
				vendas_restantes.append(venda)
		if removida:
			self._vendas = Fila()
			for venda in vendas_restantes:
				self._vendas.enqueue(venda)
		return removida

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
