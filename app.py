# Entrada/Saída de dado
# -----------------------
# print() -> Saída de dado
# input() -> Entrada de dado

# Variável
# ----------
# nome_da_variavel -> usa-se snake_case para separar palavra

# Casting (conversão)
# ---------------------
# int(valor), float(valor), str(valor), bool(valor)

# Função type() -> mostra o tipo de dado
# ---------------------
# type(10), type("abcde")

# Função -> Bloco de código
# -------------------------
# def nome_da_funcao():
#       códigos

# Módulos -> arquivos com códigos que serão importado em outros arquivos
# ---------------------
# from math import pi, pow

from os import system

lista = [{"nome": "Restaurante 1", "categoria": "Mexicana", "status": False},
         {"nome": "Restaurante 2", "categoria": "Japonesa", "status": False}]


def exibir_titulo():
    print('''
░██████╗░█████╗░██████╗░░█████╗░██████╗░  ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
╚█████╗░███████║██████╦╝██║░░██║██████╔╝  █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗  ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║  ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░
''')


def menu():
    print('1. Cadastrar')
    print('2. Listar')
    print('3. Ativar')
    print('4. Sair\n')


def escolha_opcao():
    try:
        escolha = input('Escolha uma opção: ')
        escolha = int(escolha)
        if escolha == 1:
            cadastrar()
        elif escolha == 2:
            listar()
        elif escolha == 3:
            alterar_status()
        else:
            encerrar()
    except ValueError:
        opcao_invalida()


def opcao_invalida():
    print('\nOpção inválida')
    voltar_menu()


def voltar_menu():
    input('\nDigite uma <tecla> para voltar ao menu principal: ')
    main()


def exibir_subtitulo(texto):
    system("clear")
    linha = "-" * (len(texto) + 2)
    print(f'\n{texto}')
    print(linha + "\n")


def cadastrar():
    exibir_subtitulo("Cadastrar Restaurante")
    nome = input("\nDigite o nome do Restaurante: ")
    categoria = input("\nDigite a categoria do Restaurante: ")
    dados = {"nome": nome, "categoria": categoria, "status": False}
    lista.append(dados)
    print("\nCadastro realizado com sucesso!")
    voltar_menu()


def listar():
    exibir_subtitulo("Lista de Restaurantes")
    total = 0
    print(f'{"Nome".ljust(20)} | {"Categoria".ljust(20)} | {"Status"}')
    print("-" * 60)
    for restaurante in lista:
        nome_restaurante = restaurante["nome"]
        categoria = restaurante["categoria"]
        status = restaurante["status"]
        ativo = "☒" if status else "☐"

        print(f'\n{nome_restaurante.ljust(20)} | {categoria.ljust(20)} | {ativo}')

        total += 1

    print(f"\nTotal de restaurante: {total}")
    voltar_menu()


def alterar_status():
    exibir_subtitulo("Alterar Status")
    nome_restaurante = input("\nDigite o nome do Restaurante: ")
    restaurante_encontrado = False

    for restaurante in lista:
        if nome_restaurante == restaurante["nome"]:
            restaurante_encontrado = True
            restaurante["status"] = not restaurante["status"]
            mensagem = f"\nO restaurante {nome_restaurante} foi ativado com sucesso" if restaurante[
                "status"] else f"O resturante {nome_restaurante} foi desativado com sucesso"
            print(mensagem)
    if not restaurante_encontrado:
        print("\nO resturante não foi encontrado")
    voltar_menu()


def encerrar():
    system("clear")
    print("Finalizando")


def main():
    system("clear")
    exibir_titulo()
    menu()
    escolha_opcao()

# Entry point


if __name__ == "__main__":
    main()
    print()
