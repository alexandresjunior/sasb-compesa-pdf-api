from flask import Flask, request, make_response, jsonify
from io import BytesIO
from src.relatorio import gerar_relatorio

# Cria uma instância do Flask
app = Flask(__name__)


@app.route('/', methods=['GET'])
def init():
    return "SASB-COMPESA: Gerador de Relatório de Inspeção em PDF"


@app.route('/sasb/relatorio', methods=['POST'])
def obter_relatorio():
    barragem = request.get_json()['barragem']
    formulario = request.get_json()['formulario']

    # Gera o relatório em PDF em memória
    buffer = BytesIO()
    gerar_relatorio(buffer, barragem, formulario)

    # Crie a resposta do Flask com o arquivo PDF
    buffer.seek(0)
    response = make_response(buffer.read())

    # Obter relatório salvo no disco
    # response = make_response(open("relatorio.pdf", "rb").read())

    response.headers['Content-Type'] = 'application/pdf'
    response.headers['Content-Disposition'] = 'attachment; filename=relatorio.pdf'

    return response


@app.route('/sasb/login', methods=['POST'])
def login():
    # Obtém os dados do corpo JSON da solicitação
    data = request.json
    email = data['email']
    senha = data['senha']

    # Realize a autenticação e verifique se a senha é correta
    if email == 'teste@compesa.com.br' and senha == 'teste':
        status = 200
        mensagem = 'Autenticação realizada com sucesso!'
        usuario = {
            'nome': 'Usuário de Teste',
            'cargo': 'Engenheiro Civil',
            'tipoUsuario': {
                'nome': 'Administrador'
            },
            'matricula': 12345,
            'email': email,
            'telefone': '(81) 99999-9999'
        }
    else:
        status = 400
        mensagem = 'E-mail ou senha inválidos! Tente novamente.'
        usuario = []

    # Retorna um JSON com o status e mensagem da autenticação
    return jsonify({'status': status, 'mensagem': mensagem, 'usuario': usuario})


@app.route('/sasb/cadastro', methods=['POST'])
def cadastro():
    # Obtém os dados do corpo JSON da solicitação
    data = request.json
    email = data['email']
    senha = data['senha']

    # Realize a autenticação e verifique se a senha é correta
    if email == 'teste@compesa.com.br' and senha == 'teste':
        status = 200
        mensagem = 'Cadastro realizado com sucesso!'
        usuario = {
            'nome': 'Usuário de Teste',
            'cargo': 'Engenheiro Civil',
            'tipoUsuario': {
                'nome': 'Administrador'
            },
            'matricula': 12345,
            'email': email,
            'telefone': '(81) 99999-9999'
        }
    else:
        status = 403
        mensagem = 'Acesso negado! Tente novamente.'
        usuario = []

    # Retorna um JSON com o status e mensagem da autenticação
    return jsonify({'status': status, 'mensagem': mensagem, 'usuario': usuario})


if __name__ == '__main__':
    app.run(debug=True)

# Run 'python app.py' to initialize this API
