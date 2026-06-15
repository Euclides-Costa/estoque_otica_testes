import pytest
from datetime import date, timedelta
from src.produto import Produto


@pytest.mark.parametrize(
    "quantidade_inicial,adicao,resultado",
    [
        (10, 5, 15),
        (0, 20, 20),
        (50, 1, 51)
    ]
)
def test_adicionar_estoque_parametrizado(
    quantidade_inicial,
    adicao,
    resultado
):
    produto = Produto(
        "SKU1","Óculos","Marca","Modelo","Preto",
        "0","0","0","Metal",
        100,200,5,
        quantidade=quantidade_inicial
    )

    produto.adicionar_estoque(adicao)

    assert produto.quantidade == resultado


@pytest.mark.parametrize(
    "dias_para_vencer,esperado",
    [
        (10, True),
        (30, True),
        (60, False)
    ]
)
def test_validade_parametrizado(
    dias_para_vencer,
    esperado
):
    produto = Produto(
        "SKU2","Lente","Marca","Modelo","Transparente",
        "0","0","0","Resina",
        50,100,1,
        validade=date.today() +
        timedelta(days=dias_para_vencer)
    )

    assert produto.verificar_validade() == esperado