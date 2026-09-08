def buscar_produto_por_codigo(produtos_ordenados, codigo):
    codigo = int(codigo)
    inicio = 0
    fim = len(produtos_ordenados) - 1
    while inicio <= fim:
        meio = (inicio + fim) // 2
        produto = produtos_ordenados[meio]
        if produto.codigo == codigo:
            return produto
        if codigo < produto.codigo:
            fim = meio - 1
        else:
            inicio = meio + 1
    return None
