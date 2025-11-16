from .restaurante import Restaurante


class Restaurantes:
    """Representa uma coleção de restaurantes.
    """
    def __init__(self, restaurantes_data: dict) -> None:
        """Inicializa uma instância da classe Restaurantes.

        Args:
            restaurantes_data (dict): Dados dos restaurantes.
        """
        self._lista_de_restaurantes = self.obter_restaurantes(restaurantes_data)

    def obter_restaurantes(self, restaurantes_data: dict) -> list[Restaurante]:
        """Retorna a lista de restaurantes a partir dos dados fornecidos.

        Args:
            restaurantes_data (dict): Dados dos restaurantes.

        Returns:
            list[Restaurante]: Lista de objetos Restaurante.
        """
        lista_de_restaurantes = []
        for restaurante in restaurantes_data["restaurants"]:
            lista_de_restaurantes.append(
                Restaurante(
                    nome=restaurante["name"],
                    categoria=restaurante["category"],
                    cardapio=restaurante["menu"],
                    avaliacoes=restaurante["ratings"]
                )
            )
        return lista_de_restaurantes
