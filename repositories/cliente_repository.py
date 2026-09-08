from models.cliente import Cliente

class ClienteRepository:
	def __init__(self):
		self._clientes = []

	def adicionar(self, cliente):
		self._validar_cliente(cliente)

		if self.buscar_por_codigo(cliente.codigo) is not None:
			raise ValueError("Ja existe um cliente com esse codigo.")

		self._clientes.append(cliente)

	def buscar_por_codigo(self, codigo):
		codigo = int(codigo)

		for cliente in self._clientes:
			if cliente.codigo == codigo:
				return cliente

		return None

	def listar(self):
		return self._clientes.copy()

	def atualizar(self, cliente):
		self._validar_cliente(cliente)

		for indice, cliente_atual in enumerate(self._clientes):
			if cliente_atual.codigo == cliente.codigo:
				self._clientes[indice] = cliente
				return cliente

		raise ValueError("Cliente nao encontrado.")

	def remover(self, codigo):
		cliente = self.buscar_por_codigo(codigo)

		if cliente is None:
			return False

		self._clientes.remove(cliente)
		return True

	def para_linha_csv(self, cliente):
		self._validar_cliente(cliente)
		return [cliente.codigo, cliente.nome]

	def de_linha_csv(self, linha):
		return Cliente(linha["codigo"], linha["nome"])

	@staticmethod
	def _validar_cliente(cliente):
		if not isinstance(cliente, Cliente):
			raise TypeError("O valor deve ser uma instancia de Cliente.")
