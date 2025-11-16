from .item_cardapio import ItemCardapio


class Sobremesa(ItemCardapio):
    """Classe que representa um item do tipo Sobremesa.
    """
    def __init__(self, nome: str, preco: float, tipo: str, tamanho: str) -> None:
        """Inicializa um item do tipo Sobremesa.

        Args:
            nome (str): Nome da sobremesa.
            preco (float): Preço da sobremesa.
            tipo (str): Tipo da sobremesa.
            tamanho (str): Tamanho da sobremesa.
        """
        super().__init__(nome, preco)
        self.tipo = tipo
        self.tamanho = tamanho

    def aplicar_desconto(self) -> None:
        """Aplica um desconto de 15% no preço da sobremesa.
        """
        self._preco -= (self._preco * 0.15)
