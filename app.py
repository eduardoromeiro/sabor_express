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

lista = []


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
            print('\n--------> Ativar <--------')
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


def cadastrar():
    print('\n--------> Cadastrar <--------\n')
    nome = input("\nDigite o nome do Restaurante: ")
    lista.append(nome)
    print("\nCadastro realizado com sucesso!")
    voltar_menu()


def listar():
    system("clear")
    print('\n--------> Lista de Restaurantes <--------\n')
    total = 0
    for indice, restaurante in enumerate(lista):
        print(f'{indice} - {restaurante}')
        total += 1

    print(f"\nTotal de restaurante: {total}")
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
