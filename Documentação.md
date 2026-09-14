# 🏋️ App Treino

Sistema de controle de treinos, com cadastro de usuários e seus exercícios (organizados por dia da semana, séries e repetições). O projeto tem **três formas de uso**: um CLI no terminal, uma API REST em Flask, e uma interface web simples que consome essa API.

## Índice

- [Estrutura do projeto](#estrutura-do-projeto)
- [Como funciona](#como-funciona)
- [Instalação](#instalação)
- [Uso — CLI (terminal)](#uso--cli-terminal)
- [Uso — API + Frontend web](#uso--api--frontend-web)
- [Referência da API](#referência-da-api)
- [Modelo de dados](#modelo-de-dados)
- [Validações](#validações)
- [Testes](#testes)

## Estrutura do projeto

```
App_treino/
├── app/
│   ├── database.py     # conexão com o SQLite
│   ├── models.py        # CRUD de usuários e exercícios
│   ├── exercise.py       # validações e formatação de exercício
│   └── user.py            # validações de usuário e cálculo de IMC
├── tests/
│   ├── __init__.py
│   └── test_app.py
├── main.py               # aplicação de terminal (CLI)
├── api.py                # API REST (Flask) + serve o frontend
├── index.html             # interface web (HTML/CSS/JS puro)
├── treino.db               # banco SQLite (criado automaticamente)
└── LICENSE
```

## Como funciona

```
[index.html]  --clique do usuário-->  [JavaScript]
                                            |
                                  fetch() manda um JSON
                                            |
                                            v
                                      [api.py]  (Flask, porta 5000)
                                            |
                                  chama funções de
                                            v
                                   [app/models.py]
                                            |
                                      grava/lê no
                                            v
                                      [treino.db]  (SQLite)
```

O `main.py` (CLI) fala direto com `app/models.py`, sem depender da API — é uma segunda forma de usar o mesmo banco de dados.

## Instalação

Pré-requisitos: Python 3.10+.

```bash
pip install flask flask-cors
```

Nenhuma outra dependência é necessária — o SQLite já vem embutido no Python.

## Uso — CLI (terminal)

```bash
python main.py
```

Menu disponível:

| Opção | Ação |
|---|---|
| 1 | Criar usuário (nome, sobrenome, idade, peso, altura) |
| 2 | Listar usuários cadastrados (com IMC calculado) |
| 3 | Listar todos os exercícios de todos os usuários |
| 4 | Ver exercícios de um usuário específico |
| 5 | Adicionar exercício a um usuário existente |
| 6 | Editar exercício (nome, séries, repetições e/ou dia) |
| 7 | Deletar exercício |
| 8 | Deletar usuário (apaga também os exercícios dele) |
| 0 | Sair |

## Uso — API + Frontend web

**1. Suba a API:**

```bash
python api.py
```

Ela sobe em `http://127.0.0.1:5000` e já cria/migra o banco (`treino.db`) automaticamente.

**2. Abra a interface:**

Acesse **`http://127.0.0.1:5000/`** no navegador — a própria API já serve o `index.html`.

*(Alternativa: abrir o `index.html` direto ou usar a extensão Live Server do VS Code — o CORS já está liberado para qualquer origem.)*

**Navegação da interface:**
- **Tela Home** — cadastro de novo usuário e lista de usuários (cada um mostrando idade/peso/altura e IMC).
- **Tela de detalhes** (ao clicar num usuário) — dados completos do usuário, formulário para adicionar exercício, e a lista de exercícios dele (nome, séries, repetições e dia), com opções de editar e excluir.

## Referência da API

Todas as respostas são em JSON. Base URL: `http://127.0.0.1:5000`.

### Usuários

| Método | Rota | Descrição |
|---|---|---|
| `GET` | `/usuarios` | Lista todos os usuários (com IMC e classificação) |
| `GET` | `/usuarios/<id>` | Busca um usuário pelo ID |
| `POST` | `/usuarios` | Cria um usuário |
| `DELETE` | `/usuarios/<id>` | Deleta um usuário (e seus exercícios, em cascata) |

**Corpo do `POST /usuarios`:**
```json
{
  "nome": "Fabricio",
  "sobrenome": "Teixeira",
  "idade": 22,
  "peso": 74,
  "altura": 1.73
}
```

**Resposta (201):**
```json
{
  "id": 1,
  "nome": "Fabricio",
  "sobrenome": "Teixeira",
  "idade": 22,
  "peso": 74.0,
  "altura": 1.73,
  "imc": 24.73,
  "classificacao_imc": "Peso normal"
}
```

### Exercícios

| Método | Rota | Descrição |
|---|---|---|
| `GET` | `/exercicios` | Lista todos os exercícios de todos os usuários |
| `GET` | `/usuarios/<id>/exercicios` | Lista os exercícios de um usuário específico |
| `POST` | `/usuarios/<id>/exercicios` | Cadastra um exercício para um usuário |
| `PUT` | `/exercicios/<id>` | Atualiza um exercício (qualquer campo é opcional) |
| `DELETE` | `/exercicios/<id>` | Deleta um exercício |

**Corpo do `POST /usuarios/<id>/exercicios`:**
```json
{
  "nome_exercicio": "supino",
  "series": 3,
  "repeticoes": 12,
  "dia": "segunda"
}
```

**Corpo do `PUT /exercicios/<id>`** (todos os campos são opcionais — só envie o que quer mudar):
```json
{
  "repeticoes": 10
}
```

### Erros

Erros de validação retornam `400` com uma mensagem, por exemplo:
```json
{ "erro": "dia inválido. Use Segunda, Terça, Quarta, Quinta, Sexta, Sábado ou Domingo" }
```

IDs inexistentes retornam `404`:
```json
{ "erro": "Usuário não encontrado" }
```

## Modelo de dados

**Tabela `users`**

| Campo | Tipo | Observação |
|---|---|---|
| id | INTEGER | chave primária |
| nome | TEXT | obrigatório |
| sobrenome | TEXT | obrigatório |
| idade | INTEGER | |
| peso | REAL | em kg |
| altura | REAL | em metros |

**Tabela `exercises`**

| Campo | Tipo | Observação |
|---|---|---|
| id | INTEGER | chave primária |
| user_id | INTEGER | FK para `users.id`, `ON DELETE CASCADE` |
| nome_exercicio | TEXT | obrigatório |
| series | INTEGER | |
| repeticoes | INTEGER | |
| dia | TEXT | um dos 7 dias da semana |

## Validações

- **Idade:** entre 1 e 129 anos
- **Peso:** maior que zero
- **Altura:** entre 0 e 3 metros
- **Nome do exercício:** não pode ser vazio
- **Séries / repetições:** número inteiro maior que zero
- **Dia da semana:** deve ser um de `Segunda, Terça, Quarta, Quinta, Sexta, Sábado, Domingo` (aceita minúsculas — é formatado automaticamente)
- **IMC:** calculado como `peso / altura²`, classificado em Abaixo do peso / Peso normal / Sobrepeso / Obesidade

## Testes

```bash
python -m pytest tests/
```