import os
from app.models import criar_tabelas, adicionar_usuario, adicionar_exercicio

def exibir_menu():
    print("\n + " + "=" * 30)
    print("🏋️  SISTEMA APP TREINO 🏋️")
    print("=" * 30)
    print("1.criar Usuário")
    print("2.Listar usuários cadastrados")
    print("3.Listar exercícios cadastrados")
    print("0.Sair do sistema")
    print("=" * 30)


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
                user_id = adicionar_usuario(nome, sobrenome, int(idade), float(peso), float(altura))

                print(f"\nUsuário {nome} cadastrado com sucesso!")
                print("---CADASTRAR EXERCÍCIO PARA ESSE USUÁRIO---")
                nome_exercicio = input("Digite o nome do exercício: ")
                series = input("Digite o número de séries: ")

                while True:
                    if series.isdigit():
                        adicionar_exercicio(user_id, nome_exercicio, int(series))
                        print("Exercício cadastrado com sucesso!")
                    else:
                        print("\nErro: número de séries inválido!")

                    outro = input("Deseja cadastrar mais um exercício para esse usuário? (s/n): ")
                    if outro.lower() != "s":
                        break

                    nome_exercicio = input("Digite o nome do exercício: ")
                    series = input("Digite o número de séries: ")
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
        elif opcao == "3":
            limpar_tela()
            print("---Lista de exercícios cadastrados---")
            #eu ainda vou implementar a busca no banco!
            print("Aind vou implementar a busca no banco!")

        else:
            limpar_tela()
            print("Opção inválida! digite uma opção válida,0, 1 ou 2.")

if __name__ == "__main__":
    main()
    
    
    
    