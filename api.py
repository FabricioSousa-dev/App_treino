from flask import Flask, request, jsonify,send_file
from flask_cors import CORS

from app.models import (
    criar_tabelas,
    adicionar_usuario,
    listar_usuarios,
    buscar_usuario_por_id,
    deletar_usuario,
    adicionar_exercicio,
    listar_exercicios,
    listar_exercicios_por_usuario,
    atualizar_exercicio,
    deletar_exercicio,
)
from app.exercise import formatar_nome_exercicio, validar_series, validar_nome_exercicio, validar_dia, formatar_dia
from app.user import calcular_imc, classificar_imc, validar_idade, validar_peso, validar_altura

app = Flask(__name__)
CORS(app)  


def usuario_para_dict(usuario):
    ''''
    Converte um registro de usuário em um dicionário.
    Calcula o IMC e a classificação do IMC.'''
    imc = calcular_imc(usuario['peso'], usuario['altura'])
    return {
        "id": usuario["id"],
        "nome": usuario["nome"],
        "sobrenome": usuario["sobrenome"],
        "idade": usuario["idade"],
        "peso": usuario["peso"],
        "altura": usuario["altura"],
        "imc": imc,
        "classificacao_imc": classificar_imc(imc),
    }


def exercicio_para_dict(ex):
    '''Converte um registro de exercício em um dicionário.'''
    return {
        "id": ex["id"],
        "user_id": ex["user_id"],
        "nome_exercicio": ex["nome_exercicio"],
        "series": ex["series"],
        "dia": ex["dia"],
    }

# ---------- PÁGINA INICIAL ----------
@app.route("/", methods=["GET"])
def index():
    return send_file("index.html")


# ---------- USUÁRIOS ----------

@app.route("/usuarios", methods=["GET"])
def get_usuarios():
    '''Retorna a lista de todos os usuários cadastrados.'''
    usuarios = listar_usuarios()
    return jsonify([usuario_para_dict(u) for u in usuarios])


@app.route("/usuarios/<int:user_id>", methods=["GET"])
def get_usuario(user_id):
    usuario = buscar_usuario_por_id(user_id)
    if usuario is None:
        return jsonify({"erro": "Usuário não encontrado"}), 404
    return jsonify(usuario_para_dict(usuario))


@app.route("/usuarios", methods=["POST"])
def post_usuario():
    '''Adiciona um novo usuário.'''
    dados = request.get_json(silent=True) or {}
    nome = dados.get("nome")
    sobrenome = dados.get("sobrenome")

    try:
        idade = int(dados.get("idade"))
        peso = float(dados.get("peso"))
        altura = float(dados.get("altura"))
    except (TypeError, ValueError):
        return jsonify({"erro": "idade, peso e altura devem ser números"}), 400

    if not nome or not sobrenome:
        return jsonify({"erro": "nome e sobrenome são obrigatórios"}), 400

    if not (validar_idade(idade) and validar_peso(peso) and validar_altura(altura)):
        return jsonify({"erro": "idade, peso ou altura fora da faixa esperada"}), 400

    user_id = adicionar_usuario(nome, sobrenome, idade, peso, altura)
    usuario = buscar_usuario_por_id(user_id)
    return jsonify(usuario_para_dict(usuario)), 201


@app.route("/usuarios/<int:user_id>", methods=["DELETE"])
def delete_usuario(user_id):
    '''Deleta um usuário pelo ID.'''
    if buscar_usuario_por_id(user_id) is None:
        return jsonify({"erro": "Usuário não encontrado"}), 404
    deletar_usuario(user_id)
    return jsonify({"mensagem": "Usuário deletado com sucesso"})


# ---------- EXERCÍCIOS ----------

@app.route("/exercicios", methods=["GET"])
def get_exercicios():
    exercicios = listar_exercicios()
    return jsonify([exercicio_para_dict(e) for e in exercicios])


@app.route("/usuarios/<int:user_id>/exercicios", methods=["GET"])
def get_exercicios_por_usuario(user_id):
    '''Retorna os exercícios de um usuário específico.'''
    if buscar_usuario_por_id(user_id) is None:
        return jsonify({"erro": "Usuário não encontrado"}), 404
    exercicios = listar_exercicios_por_usuario(user_id)
    return jsonify([exercicio_para_dict(e) for e in exercicios])


@app.route("/usuarios/<int:user_id>/exercicios", methods=["POST"])
def post_exercicio(user_id):
    '''Adiciona um novo exercício para um usuário específico.'''
    if buscar_usuario_por_id(user_id) is None:
        return jsonify({"erro": "Usuário não encontrado"}), 404

    dados = request.get_json(silent=True) or {}
    nome_exercicio = dados.get("nome_exercicio", "")
    series = dados.get("series")
    dia = dados.get("dia", "")

    if not validar_nome_exercicio(nome_exercicio):
        return jsonify({"erro": "nome_exercicio inválido"}), 400

    try:
        series_int = int(series)
    except (TypeError, ValueError):
        return jsonify({"erro": "series deve ser um número inteiro"}), 400

    if not validar_series(series_int):
        return jsonify({"erro": "series deve ser maior que zero"}), 400

    if not validar_dia(dia):
        return jsonify({"erro": "dia inválido. Use Segunda, Terça, Quarta, Quinta, Sexta, Sábado ou Domingo"}), 400

    adicionar_exercicio(user_id, formatar_nome_exercicio(nome_exercicio), series_int, formatar_dia(dia))


    exercicios = listar_exercicios_por_usuario(user_id)
    return jsonify(exercicio_para_dict(exercicios[-1])), 201


@app.route("/exercicios/<int:exercicio_id>", methods=["PUT"])
def put_exercicio(exercicio_id):
    '''Atualiza os detalhes de um exercício específico.'''
    dados = request.get_json(silent=True) or {}

    nome_exercicio = dados.get("nome_exercicio")
    series = dados.get("series")
    dia = dados.get("dia")

    nome_final = None
    if nome_exercicio is not None:
        if not validar_nome_exercicio(nome_exercicio):
            return jsonify({"erro": "nome_exercicio inválido"}), 400
        nome_final = formatar_nome_exercicio(nome_exercicio)

    series_final = None
    if series is not None:
        try:
            series_final = int(series)
        except (TypeError, ValueError):
            return jsonify({"erro": "series deve ser um número inteiro"}), 400
        if not validar_series(series_final):
            return jsonify({"erro": "series deve ser maior que zero"}), 400

    dia_final = None
    if dia is not None: 
        if not validar_dia(dia):
            return jsonify({"erro": "dia inválido"}), 400
        dia_final = formatar_dia(dia)

    atualizar_exercicio(exercicio_id, nome_final, series_final, dia_final)
    return jsonify({"mensagem": "Exercício atualizado com sucesso"})


@app.route("/exercicios/<int:exercicio_id>", methods=["DELETE"])
def delete_exercicio(exercicio_id):
    '''Deleta um exercício pelo ID.'''
    if deletar_exercicio(exercicio_id):
        return jsonify({"mensagem": "Exercício deletado com sucesso"})
    return jsonify({"erro": "Exercício não encontrado"}), 404


if __name__ == "__main__":
    criar_tabelas()
    app.run(debug=True)