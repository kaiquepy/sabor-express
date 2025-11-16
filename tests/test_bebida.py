from tests.fixtures import bebida_fixture


def test_bebida_str(bebida_fixture) -> None:
    """Verifica se a conversão para string retorna o nome da bebida.

    Args:
        bebida_fixture (Bebida): Fixture da bebida.
    """
    bebida = bebida_fixture
    assert str(bebida) == "Suco"


def test_bebida_aplicar_desconto(bebida_fixture) -> None:
    """Aplica 8% de desconto e verifica se o novo preço está correto.

    Args:
        bebida_fixture (Bebida): Fixture da bebida.
    """
    bebida = bebida_fixture
    preco_original = bebida._preco
    bebida.aplicar_desconto()
    # 8% de 50.0 = 4.0, preço final esperado = 46.0
    assert bebida._preco == preco_original * 0.92
