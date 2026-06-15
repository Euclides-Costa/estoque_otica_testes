import bcrypt
from src.banco import Banco

class Usuario:

    def __init__(self):
        self.banco = Banco()

    # --------------------------
    # CADASTRAR
    # --------------------------

    def cadastrar(self, usuario, senha):

        senha_hash = bcrypt.hashpw(
            senha.encode(),
            bcrypt.gensalt()
        ).decode()

        try:

            self.banco.cursor.execute("""
            INSERT INTO usuarios(usuario, senha)
            VALUES(?, ?)
            """, (usuario, senha_hash))

            self.banco.conexao.commit()

            print("Usuário cadastrado!")

        except:
            print("Usuário já existe!")

    # --------------------------
    # LOGIN
    # --------------------------

    def login(self, usuario, senha):

        self.banco.cursor.execute("""
        SELECT senha
        FROM usuarios
        WHERE usuario = ?
        """, (usuario,))

        resultado = self.banco.cursor.fetchone()

        if resultado:

            senha_hash = resultado[0]

            if bcrypt.checkpw(
                senha.encode(),
                senha_hash.encode()
            ):
                return True

        return False