usuarios = list()

while True:
    u = str(input("Digite o seu nome: "))

    opcao = " "
    while not u.strip() or not u.isalpha():
        print("Nome invalido,use letras!")
        u = str(input("Digite o seu nome: "))

    print("Olá {}!".format(u))
    opcao = str(input("Deseja cadastrar outro usuario? (s/n): "))

    if opcao.lower() != "s":
        break
print("Usuario cadastrado com sucesso!")
print("Usuarios cadastrados:")

for i, user in enumerate(usuarios,start=1):
    print(f"{i} {user}")
