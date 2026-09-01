import os
from app.models import (
    criar_tabelas,
    adicionar_usuario,
    listar_usuarios,
    buscar_usuario_por_id,
    deletar_usuario,
    adicionar_exercicio,
    listar_exercicios,
    listar_exercicios_por_usuario,
    atualizar_exercicio,
    deletar_exercicio,
)
from app.exercise import formatar_nome_exercicio, validar_series, validar_nome_exercicio, validar_dia, formatar_dia
from app.user import calcular_imc, classificar_imc, validar_idade, validar_peso, validar_altura


def exibir_menu():
    print("\n + " + "=" * 30)
    print("🏋️  SISTEMA APP TREINO 🏋️")
    print("=" * 30)
    print("1. Criar usuário")
    print("2. Listar usuários cadastrados")
    print("3. Listar todos os exercícios")
    print("4. Ver exercícios de um usuário")
    print("5. Adicionar exercício a um usuário existente")
    print("6. Editar exercício")
    print("7. Deletar exercício")
    print("8. Deletar usuário")
    print("0. Sair do sistema")
    print("=" * 30)


def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')


def escolher_usuario():
    '''
    Mostra a lista de usuários e pede um ID válido.
    Retorna o ID (int) ou None se inválido/cancelado.
    '''
    usuarios = listar_usuarios()
    if not usuarios:
        print("Nenhum usuário cadastrado ainda.")
        return None

    for usuario in usuarios:
        print(f"ID: {usuario['id']} - {usuario['nome']} {usuario['sobrenome']}")

    user_id = input("\nDigite o ID do usuário: ")
    if not user_id.isdigit():
        print("ID inválido!")
        return None

    if buscar_usuario_por_id(int(user_id)) is None:
        print("Usuário não encontrado!")
        return None

    return int(user_id)


