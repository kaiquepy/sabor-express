from tests.fixtures import prato_fixture


def test_prato_str(prato_fixture) -> None:
    """Verifica se a conversão para string retorna o nome do prato."""
    prato = prato_fixture
    assert str(prato) == "Feijoada"


def test_prato_aplicar_desconto(prato_fixture) -> None:
    """Garante que o desconto de 5% é aplicado corretamente ao preço."""
    prato = prato_fixture
    preco_original = prato._preco
    prato.aplicar_desconto()
    # 5% de 100.0 = 5.0, preço final esperado = 95.0
    assert prato._preco == preco_original * 0.95
