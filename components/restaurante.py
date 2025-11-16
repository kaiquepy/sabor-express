from .avaliacao_restaurante import AvaliacaoRestaurante
from .cardapio.bebida import Bebida
from .cardapio.item_cardapio import ItemCardapio
from .cardapio.prato import Prato
from .cardapio.sobremesa import Sobremesa


class Restaurante:
    """Representa um restaurante com seu cardápio, avaliações e estado ativo/inativo.
    """
    def __init__(self, nome: str, categoria: str, cardapio: list, avaliacoes: dict) -> None:
        """Inicializa uma instância de Restaurante.

        Args:
            nome (str): Nome do restaurante.
            categoria (str): Categoria do restaurante.
            cardapio (list): Lista de itens do cardápio.
            avaliacoes (dict): Dicionário contendo avaliações do restaurante.
        """
        self._nome = nome.title()
        self._categoria = categoria.upper()
        self._cardapio = self.processar_cardapio(cardapio)
        self._ativo = False
        self._avaliacoes = AvaliacaoRestaurante(
            media=avaliacoes["average"],
            avaliacoes_individuais=avaliacoes["individual_ratings"]
        )

    def __str__(self) -> str:
        """Retorna uma representação textual da instância.

        Returns:
            str: Representação textual do restaurante.
        """
        return f'{self._nome} | {self._categoria}'

    @property
    def ativo(self) -> str:
        """Retorna um símbolo verde de verificação se restaurante ativo e um x vermelho se não.

        Returns:
            str: Símbolo indicando o estado do restaurante.
        """
        return '✅' if self._ativo else '❌'

    @property
    def exibir_cardapio(self) -> None:
        """Exibe o cardápio do restaurante formatado.
        """
        print(f'\nCardapio do restaurante {self._nome}\n')

        for i, item in enumerate(self._cardapio, start=1):
            if hasattr(item, 'descricao'):
                mensagem = f'{i}. Nome: {item._nome.ljust(25)} | Preço: R${str(item._preco).ljust(20)} | Descrição: {item.descricao}'
                print(mensagem)
            else:
                mensagem = f'{i}. Nome: {item._nome.ljust(25)} | Preço: R${str(item._preco).ljust(20)} | Tamanho: {item.tamanho}'
                print(mensagem)

    def calcular_media_avaliacoes(self) -> None:
        """Calcula a média das avaliações do restaurante com base nas avaliações individuais.
        """
        soma = 0
        for avaliacao in self._avaliacoes.avaliacoes_individuais:
            soma += avaliacao["rating"]

        self._avaliacoes.media = soma / len(self._avaliacoes.avaliacoes_individuais)

    def processar_cardapio(self, cardapio_data: list[dict]) -> list[ItemCardapio]:
        """Processa os dados do cardápio e cria instâncias dos itens correspondentes.

        Args:
            cardapio_data (list[dict]): Lista de dicionários contendo os dados do cardápio.

        Returns:
            list[ItemCardapio]: Lista de instâncias dos itens do cardápio.
        """
        cardapio = []

        for item in cardapio_data:
            if "tipo" in item:
                if item["tipo"] == "Bebida":
                    Bebida(
                        nome=item["Item"],
                        preco=item["Price"],
                        tamanho=item["Size"]
                    )
                elif item["tipo"] == "Sobremesa":
                    Sobremesa(
                        nome=item["Item"],
                        preco=item["Price"],
                        tipo=item["Type"],
                        tamanho=item["Size"]
                    )
            else:
                cardapio.append(
                    Prato(
                        nome=item["Item"],
                        preco=item["Price"],
                        descricao=item["Description"]
                    )
                )

        return cardapio

    def alternar_estado(self) -> None:
        """Altera o estado do restaurante entre ativo e inativo.
        """
        self._ativo = not self._ativo

    def adicionar_no_cardapio(self, item: ItemCardapio) -> None:
        """Adiciona um item ao cardápio do restaurante.

        Args:
            item (ItemCardapio): Item a ser adicionado no cardápio.
        """
        if isinstance(item, ItemCardapio):
            self._cardapio.append(item)
