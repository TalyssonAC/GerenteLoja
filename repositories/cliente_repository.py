from models.cliente import Cliente
from estruturas.lse import LSE

class ClienteRepository:
	def __init__(self):
		self._clientes = LSE()

	def adicionar(self, cliente):
		self._validar_cliente(cliente)

		if self.buscar_por_codigo(cliente.codigo) is not None:
			raise ValueError("Ja existe um cliente com esse codigo.")

		self._clientes.inserir_fim(cliente)

	def buscar_por_codigo(self, codigo):
		return self._clientes.buscar(codigo)

	def listar(self):
		return self._clientes.listar()

	def atualizar(self, cliente):
		self._validar_cliente(cliente)

		if self._clientes.remover(cliente.codigo) is None:
			raise ValueError("Cliente nao encontrado.")
		self._clientes.inserir_fim(cliente)
		return cliente

	def remover(self, codigo):
		return self._clientes.remover(codigo) is not None

	def para_linha_csv(self, cliente):
		self._validar_cliente(cliente)
		return [cliente.codigo, cliente.nome]

	def de_linha_csv(self, linha):
		return Cliente(linha["codigo"], linha["nome"])

	@staticmethod
	def _validar_cliente(cliente):
		if not isinstance(cliente, Cliente):
			raise TypeError("O valor deve ser uma instancia de Cliente.")
