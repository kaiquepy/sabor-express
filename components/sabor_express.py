import json

from components.cardapio.item_cardapio import ItemCardapio
from components.restaurante import Restaurante
from .restaurantes import Restaurantes


class SaborExpress:
    """Classe principal do programa SaborExpress.
    """
    def __init__(self) -> None:
        """Inicializa uma instância da classe SaborExpress.
        """
        self._restaurantes: list[Restaurante] = None

    def exibir_nome_do_programa(self) -> None:
        """Exibe o nome do programa SaborExpress na tela.
        """
        print("""
        ░██████╗░█████╗░██████╗░░█████╗░██████╗░  ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
        ██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
        ╚█████╗░███████║██████╦╝██║░░██║██████╔╝  █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
        ░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗  ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
        ██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║  ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
        ╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░
        """)

    def obter_restaurantes(self) -> None:
        """Obtém a lista de restaurantes a partir do arquivo JSON e inicializa a instância de Restaurantes.
        """
        with open("data/restaurants_db.json") as file:
            restaurants_data = json.load(file)

        restaurantes = Restaurantes(restaurants_data)

        self._restaurantes = restaurantes

    def escolher_restaurante(self, restaurante_escolhido_index: int) -> Restaurante:
        """Seleciona um restaurante com base no índice fornecido.

        Args:
            restaurante_escolhido_index (int): Índice do restaurante escolhido.

        Returns:
            Restaurante: Instância do restaurante selecionado.
        """
        restaurante_escolhido: Restaurante = self._restaurantes._lista_de_restaurantes[restaurante_escolhido_index - 1]

        return restaurante_escolhido

    def escolher_pedido(self, restaurante_escolhido: Restaurante, pedido_escolhido_index: int) -> ItemCardapio:
        """Seleciona um item do cardápio do restaurante com base no índice fornecido.

        Args:
            restaurante_escolhido (Restaurante): Restaurante escolhido.
            pedido_escolhido_index (int): Índice do pedido escolhido.

        Returns:
            ItemCardapio: Item do cardápio selecionado.
        """
        return restaurante_escolhido._cardapio[pedido_escolhido_index - 1]

    def calcular_preco(self, pedido_escolhido: ItemCardapio, tem_desconto: str) -> None:
        """Calcula o preço do pedido, aplicando desconto se aplicável.

        Args:
            pedido_escolhido (ItemCardapio): Item do cardápio escolhido.
            tem_desconto (str): Indica se há desconto ("S" para sim, "N" para não).
        """
        if tem_desconto == "S":
            pedido_escolhido.aplicar_desconto()

        print(f"O pedido ficou por {pedido_escolhido._preco:.2f}")

    def avaliar_pedido(self, idx: int) -> None:
        """Permite que o usuário avalie o pedido feito.

        Args:
            idx (int): Índice do restaurante avaliado.
        """
        nota_avaliacao = int(input("Nota (1 a 5):"))
        descricao_avaliacao = input("Comentário:")

        self._restaurantes._lista_de_restaurantes[idx]._avaliacoes.avaliacoes_individuais.append({
            "rating": nota_avaliacao,
            "description": descricao_avaliacao
        })

        self._restaurantes._lista_de_restaurantes[idx].calcular_media_avaliacoes

        nova_avaliacao = {
            "average": self._restaurantes._lista_de_restaurantes[idx]._avaliacoes.media,
            "individual_ratings": self._restaurantes._lista_de_restaurantes[idx]._avaliacoes.avaliacoes_individuais,
        }

        with open("nova_avaliacao.json", "w", encoding="utf-8") as file:
            json.dump({f"{self._restaurantes._lista_de_restaurantes[idx]._nome}": nova_avaliacao}, file, ensure_ascii=False, indent=4)

        print("\nObrigado pela avaliação!")

    def iniciar_interface_de_pedidos(self) -> None:
        """Inicia a interface de pedidos do SaborExpress.
        """
        # Mostra lista de restaurantes e obtém o escolhido
        print("Digite o número do restaurante no qual deseja fazer o pedido.")

        for idx, restaurante in enumerate(self._restaurantes._lista_de_restaurantes):
            print(f"{idx + 1}" + f" - {restaurante._nome}" )

        restaurante_escolhido_index = int(input("Restaurante escolhido: "))

        restaurante_escolhido = self.escolher_restaurante(restaurante_escolhido_index)

        # Mostra lista de pedidos do restaurante e obtém o escolhido
        print("\nDigite o número do item que deseja pedir.")
        restaurante_escolhido.exibir_cardapio
        pedido_escolhido_index = int(input("Pedido escolhido: "))

        pedido_escolhido = self.escolher_pedido(restaurante_escolhido, pedido_escolhido_index)

        # Calcula o preço do pedido após verificar se tem desconto ou não
        tem_desconto = input("Você tem cupom de desconto? (S/N)")

        self.calcular_preco(pedido_escolhido, tem_desconto)

        # Permite que o usuário faça uma avaliação
        deseja_avaliar = input("Deseja fazer uma avaliação? (S/N)")

        if deseja_avaliar == "S":
            self.avaliar_pedido(restaurante_escolhido_index)

        print("\nPedido finalizado.")
