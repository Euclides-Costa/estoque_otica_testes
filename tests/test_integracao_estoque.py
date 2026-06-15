from src.estoque import Estoque
from src.produto import Produto


def test_cadastrar_produto_integracao():

    estoque = Estoque()

    produto = Produto(
        "INT001",
        "Óculos",
        "RayBan",
        "RB001",
        "Preto",
        "0","0","0",
        "Metal",
        100,
        200,
        5,
        10
    )

    estoque.cadastrar_produto(produto)

    estoque.banco.cursor.execute(
        """
        SELECT sku
        FROM produtos
        WHERE sku = ?
        """,
        ("INT001",)
    )

    resultado = estoque.banco.cursor.fetchone()

    assert resultado[0] == "INT001" 