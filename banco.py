import sqlite3

class Banco:

    def __init__(self):
        self.conexao = sqlite3.connect("otica.db")
        self.cursor = self.conexao.cursor()

        self.criar_tabelas()

    def criar_tabelas(self):

        # --------------------------
        # USUÁRIOS
        # --------------------------

        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS usuarios(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            usuario TEXT UNIQUE,
            senha TEXT
        )
        """)

        # --------------------------
        # PRODUTOS
        # --------------------------

        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS produtos(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            sku TEXT UNIQUE,
            tipo TEXT,
            marca TEXT,
            modelo TEXT,
            cor TEXT,
            grau_esferico TEXT,
            grau_cilindrico TEXT,
            eixo TEXT,
            material TEXT,
            preco_custo REAL,
            preco_venda REAL,
            quantidade_minima INTEGER,
            quantidade INTEGER,
            validade TEXT,
            lote TEXT
        )
        """)

        # --------------------------
        # FORNECEDORES
        # --------------------------

        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS fornecedores(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT,
            cnpj TEXT,
            contato TEXT,
            prazo_entrega INTEGER
        )
        """)

        # --------------------------
        # MOVIMENTAÇÕES
        # --------------------------

        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS movimentacoes(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            sku TEXT,
            tipo TEXT,
            quantidade INTEGER,
            usuario TEXT,
            motivo TEXT,
            data TEXT
        )
        """)

        self.conexao.commit()