def cadastrar_exercicios_para_usuario(user_id):
    while True:
        nome_exercicio = input("Digite o nome do exercício: ")
        series = input("Digite o número de séries: ")
        dia = input("Digite o dia da semana (Segunda, Terça, Quarta, Quinta, Sexta, Sábado, Domingo): ")

        if (validar_nome_exercicio(nome_exercicio) and series.isdigit()
                and validar_series(int(series)) and validar_dia(dia)):
            adicionar_exercicio(
                user_id,
                formatar_nome_exercicio(nome_exercicio),
                int(series),
                formatar_dia(dia)
            )
            print("Exercício cadastrado com sucesso!")
        else:
            print("\nErro: nome, séries ou dia inválido!")

        outro = input("Deseja cadastrar mais um exercício? (s/n): ")
        if outro.lower() != "s":
            break


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
            idade = input(f"Digite a sua idade {nome} {sobrenome}: ")
            peso = input(f"Digite o seu peso (kg) {nome} {sobrenome}: ")
            altura = input(f"Digite a sua altura (m) {nome} {sobrenome}: ")

            try:
                idade_i, peso_f, altura_f = int(idade), float(peso), float(altura)
            except ValueError:
                print("\nErro: idade, peso e altura devem ser números.")
                continue

            if not (validar_idade(idade_i) and validar_peso(peso_f) and validar_altura(altura_f)):
                print("\nErro: valores fora da faixa esperada (confira idade/peso/altura).")
                continue

            user_id = adicionar_usuario(nome, sobrenome, idade_i, peso_f, altura_f)
            imc = calcular_imc(peso_f, altura_f)
            print(f"\nUsuário {nome} cadastrado com sucesso! IMC: {imc} ({classificar_imc(imc)})")

            print("---CADASTRAR EXERCÍCIO PARA ESSE USUÁRIO---")
            cadastrar_exercicios_para_usuario(user_id)

        elif opcao == "2":
            limpar_tela()
            print("---Lista de usuários cadastrados---")
            usuarios = listar_usuarios()
            for usuario in usuarios:
                imc = calcular_imc(usuario['peso'], usuario['altura'])
                print("-" * 30)
                print(f"ID: {usuario['id']}, Nome: {usuario['nome']} {usuario['sobrenome']}, "
                      f"Idade: {usuario['idade']}, Peso: {usuario['peso']}, Altura: {usuario['altura']}, "
                      f"IMC: {imc} ({classificar_imc(imc)})")
            print("-" * 30)

        elif opcao == "3":
            limpar_tela()
            print("---Lista de todos os exercícios---")
            exercicios = listar_exercicios()
            if exercicios:
                for ex in exercicios:
                    print("-" * 30)
                    print(f"ID: {ex['id']}, Usuário ID: {ex['user_id']}, "
                          f"Exercício: {ex['nome_exercicio']}, Séries: {ex['series']}, Dia: {ex['dia']}")
                print("-" * 30)
            else:
                print("Nenhum exercício cadastrado ainda.")

        elif opcao == "4":
            limpar_tela()
            print("---Exercícios por usuário---")
            user_id = escolher_usuario()
            if user_id is not None:
                exercicios = listar_exercicios_por_usuario(user_id)
                if exercicios:
                    for ex in exercicios:
                        print("-" * 30)
                        print(f"ID: {ex['id']}, Exercício: {ex['nome_exercicio']}, Séries: {ex['series']}, Dia: {ex['dia']}")
                    print("-" * 30)
                else:
                    print("Esse usuário ainda não tem exercícios cadastrados.")

        elif opcao == "5":
            limpar_tela()
            print("---Adicionar exercício a usuário existente---")
            user_id = escolher_usuario()
            if user_id is not None:
                cadastrar_exercicios_para_usuario(user_id)

        elif opcao == "6":
            limpar_tela()
            print("---Editar exercício---")
            user_id = escolher_usuario()
            if user_id is not None:
                exercicios = listar_exercicios_por_usuario(user_id)
                if not exercicios:
                    print("Esse usuário não tem exercícios para editar.")
                    continue
                for ex in exercicios:
                    print(f"ID: {ex['id']} - {ex['nome_exercicio']} ({ex['series']} séries, {ex['dia']})")                
                ex_id = input("Digite o ID do exercício a editar: ")
                if ex_id.isdigit():
                    novo_nome = input("Novo nome (deixe em branco para não mudar): ")
                    nova_series = input("Novo número de séries (deixe em branco para não mudar): ")
                    novo_dia = input("Novo dia (deixa em branco para não mudar): ")
                    atualizar_exercicio(
                        int(ex_id),
                        formatar_nome_exercicio(novo_nome) if novo_nome.strip() else None,
                        int(nova_series) if nova_series.isdigit() else None,
                        formatar_dia(novo_dia) if novo_dia.strip() and validar_dia(novo_dia) else None

                        )
                    print("Exercício atualizado com sucesso!")
                else:
                    print("ID inválido!")

        elif opcao == "7":
            limpar_tela()
            print("---Deletar exercício---")
            user_id = escolher_usuario()
            if user_id is not None:
                exercicios = listar_exercicios_por_usuario(user_id)
                if not exercicios:
                    print("Esse usuário não tem exercícios para deletar.")
                    continue
                for ex in exercicios:
                    print(f"ID: {ex['id']} - {ex['nome_exercicio']} ({ex['series']} séries, {ex['dia']})")
                ex_id = input("Digite o ID do exercício a deletar: ")
                if ex_id.isdigit() and deletar_exercicio(int(ex_id)):
                    print("Exercício deletado com sucesso!")
                else:
                    print("ID inválido ou exercício não encontrado!")

        elif opcao == "8":
            limpar_tela()
            print("---Deletar usuário---")
            user_id = escolher_usuario()
            if user_id is not None:
                confirmacao = input("Tem certeza? Isso apagará também os exercícios dele (s/n): ")
                if confirmacao.lower() == "s" and deletar_usuario(user_id):
                    print("Usuário deletado com sucesso!")

        elif opcao == "0":
            limpar_tela()
            print("Saindo do sistema...")
            break

        else:
            limpar_tela()
            print("Opção inválida! Escolha uma opção entre 0 e 8.")


if __name__ == "__main__":
    main()