while True:
    nome = str(input("Digite seu nome:  ")).strip().upper()
    if nome == "FECHAR":
        print("fechando!....")
        break
    while not nome.isalpha():
        print("Por favor, digite apenas letras")
        nome = str(input("Digite seu nome:  ")).strip().upper()
print(f"Bem-vindo {nome}")