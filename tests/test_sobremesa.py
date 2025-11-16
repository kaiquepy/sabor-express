from tests.fixtures import sobremesa_fixture

def test_sobremesa_str(sobremesa_fixture) -> None:
    """Teste para verificar a conversão para string de uma sobremesa.

    Args:
        sobremesa_fixture (Sobremesa): Fixture da sobremesa para o teste.
    """
    sobremesa = sobremesa_fixture
    assert str(sobremesa) == "Sorvete"

def teste_aplicar_desconto_sobremesa(sobremesa_fixture) -> None:
    """Teste para verificar a aplicação de desconto em uma sobremesa.

    Args:
        sobremesa_fixture (Sobremesa): Fixture da sobremesa para o teste.
    """
    sobremesa = sobremesa_fixture
    sobremesa.aplicar_desconto()

    assert sobremesa._preco == 85
