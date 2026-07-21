def calcular_imc(peso, altura):
    '''
    Função para calcular o IMC (Índice de Massa Corporal).
    Retorna o IMC arredondado para duas casas decimais.'''
    if altura <= 0:
        return 0.0
    imc = peso / (altura * altura)
    return round(imc, 2)