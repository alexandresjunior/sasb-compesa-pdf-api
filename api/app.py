from flask import Flask

# Cria uma instância do Flask
app = Flask(__name__)

@app.route('/', methods=['GET'])
def init():
    return "SASB-COMPESA: Gerador de Relatório de Inspeção em PDF"

if __name__ == '__main__':
    app.run(debug=True)

## Run 'python app.py' to initialize this API