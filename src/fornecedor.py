class Fornecedor:
    def __init__(self, nome, cnpj, contato, prazo_entrega):
        self.nome = nome
        self.cnpj = cnpj
        self.contato = contato
        self.prazo_entrega = prazo_entrega

    def exibir(self):
        print(f"""
Fornecedor: {self.nome}
CNPJ: {self.cnpj}
Contato: {self.contato}
Prazo de entrega: {self.prazo_entrega} dias
""")