import os

from services.sistema_service import SistemaService


def ler_inteiro(mensagem, minimo=None):
	valor = int(input(mensagem).strip())
	if minimo is not None and valor < minimo:
		raise ValueError(f"Informe um numero maior ou igual a {minimo}.")
	return valor


def ler_float(mensagem, minimo=None):
	texto = input(mensagem).strip().replace("R$", "").replace(" ", "")
	if "," in texto:
		texto = texto.replace(".", "").replace(",", ".")
	else:
		texto = texto.replace(",", ".")

	valor = float(texto)
	if minimo is not None and valor < minimo:
		raise ValueError(f"Informe um numero maior ou igual a {minimo}.")
	return valor


def ler_texto(mensagem):
	valor = input(mensagem).strip()
	if valor == "":
		raise ValueError("Este campo nao pode ficar vazio.")
	return valor


def pausar():
	input("\nPressione ENTER para continuar...")


def limpar_tela():
	comando = "cls" if os.name == "nt" else "clear"
	os.system(comando)


def imprimir_registros(registros, mensagem_vazia):
	if len(registros) == 0:
		print(mensagem_vazia)
		return

	for registro in registros:
		print(registro)


def mostrar_menu():
	limpar_tela()
	print("\n==============================")
	print(" SISTEMA DE ESTOQUE E VENDAS")
	print("==============================")
	print("1 - Vender")
	print("2 - Estoque")
	print("0 - Sair")


def mostrar_menu_vender():
	limpar_tela()
	print("\n==============================")
	print(" VENDER")
	print("==============================")
	print("1 - Realizar venda")
	print("2 - Gerenciar clientes")
	print("3 - Informacoes sobre vendas")
	print("0 - Voltar")


def mostrar_menu_clientes():
	limpar_tela()
	print("\n==============================")
	print(" GERENCIAMENTO DE CLIENTES")
	print("==============================")
	print("1 - Cadastrar cliente")
	print("2 - Listar clientes")
	print("3 - Buscar cliente")
	print("4 - Remover cliente")
	print("0 - Voltar")


def mostrar_menu_informacoes_vendas():
	limpar_tela()
	print("\n==============================")
	print(" INFORMACOES SOBRE VENDAS")
	print("==============================")
	print("1 - Visualizar fila de vendas")
	print("2 - Visualizar primeira venda da fila")
	print("3 - Exibir valor total das vendas")
	print("4 - Exibir clientes e valores totais gastos")
	print("5 - Exibir cliente que mais gastou")
	print("6 - Exibir produto mais vendido")
	print("7 - Desfazer ultima operacao")
	print("0 - Voltar")


def mostrar_menu_estoque():
	limpar_tela()
	print("\n==============================")
	print(" GERENCIAMENTO DE ESTOQUE")
	print("==============================")
	print("1 - Cadastrar produto")
	print("2 - Listar produtos")
	print("3 - Buscar produto")
	print("4 - Atualizar estoque")
	print("5 - Remover produto")
	print("6 - Listar produtos em ordem inversa")
	print("7 - Listar produtos ordenados por ID")
	print("8 - Buscar produto por ID usando Busca Binaria")
	print("9 - Exibir valor total do estoque")
	print("10 - Listar movimentacoes de estoque")
	print("11 - Listar produtos abaixo do estoque minimo")
	print("0 - Voltar")


def exibir_cliente(cliente):
	if cliente is None:
		print("Cliente nao encontrado.")
	else:
		print(cliente)


def exibir_produto(produto):
	if produto is None:
		print("Produto nao encontrado.")
	else:
		print(produto)


def cadastrar_venda(service):
	codigo_cliente = ler_inteiro("Codigo do cliente: ", 1)
	quantidade_itens = ler_inteiro("Quantidade de produtos diferentes: ", 1)
	itens = []

	for indice in range(quantidade_itens):
		print(f"\nItem {indice + 1}")
		codigo_produto = ler_inteiro("Codigo do produto: ", 1)
		quantidade = ler_inteiro("Quantidade: ", 1)
		itens.append((codigo_produto, quantidade))

	venda = service.realizar_venda(codigo_cliente, itens)
	print(f"Venda realizada com sucesso: {venda}")
	for item in venda.itens:
		print(f"  Produto {item.codigo_produto} - quantidade: {item.quantidade}")


def executar_cliente(opcao, service):
	if opcao == 1:
		nome = ler_texto("Nome do cliente: ")
		cliente = service.cadastrar_cliente(nome)
		print(f"Cliente cadastrado com sucesso: {cliente}")

	elif opcao == 2:
		imprimir_registros(service.clientes.listar(), "Nenhum cliente cadastrado.")

	elif opcao == 3:
		codigo = ler_inteiro("Codigo do cliente: ", 1)
		exibir_cliente(service.clientes.buscar_por_codigo(codigo))

	elif opcao == 4:
		codigo = ler_inteiro("Codigo do cliente: ", 1)
		if service.remover_cliente(codigo):
			print("Cliente removido com sucesso.")
		else:
			print("Cliente nao encontrado.")

	else:
		print("Opcao invalida. Tente novamente.")


