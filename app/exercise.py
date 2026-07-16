def formatar_nome_exercisio(nome):
    return nome.strip().title()

def validar_series(series):
    if series <= 0:
        return False
    return True