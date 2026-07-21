def formatar_nome_exercicio(nome):
    '''
    Função para formatar o nome do exercício.
    Retorna o nome formatado.
    '''
    return nome.strip().title()

def validar_series(series):
    '''
    Função para validar o número de séries.
    Retorna True se o número de séries for válido, False caso contrário.
    '''
    if series <= 0:
        return False
    return True