def executar_informacao_venda(opcao, service):
	if opcao == 1:
		imprimir_registros(service.vendas.listar(), "A fila de vendas esta vazia.")

	elif opcao == 2:
		primeira = service.vendas_repository.primeira()
		if primeira is None:
			print("A fila de vendas esta vazia.")
		else:
			print(primeira)

	elif opcao == 3:
		print(f"Valor total das vendas: R$ {service.valor_total_vendas():.2f}")

	elif opcao == 4:
		gastos = service.clientes_e_valores_gastos()
		if len(gastos) == 0:
			print("Nenhum cliente cadastrado.")
		else:
			for cliente, total in gastos:
				print(f"{cliente.nome} - R$ {total:.2f}")

	elif opcao == 5:
		resultado = service.cliente_que_mais_gastou()
		if resultado is None:
			print("Ainda nao existem vendas registradas.")
		else:
			cliente, total = resultado
			print(f"Cliente que mais gastou: {cliente.nome} - R$ {total:.2f}")

	elif opcao == 6:
		resultado = service.produto_mais_vendido()
		if resultado is None:
			print("Ainda nao existem produtos vendidos.")
		else:
			produto, quantidade = resultado
			print(f"Produto mais vendido: {produto.nome} - {quantidade} unidade(s)")

	elif opcao == 7:
		tipo = service.desfazer_ultima_operacao()
		print(f"Ultima operacao desfeita: {tipo}.")

	else:
		print("Opcao invalida. Tente novamente.")


def executar_estoque(opcao, service):
	if opcao == 1:
		nome = ler_texto("Nome do produto: ")
		preco = ler_float("Preco: ", 0.01)
		quantidade = ler_inteiro("Quantidade em estoque: ", 0)
		estoque_minimo = ler_inteiro("Estoque minimo: ", 0)
		produto = service.cadastrar_produto(nome, preco, quantidade, estoque_minimo)
		print(f"Produto cadastrado com sucesso: {produto}")

	elif opcao == 2:
		imprimir_registros(service.produtos.listar(), "Nenhum produto cadastrado.")

	elif opcao == 3:
		codigo = ler_inteiro("Codigo do produto: ", 1)
		exibir_produto(service.produtos.buscar_por_codigo(codigo))

	elif opcao == 4:
		codigo = ler_inteiro("Codigo do produto: ", 1)
		quantidade = ler_inteiro("Nova quantidade em estoque: ", 0)
		produto = service.atualizar_estoque(codigo, quantidade)
		print(f"Estoque atualizado com sucesso: {produto}")

	elif opcao == 5:
		codigo = ler_inteiro("Codigo do produto: ", 1)
		if service.remover_produto(codigo):
			print("Produto removido com sucesso.")
		else:
			print("Produto nao encontrado.")

	elif opcao == 6:
		imprimir_registros(service.produtos.listar_inverso(), "Nenhum produto cadastrado.")

	elif opcao == 7:
		imprimir_registros(service.listar_produtos_ordenados(), "Nenhum produto cadastrado.")

	elif opcao == 8:
		codigo = ler_inteiro("Codigo do produto: ", 1)
		exibir_produto(service.buscar_produto_binario(codigo))

	elif opcao == 9:
		print(f"Valor total do estoque: R$ {service.valor_total_estoque():.2f}")

	elif opcao == 10:
		imprimir_registros(
			service.estoque.listar_movimentacoes(),
			"Nenhuma movimentacao de estoque registrada.",
		)

	elif opcao == 11:
		imprimir_registros(
			service.produtos.listar_abaixo_estoque_minimo(),
			"Nenhum produto abaixo do estoque minimo.",
		)

	else:
		print("Opcao invalida. Tente novamente.")


def executar_menu(mostrar, executar, service, mensagem):
	while True:
		mostrar()
		try:
			opcao = ler_inteiro(mensagem)
			if opcao == 0:
				return
			executar(opcao, service)
		except (ValueError, TypeError, IndexError, KeyError, OSError) as erro:
			print(f"Erro: {erro}")
		pausar()


def menu_clientes(service):
	executar_menu(
		mostrar_menu_clientes,
		executar_cliente,
		service,
		"Escolha uma opcao de clientes: ",
	)


def menu_informacoes_vendas(service):
	executar_menu(
		mostrar_menu_informacoes_vendas,
		executar_informacao_venda,
		service,
		"Escolha uma opcao de vendas: ",
	)


def menu_vender(service):
	while True:
		mostrar_menu_vender()
		pausar_apos_operacao = True
		try:
			opcao = ler_inteiro("Escolha uma opcao de vendas: ")
			if opcao == 0:
				return
			if opcao == 1:
				cadastrar_venda(service)
			elif opcao == 2:
				pausar_apos_operacao = False
				menu_clientes(service)
			elif opcao == 3:
				pausar_apos_operacao = False
				menu_informacoes_vendas(service)
			else:
				print("Opcao invalida. Tente novamente.")
		except (ValueError, TypeError, IndexError, KeyError, OSError) as erro:
			print(f"Erro: {erro}")
		if pausar_apos_operacao:
			pausar()


def menu_estoque(service):
	executar_menu(
		mostrar_menu_estoque,
		executar_estoque,
		service,
		"Escolha uma opcao de estoque: ",
	)


def executar_opcao(opcao, service):
	if opcao == 1:
		menu_vender(service)
	elif opcao == 2:
		menu_estoque(service)
	else:
		print("Opcao invalida. Tente novamente.")
		pausar()


def main():
	try:
		service = SistemaService()
	except (ValueError, TypeError, KeyError, OSError) as erro:
		print(f"Nao foi possivel carregar os dados: {erro}")
		service = SistemaService(diretorio_dados=None)

	while True:
		mostrar_menu()

		try:
			opcao = ler_inteiro("Escolha uma opcao: ")
			if opcao == 0:
				print("Sistema encerrado.")
				break

			executar_opcao(opcao, service)
		except (ValueError, TypeError, IndexError, KeyError, OSError) as erro:
			print(f"Erro: {erro}")


if __name__ == "__main__":
	main()