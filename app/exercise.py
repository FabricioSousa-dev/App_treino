DIAS_VALIDOS = ["Segunda", "Terça", "Quarta", "Quinta", "Sexta", "Sábado", "Domingo"]


def formatar_nome_exercicio(nome):
    '''
    Função para formatar o nome do exercício.
    Retorna o nome formatado (sem espaços nas pontas, com iniciais maiúsculas).
    '''
    return nome.strip().title()


def validar_series(series):
    '''
    Função para validar o número de séries.
    Retorna True se o número de séries for válido (maior que zero), False caso contrário.
    '''
    return series > 0


def validar_repeticoes(repeticoes):
    '''
    Função para validar o número de repetições.
    Retorna True se o número de repetições for válido (maior que zero), False caso contrário.
    '''
    return repeticoes > 0


def validar_nome_exercicio(nome):
    '''
    Função para validar se o nome do exercício não está vazio.
    Retorna True se válido, False caso contrário.
    '''
    return bool(nome and nome.strip())


def formatar_dia(dia):
    '''
    Formata o dia da semana digitado (tira espaços, deixa com inicial maiúscula).
    '''
    return dia.strip().capitalize()


def validar_dia(dia):
    '''
    Retorna True se o dia informado é um dos dias da semana válidos.
    '''
    return formatar_dia(dia) in DIAS_VALIDOS