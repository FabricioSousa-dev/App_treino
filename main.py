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