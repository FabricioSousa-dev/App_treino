import os
from app.models import criar_tabelas, adicionar_usuario

def exibir_menu():
    print("\n + ""=" * 30)
    print("🏋️  SISTEMA APP TREINO 🏋️")
    print("="*30)
    print("1.criar tabelas")
    print("2.Listar usuários cadastrados")
    print("0.Sair do sistema")
    print("="*30)


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
            print("---CADASTRAR NOVO USUÁRIO---")

            nome = input("Digite o nome do usuário: ")
            sobrenome = input(f"Digite o seu sobrenome {nome}: ")
            idade = input(f"Digite a sua idade {nome} {sobrenome}:  ")
            peso = input(f"Digite o seu peso {nome} {sobrenome}:  ")
            altura = input(f"Digite a sua altura {nome} {sobrenome}:  ")
             
            if idade.isdigit():
                adicionar_usuario(nome, sobrenome, int(idade), float(peso), float(altura))
            else:
                print("\n Erro: Idade inválida! Digite um número inteiro para a idade.")
        elif opcao == "2":
            limpar_tela()
            print("---Lista de usuários cadastrados---")
            #eu ainda vou implementar a busca no banco!
        elif opcao == "0":
            limpar_tela()
            print("Saindo do sistema...")
            break
        else:
            limpar_tela()
            print("Opção inválida! digite uma opção válida,0, 1 ou 2.")
if __name__ == "__main__":
    main()

