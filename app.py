from flask import Flask, request, make_response

from src.relatorio import gerar_relatorio

# Cria uma instância do Flask
app = Flask(__name__)


@app.route('/api/hello', methods=['GET'])
def hello():
    return "Hello, World!"


@app.route('/relatorio', methods=['POST'])
def obter_relatorio():
    barragem = request.get_json()['barragem']
    formulario = request.get_json()['formulario']
    
    # Gera o relatório em PDF
    gerar_relatorio()
    
    # Crie a resposta do Flask com o arquivo PDF
    response = make_response(open("relatorio.pdf", "rb").read())
    
    response.headers['Content-Type'] = 'application/pdf'
    response.headers['Content-Disposition'] = 'attachment; filename=relatorio.pdf'
    
    return response


if __name__ == '__main__':
    app.run(debug=True)

## Run 'python app.py' to initialize this API