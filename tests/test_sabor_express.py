from tests.fixtures import sabor_express_object_fixture

def teste_escolher_restaurante(sabor_express_object_fixture) -> None:
    """Teste para verificar a escolha de um restaurante.

    Args:
        sabor_express_object_fixture (SaborExpress): Fixture do objeto SaborExpress para o teste.
    """
    sabor_express = sabor_express_object_fixture
    restaurante_escolhido = sabor_express.escolher_restaurante(1)

    assert restaurante_escolhido._nome == "Restaurante 1"

def teste_escolher_pedido(sabor_express_object_fixture) -> None:
    """Teste para verificar a escolha de um pedido em um restaurante.

    Args:
        sabor_express_object_fixture (SaborExpress): Fixture do objeto SaborExpress para o teste.
    """
    sabor_express = sabor_express_object_fixture
    restaurante_escolhido = sabor_express.escolher_restaurante(1)

    pedido_escolhido = sabor_express.escolher_pedido(restaurante_escolhido, 1)

    assert pedido_escolhido._nome == "Item 1"
