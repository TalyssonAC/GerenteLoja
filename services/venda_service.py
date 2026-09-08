from models.item_venda import ItemVenda
from models.venda import Venda


class VendaService:
    def __init__(
        self,
        venda_repository,
        cliente_repository,
        produto_repository,
        estoque_service,
    ):
        self._venda_repository = venda_repository
        self._cliente_repository = cliente_repository
        self._produto_repository = produto_repository
        self._estoque_service = estoque_service

    def registrar(self, codigo, codigo_cliente, itens, data=None):
        if self._cliente_repository.buscar_por_codigo(codigo_cliente) is None:
            raise ValueError("Cliente nao encontrado.")

        if self.buscar_por_codigo(codigo) is not None:
            raise ValueError("Ja existe uma venda com esse codigo.")

        if itens is None:
            raise ValueError("A venda deve possuir pelo menos um item.")

        venda = Venda(codigo, codigo_cliente, data)

        for codigo_produto, quantidade in itens:
            produto = self._produto_repository.buscar_por_codigo(codigo_produto)

            if produto is None:
                raise ValueError("Produto nao encontrado.")

            item = ItemVenda(codigo, codigo_produto, quantidade, produto.preco)
            venda.adicionar_item(item)

        if not venda.possui_itens():
            raise ValueError("A venda deve possuir pelo menos um item.")

        self._validar_estoque_disponivel(venda)
        self._venda_repository.adicionar(venda)

        for item in venda.itens:
            codigo_movimentacao = self._estoque_service.proximo_codigo_movimentacao()
            self._estoque_service.registrar_saida(
                codigo_movimentacao,
                item.codigo_produto,
                item.quantidade,
                venda.data,
            )

        return venda

    def buscar_por_codigo(self, codigo):
        return self._venda_repository.buscar_por_codigo(codigo)

    def listar(self):
        return self._venda_repository.listar()

    def listar_por_cliente(self, codigo_cliente):
        return self._venda_repository.listar_por_cliente(codigo_cliente)

    def _validar_estoque_disponivel(self, venda):
        for item in venda.itens:
            produto = self._produto_repository.buscar_por_codigo(item.codigo_produto)

            if produto.quantidade_estoque < item.quantidade:
                raise ValueError(
                    f"Estoque insuficiente para o produto {produto.codigo}."
                )
