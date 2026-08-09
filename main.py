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