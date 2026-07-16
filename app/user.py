def calcular_imc(peso, altura):
    if altura <= 0:
        return 0.0
    imc = peso / (altura * altura)
    return round(imc, 2)