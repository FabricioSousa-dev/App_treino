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


def validar_nome_exercicio(nome):
    '''
    Função para validar se o nome do exercício não está vazio.
    Retorna True se válido, False caso contrário.
    '''
    return bool(nome and nome.strip())