from tests.fixtures import restaurantes_fixture, restaurantes_data_fixture
from components.restaurantes import Restaurantes
from components.restaurante import Restaurante


def test_restaurantes_lista_vazia() -> None:
    """Teste para verificar se a classe Restaurantes lida corretamente com uma lista vazia de restaurantes.
    """
    dados_vazios = {"restaurants": []}
    restaurantes_obj = Restaurantes(dados_vazios)
    assert restaurantes_obj._lista_de_restaurantes == []
