from src.produto import Produto
from src.fornecedor import Fornecedor
from src.estoque import Estoque
from src.utils import converter_data

class Sistema:

    def __init__(self):
        self.estoque = Estoque()

    def menu(self):

        while True:

            print("""
==============================
 SISTEMA DE ESTOQUE - ÓTICA
==============================

1 - Cadastrar Produto
2 - Listar Produtos
3 - Entrada de Produto
4 - Saída de Produto
5 - Histórico
6 - Verificar Validade
7 - Cadastrar Fornecedor
8 - Listar Fornecedores
0 - Sair
""")

            opcao = input("Escolha: ")

            # --------------------
            # CADASTRAR PRODUTO
            # --------------------

            if opcao == "1":

                sku = input("SKU: ")
                tipo = input("Tipo: ")
                marca = input("Marca: ")
                modelo = input("Modelo: ")
                cor = input("Cor: ")

                grau_esferico = input("Grau esférico: ")
                grau_cilindrico = input("Grau cilíndrico: ")
                eixo = input("Eixo: ")

                material = input("Material: ")

                preco_custo = float(
                    input("Preço custo: ")
                )

                preco_venda = float(
                    input("Preço venda: ")
                )

                qtd_min = int(
                    input("Quantidade mínima: ")
                )

                quantidade = int(
                    input("Quantidade inicial: ")
                )

                validade = input(
                    "Validade (dd/mm/aaaa ou vazio): "
                )

                lote = input("Lote: ")

                if validade != "":
                    validade = converter_data(validade)
                else:
                    validade = None

                produto = Produto(
                    sku,
                    tipo,
                    marca,
                    modelo,
                    cor,
                    grau_esferico,
                    grau_cilindrico,
                    eixo,
                    material,
                    preco_custo,
                    preco_venda,
                    qtd_min,
                    quantidade,
                    validade,
                    lote
                )

                self.estoque.cadastrar_produto(produto)

                print("Produto cadastrado!")

            # --------------------
            # LISTAR
            # --------------------

            elif opcao == "2":
                self.estoque.listar_produtos()

            # --------------------
            # ENTRADA
            # --------------------

            elif opcao == "3":

                sku = input("SKU: ")
                qtd = int(input("Quantidade: "))
                usuario = input("Usuário: ")
                motivo = input("Motivo: ")

                self.estoque.entrada_produto(
                    sku,
                    qtd,
                    usuario,
                    motivo
                )

            # --------------------
            # SAÍDA
            # --------------------

            elif opcao == "4":

                sku = input("SKU: ")
                qtd = int(input("Quantidade: "))
                usuario = input("Usuário: ")
                motivo = input("Motivo: ")

                self.estoque.saida_produto(
                    sku,
                    qtd,
                    usuario,
                    motivo
                )

            # --------------------
            # HISTÓRICO
            # --------------------

            elif opcao == "5":
                self.estoque.historico()

            # --------------------
            # VALIDADE
            # --------------------

            elif opcao == "6":
                self.estoque.verificar_validade()

            # --------------------
            # FORNECEDOR
            # --------------------

            elif opcao == "7":

                nome = input("Nome: ")
                cnpj = input("CNPJ: ")
                contato = input("Contato: ")
                prazo = int(
                    input("Prazo entrega: ")
                )

                fornecedor = Fornecedor(
                    nome,
                    cnpj,
                    contato,
                    prazo
                )

                self.estoque.cadastrar_fornecedor(
                    fornecedor
                )

                print("Fornecedor cadastrado!")

            elif opcao == "8":
                self.estoque.listar_fornecedores()

            # --------------------
            # SAIR
            # --------------------

            elif opcao == "0":
                print("Sistema encerrado!")
                break

            else:
                print("Opção inválida!")