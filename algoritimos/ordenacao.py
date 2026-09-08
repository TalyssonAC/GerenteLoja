def ordenar_produtos_por_id(produtos):
    """Insertion Sort sem usar sort() ou sorted()."""
    produtos_ordenados = list(produtos)
    for indice in range(1, len(produtos_ordenados)):
        atual = produtos_ordenados[indice]
        anterior = indice - 1
        while anterior >= 0 and produtos_ordenados[anterior].codigo > atual.codigo:
            produtos_ordenados[anterior + 1] = produtos_ordenados[anterior]
            anterior -= 1
        produtos_ordenados[anterior + 1] = atual
    return produtos_ordenados
