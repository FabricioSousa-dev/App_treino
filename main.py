import os
from app.models import criar_tabelas, adicionar_usuario

def exibir_menu():
    print("\n + ""=" * 30)
    print("🏋️  SISTEMA APP TREINO 🏋️")
    print("="*30)
    print("1.criar tabelas")
    print("2.Listar usuários cadastrados")
    print("0.Sair do sistema")
    print("="30)

def limpar_tela():
    os.system('cls')

def main():
    criar_tabelas()

    limpar_tela()
    print("Bem-vindo ao sistema de treino!")

    while True:
        exibir_menu()

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            limpar_tela()
            print("========Cadastrar novo usuário========")
            nome = input("Digite o nome do usuário: ")
            idade = input("Digite a idade do usuário: ")

            if idade.isdigit():
                adicionar_usuario(nome, idade)
                print(f"Usuário {nome} cadastrado com sucesso!")
            else:
                print("\n❌ Erro: a idade deve ser um número inteiro. por favor,tente novamente.")
        elif opcao == "2":
            limpar_tela()
            print("========Listar usuários cadastrados========")
