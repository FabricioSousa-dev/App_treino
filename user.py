u = str(input("Digite o seu nome: "))
opcao = " "
while not u.strip() or not u.isalpha():
    print("Nome invalido,use letras!")
    u = str(input("Digite o seu nome: "))
print("Olá {}!".format(u))