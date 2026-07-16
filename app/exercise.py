def formatar_nome_exercicio(nome):
    return nome.strip().title()

def validar_series(series):
    if series <= 0:
        return False
    return True