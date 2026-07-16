from app.models import criar_tabelas, adicionar_usuario

def main():
    print(f"Bem-vindo(a) {__name__}!")
    print("Iniciando o sistemas...")
    criar_tabelas()
    print("Tabelas criadas com sucesso!")

    print("Adicionando usuário...")
    