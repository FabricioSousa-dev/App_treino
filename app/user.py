def calcular_imc(peso, altura):
    '''
    Função para calcular o IMC (Índice de Massa Corporal).
    Retorna o IMC arredondado para duas casas decimais.
    '''
    if altura <= 0:
        return 0.0
    imc = peso / (altura * altura)
    return round(imc, 2)


def classificar_imc(imc):
    '''
    Função para classificar o IMC segundo as faixas padrão da OMS.
    Retorna uma string com a classificação.
    '''
    if imc == 0:
        return "IMC inválido"
    if imc < 18.5:
        return "Abaixo do peso"
    if imc < 25:
        return "Peso normal"
    if imc < 30:
        return "Sobrepeso"
    return "Obesidade"


def validar_idade(idade):
    '''
    Retorna True se a idade for um inteiro positivo plausível.
    '''
    return idade > 0 and idade < 130


def validar_peso(peso):
    '''
    Retorna True se o peso for positivo.
    '''
    return peso > 0


def validar_altura(altura):
    '''
    Retorna True se a altura for positiva e plausível (em metros).
    '''
    return 0 < altura < 3