from src.estoque import Estoque


def test_entrada_produto_integracao():

    estoque = Estoque()

    estoque.entrada_produto(
        "INT001",
        5,
        "admin",
        "Reposição"
    )

    estoque.banco.cursor.execute(
        """
        SELECT tipo
        FROM movimentacoes
        WHERE sku = ?
        ORDER BY id DESC
        LIMIT 1
        """,
        ("INT001",)
    )

    resultado = estoque.banco.cursor.fetchone()

    assert resultado[0] == "ENTRADA"