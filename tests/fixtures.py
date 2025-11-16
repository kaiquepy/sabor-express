from components.cardapio.prato import Prato
from components.cardapio.sobremesa import Sobremesa
from components.cardapio.bebida import Bebida
from components.restaurante import Restaurante
from components.restaurantes import Restaurantes
from components.sabor_express import SaborExpress
import pytest


@pytest.fixture
def sabor_express_object_fixture() -> SaborExpress:
    """Fixture que retorna um objeto SaborExpress para testes.

    Returns:
        SaborExpress: Um objeto SaborExpress com restaurantes pré-definidos para testes.
    """
    sabor_express_mock = SaborExpress()
    sabor_express_mock._restaurantes = Restaurantes({
            "restaurants": [
                {
                    "name": "restaurante 1",
                    "category": "tradicional",
                    "menu": [
                        {
                            "Item": "Item 1",
                            "Price": 5,
                            "Description": "An item 1"
                        },
                        {
                            "Item": "Item 2",
                            "Price": 10,
                            "Description": "An item 2"
                        },
                        {
                            "Item": "Item 1",
                            "Price": 6,
                            "Description": "An item 3"
                        }
                    ],
                    "ratings": {
                        "average": 3,
                        "individual_ratings": [
                            {
                                "rating": 3,
                                "description": "Don't like it that much"
                            }
                        ]
                    }
                },
                {
                    "name": "restaurante 2",
                    "category": "tradicional",
                    "menu": [
                        {
                            "Item": "Item 1",
                            "Price": 5,
                            "Description": "An item 1"
                        },
                        {
                            "Item": "Item 2",
                            "Price": 10,
                            "Description": "An item 2"
                        },
                        {
                            "Item": "Item 1",
                            "Price": 6,
                            "Description": "An item 3"
                        }
                    ],
                    "ratings": {
                        "average": 3,
                        "individual_ratings": [
                            {
                                "rating": 3,
                                "description": "Don't like it that much"
                            }
                        ]
                    }
                }
            ]
        })

    return sabor_express_mock


@pytest.fixture
def sobremesa_fixture() -> Sobremesa:
    """Fixture que retorna um objeto Sobremesa para testes.

    Returns:
        Sobremesa: Um objeto Sobremesa com nome "Sorvete", preço 100, tipo "Gelados" e tamanho "500ml".
    """
    return Sobremesa(
        nome="Sorvete",
        preco=100,
        tipo="Gelados",
        tamanho="500ml"
    )


@pytest.fixture
def prato_fixture() -> Prato:
    """Fixture que retorna um objeto Prato para testes.

    Returns:
        Prato: Um objeto Prato com nome "Feijoada", preço 100.0 e descrição "Deliciosa feijoada".
    """
    return Prato(nome="Feijoada", preco=100.0, descricao="Deliciosa feijoada")


@pytest.fixture
def bebida_fixture() -> Bebida:
    """Fixture que retorna um objeto Bebida para testes.

    Returns:
        Bebida: Um objeto Bebida com nome "Suco", preço 50.0 e tamanho "500ml".
    """
    return Bebida(nome="Suco", preco=50.0, tamanho="500ml")


@pytest.fixture
def restaurantes_data_fixture(restaurante_data_fixture: dict) -> dict:
    """Fixture que retorna um dicionário com dados de restaurantes para testes.

    Args:
        restaurante_data_fixture (dict): Dicionário com os dados de um restaurante.

    Returns:
        dict: Dicionário com a chave ``restaurants`` contendo uma lista com os dados de restaurantes.
    """
    return {"restaurants": [restaurante_data_fixture]}


@pytest.fixture
def restaurantes_fixture(restaurantes_data_fixture: dict) -> Restaurantes:
    """Fixture que retorna um objeto Restaurantes para testes.

    Args:
        restaurantes_data_fixture (dict): Dicionário com os dados de restaurantes.

    Returns:
        Restaurantes: Um objeto Restaurantes instanciado com os dados fornecidos.
    """
    return Restaurantes(restaurantes_data_fixture)


@pytest.fixture
def restaurante_data_fixture() -> dict:
    """Fixture que retorna um dicionário com dados de um restaurante para testes.
    
    Returns:
        dict: Dicionário com os dados de um restaurante.
    """
    return {
        "name": "Restaurante X",
        "category": "caseira",
        "menu": [
            {"Item": "Feijoada", "Price": 100.0, "Description": "Deliciosa feijoada"},
            {"Item": "Suco", "Price": 50.0, "Size": "500ml", "tipo": "Bebida"},
            {"Item": "Sorvete", "Price": 80.0, "Type": "Gelado", "Size": "300ml", "tipo": "Sobremesa"},
        ],
        "ratings": {
            "average": 4,
            "individual_ratings": [
                {"rating": 4, "description": "Muito bom"},
            ],
        },
    }


@pytest.fixture
def restaurante_fixture(restaurante_data_fixture: dict) -> Restaurante:
    """Fixture que retorna um objeto Restaurante para testes.

    Args:
        restaurante_data_fixture (dict): Dicionário com os dados de um restaurante.

    Returns:
        Restaurante: Um objeto Restaurante instanciado com os dados fornecidos.
    """
    return Restaurante(
        nome=restaurante_data_fixture["name"],
        categoria=restaurante_data_fixture["category"],
        cardapio=restaurante_data_fixture["menu"],
        avaliacoes=restaurante_data_fixture["ratings"],
    )
