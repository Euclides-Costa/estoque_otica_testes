from datetime import datetime

class Produto:
    def __init__(self, sku, tipo, marca, modelo, cor,
                 grau_esferico, grau_cilindrico, eixo,
                 material, preco_custo, preco_venda,
                 quantidade_minima, quantidade=0,
                 validade=None, lote=None):

        self.sku = sku
        self.tipo = tipo
        self.marca = marca
        self.modelo = modelo
        self.cor = cor

        self.grau_esferico = grau_esferico
        self.grau_cilindrico = grau_cilindrico
        self.eixo = eixo

        self.material = material
        self.preco_custo = preco_custo
        self.preco_venda = preco_venda

        self.quantidade_minima = quantidade_minima
        self.quantidade = quantidade

        self.validade = validade
        self.lote = lote

    def adicionar_estoque(self, qtd):
        self.quantidade += qtd

    def remover_estoque(self, qtd):
        if qtd <= self.quantidade:
            self.quantidade -= qtd
        else:
            print("Estoque insuficiente!")

    def verificar_validade(self):
        if self.validade:
            hoje = datetime.now().date()
            dias = (self.validade - hoje).days

            if dias <= 30:
                return True

        return False

    def exibir(self):
        print(f"""
SKU: {self.sku}
Tipo: {self.tipo}
Marca: {self.marca}
Modelo: {self.modelo}
Quantidade: {self.quantidade}
Preço Venda: R$ {self.preco_venda}
""")