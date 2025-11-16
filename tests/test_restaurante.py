import pytest

from components.cardapio.prato import Prato
from components.cardapio.bebida import Bebida
from components.cardapio.sobremesa import Sobremesa
from components.restaurante import Restaurante
from tests.fixtures import restaurante_fixture, restaurante_data_fixture


def test_restaurante_normaliza_nome_categoria(restaurante_data_fixture) -> None:
    """Teste para verificar a normalização do nome e categoria do restaurante.

    Args:
        restaurante_data_fixture (dict): Fixture de dados do restaurante.
    """
    dados = restaurante_data_fixture.copy()
    dados["name"] = "bar da esquina"
    dados["category"] = "regional"
    r = Restaurante(
        nome=dados["name"],
        categoria=dados["category"],
        cardapio=dados["menu"],
        avaliacoes=dados["ratings"],
    )
    assert r._nome == "Bar Da Esquina"
    assert r._categoria == "REGIONAL"


def test_restaurante_alternar_estado(restaurante_fixture) -> None:
    """Teste para verificar a alternância do estado do restaurante.

    Args:
        restaurante_fixture (Restaurante): Fixture do objeto Restaurante.
    """

    assert restaurante_fixture.ativo == "❌"
    restaurante_fixture.alternar_estado()
    assert restaurante_fixture.ativo == "✅"
    restaurante_fixture.alternar_estado()
    assert restaurante_fixture.ativo == "❌"


def test_restaurante_calcular_media(restaurante_fixture) -> None:
    """Teste para verificar o cálculo da média das avaliações do restaurante.

    Args:
        restaurante_fixture (Restaurante): Fixture do objeto Restaurante.
    """
    restaurante = restaurante_fixture

    restaurante._avaliacoes.avaliacoes_individuais.append({"rating": 5, "description": "Ótimo"})
    restaurante.calcular_media_avaliacoes()
    assert restaurante._avaliacoes.media == pytest.approx((4 + 5) / 2)


def test_restaurante_adicionar_no_cardapio(restaurante_fixture) -> None:
    """Teste para verificar a adição de um item ao cardápio do restaurante.

    Args:
        restaurante_fixture (Restaurante): Fixture do objeto Restaurante.
    """
    restaurante = restaurante_fixture
    tamanho_anterior = len(restaurante._cardapio)
    novo_item = Prato(nome="Lasanha", preco=70.0, descricao="Caseira")
    restaurante.adicionar_no_cardapio(novo_item)
    assert len(restaurante._cardapio) == tamanho_anterior + 1
    assert restaurante._cardapio[-1] is novo_item

    tamanho_intermediario = len(restaurante._cardapio)
    restaurante.adicionar_no_cardapio(123)
    assert len(restaurante._cardapio) == tamanho_intermediario
