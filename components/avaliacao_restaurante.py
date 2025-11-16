class AvaliacaoRestaurante:
    """Classe que representa a avaliação de um restaurante.
    """
    def __init__(self, media: float, avaliacoes_individuais: list) -> None:
        """Inicializa uma instância da classe AvaliacaoRestaurante.

        Args:
            media (float): Média das avaliações do restaurante.
            avaliacoes_individuais (list): Lista de avaliações individuais do restaurante.
        """
        self.media = media
        self.avaliacoes_individuais = avaliacoes_individuais
