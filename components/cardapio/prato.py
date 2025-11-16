from .item_cardapio import ItemCardapio


class Prato(ItemCardapio):
    """Classe que representa um item do tipo Prato.
    """
    def __init__(self, nome: str, preco: float, descricao: str) -> None:
        """Inicializa um item do tipo Prato.

        Args:
            nome (str): Nome do prato.
            preco (float): Preço do prato.
            descricao (str): Descrição do prato.
        """
        super().__init__(nome, preco)
        self.descricao = descricao

    def aplicar_desconto(self) -> None:
        """Aplica um desconto de 5% no preço do prato.
        """
        self._preco -= (self._preco * 0.05)
