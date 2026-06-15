from src.sistema import Sistema
from src.autenticacao import Usuario

auth = Usuario()

while True:

    print("""
==============================
 SISTEMA DE ESTOQUE - ÓTICA
==============================

1 - Criar Conta
2 - Fazer Login
0 - Sair
""")

    opcao = input("Escolha: ")

    # --------------------------
    # CRIAR CONTA
    # --------------------------

    if opcao == "1":

        usuario = input("Novo usuário: ")
        senha = input("Nova senha: ")

        auth.cadastrar(usuario, senha)

    # --------------------------
    # LOGIN
    # --------------------------

    elif opcao == "2":

        usuario = input("Usuário: ")
        senha = input("Senha: ")

        if auth.login(usuario, senha):

            print("\nLogin realizado!\n")

            sistema = Sistema()
            sistema.menu()

        else:
            print("\nUsuário ou senha inválidos!\n")

    # --------------------------
    # SAIR
    # --------------------------

    elif opcao == "0":
        print("Sistema encerrado!")
        break

    else:
        print("Opção inválida!")