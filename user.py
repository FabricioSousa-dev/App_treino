person = list()

while True:
    user = dict()
    user['Nome'] = input("Enter your name: ").upper().strip()
    user['Sobrenome'] = input("Enter your last name: ").upper().strip()
    user['Idade'] = input("Enter your age: ").strip()
    user['Peso'] = input("Enter your weight: ").strip()
    user['Altura'] = input("Enter your height: ").strip()

    while True:
        opc = input("Do you want to add another person? [S/N]: ").upper().strip()[0]
        if opc in 'SN':
            break
        print("Error! Please enter only S or N.")

    person.append(user.copy())
    if opc == 'N':
        break

print("Position   | Name | Last Name | Age | Weight | Height")
for k, v in enumerate(person):
    print(f"{k+1:<10} | {v['Nome']:<4} | {v['Sobrenome']:<9} | {v['Idade']:<3} | {v['Peso']:<6} | {v['Altura']:<6}")