from .item_cardapio import ItemCardapio


class Bebida(ItemCardapio):
    """Classe que representa um item do tipo Bebida.
    """
    def __init__(self, nome: str, preco: float, tamanho: str) -> None:
        """Inicializa um item do tipo Bebida.

        Args:
            nome (str): Nome da bebida.
            preco (float): Preço da bebida.
            tamanho (str): Tamanho da bebida.
        """
        super().__init__(nome, preco)
        self.tamanho = tamanho

    def aplicar_desconto(self) -> None:
        """Aplica um desconto de 8% no preço da bebida.
        """
        self._preco -= (self._preco * 0.08)
