from banco import Banco
from datetime import datetime

class Estoque:

    def __init__(self):

        self.banco = Banco()

    # --------------------------
    # CADASTRAR PRODUTO
    # --------------------------

    def cadastrar_produto(self, produto):

        self.banco.cursor.execute("""
        INSERT INTO produtos(
            sku, tipo, marca, modelo, cor,
            grau_esferico, grau_cilindrico,
            eixo, material,
            preco_custo, preco_venda,
            quantidade_minima,
            quantidade,
            validade,
            lote
        )
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (

            produto.sku,
            produto.tipo,
            produto.marca,
            produto.modelo,
            produto.cor,
            produto.grau_esferico,
            produto.grau_cilindrico,
            produto.eixo,
            produto.material,
            produto.preco_custo,
            produto.preco_venda,
            produto.quantidade_minima,
            produto.quantidade,
            str(produto.validade),
            produto.lote
        ))

        self.banco.conexao.commit()

        print("Produto cadastrado!")

    # --------------------------
    # LISTAR PRODUTOS
    # --------------------------

    def listar_produtos(self):

        self.banco.cursor.execute("""
        SELECT sku, modelo, marca,
               quantidade, preco_venda
        FROM produtos
        """)

        produtos = self.banco.cursor.fetchall()

        if len(produtos) == 0:
            print("\nNenhum produto cadastrado!\n")
            return

        print("\n===== PRODUTOS =====\n")

        for produto in produtos:

            print(f"""
SKU: {produto[0]}
Modelo: {produto[1]}
Marca: {produto[2]}
Quantidade: {produto[3]}
Preço: R$ {produto[4]}
""")

    # --------------------------
    # ENTRADA
    # --------------------------

    def entrada_produto(self,
                         sku,
                         qtd,
                         usuario,
                         motivo):

        self.banco.cursor.execute("""
        UPDATE produtos
        SET quantidade = quantidade + ?
        WHERE sku = ?
        """, (qtd, sku))

        self.banco.cursor.execute("""
        INSERT INTO movimentacoes(
            sku, tipo, quantidade,
            usuario, motivo, data
        )
        VALUES (?, ?, ?, ?, ?, ?)
        """, (
            sku,
            "ENTRADA",
            qtd,
            usuario,
            motivo,
            str(datetime.now())
        ))

        self.banco.conexao.commit()

        print("Entrada registrada!")

    # --------------------------
    # SAÍDA
    # --------------------------

    def saida_produto(self,
                      sku,
                      qtd,
                      usuario,
                      motivo):

        self.banco.cursor.execute("""
        UPDATE produtos
        SET quantidade = quantidade - ?
        WHERE sku = ?
        """, (qtd, sku))

        self.banco.cursor.execute("""
        INSERT INTO movimentacoes(
            sku, tipo, quantidade,
            usuario, motivo, data
        )
        VALUES (?, ?, ?, ?, ?, ?)
        """, (
            sku,
            "SAÍDA",
            qtd,
            usuario,
            motivo,
            str(datetime.now())
        ))

        self.banco.conexao.commit()

        print("Saída registrada!")

    # --------------------------
    # HISTÓRICO
    # --------------------------

    def historico(self):

        self.banco.cursor.execute("""
        SELECT sku, tipo,
               quantidade,
               usuario,
               motivo,
               data
        FROM movimentacoes
        """)

        movimentacoes = self.banco.cursor.fetchall()

        if len(movimentacoes) == 0:
            print("\nNenhuma movimentação!\n")
            return

        print("\n===== HISTÓRICO =====\n")

        for mov in movimentacoes:

            print(f"""
Produto SKU: {mov[0]}
Tipo: {mov[1]}
Quantidade: {mov[2]}
Usuário: {mov[3]}
Motivo: {mov[4]}
Data: {mov[5]}
""")

    # --------------------------
    # FORNECEDOR
    # --------------------------

    def cadastrar_fornecedor(self,
                             fornecedor):

        self.banco.cursor.execute("""
        INSERT INTO fornecedores(
            nome,
            cnpj,
            contato,
            prazo_entrega
        )
        VALUES (?, ?, ?, ?)
        """, (
            fornecedor.nome,
            fornecedor.cnpj,
            fornecedor.contato,
            fornecedor.prazo_entrega
        ))

        self.banco.conexao.commit()

        print("Fornecedor cadastrado!")

    def listar_fornecedores(self):

        self.banco.cursor.execute("""
        SELECT nome, cnpj,
               contato,
               prazo_entrega
        FROM fornecedores
        """)

        fornecedores = self.banco.cursor.fetchall()

        if len(fornecedores) == 0:
            print("\nNenhum fornecedor cadastrado!\n")
            return

        print("\n===== FORNECEDORES =====\n")

        for fornecedor in fornecedores:

            print(f"""
Nome: {fornecedor[0]}
CNPJ: {fornecedor[1]}
Contato: {fornecedor[2]}
Prazo: {fornecedor[3]} dias
""")

    # --------------------------
    # VALIDADE
    # --------------------------

    def verificar_validade(self):

        self.banco.cursor.execute("""
        SELECT modelo, validade
        FROM produtos
        WHERE validade IS NOT NULL
        """)

        produtos = self.banco.cursor.fetchall()

        if len(produtos) == 0:
            print("\nNenhum produto com validade!\n")
            return

        print("\n===== VALIDADES =====\n")

        for produto in produtos:

            print(f"""
Produto: {produto[0]}
Validade: {produto[1]}
""")