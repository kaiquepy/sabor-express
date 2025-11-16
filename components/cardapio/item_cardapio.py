from abc import ABC, abstractmethod


class ItemCardapio(ABC):
    """Classe abstrata que representa um item do cardápio.
    """
    def __init__(self, nome: str, preco: float) -> None:
        """Inicializa um item do cardápio.

        Args:
            nome (str): Nome do item.
            preco (float): Preço do item.
        """
        self._nome = nome
        self._preco = preco

    def __str__(self) -> str:
        """Retorna a representação em string do item do cardápio.

        Returns:
            str: Nome do item.
        """
        return f'{self._nome}'

    @abstractmethod
    def aplicar_desconto(self) -> None:
        """Aplica um desconto no preço do item do cardápio.
        """
        pass
