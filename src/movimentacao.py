from datetime import datetime

class Movimentacao:
    def __init__(self, produto, tipo, quantidade,
                 usuario, motivo):

        self.produto = produto
        self.tipo = tipo
        self.quantidade = quantidade
        self.usuario = usuario
        self.motivo = motivo
        self.data = datetime.now()

    def exibir(self):
        print(f"""
Data: {self.data}
Produto: {self.produto.modelo}
Tipo: {self.tipo}
Quantidade: {self.quantidade}
Usuário: {self.usuario}
Motivo: {self.motivo}
""")