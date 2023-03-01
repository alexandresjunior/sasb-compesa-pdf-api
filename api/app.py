from flask import Flask, Response
from reportlab.pdfgen import canvas
from io import BytesIO

# Cria uma instância do Flask
app = Flask(__name__)

@app.route('/', methods=['GET'])
def init():
    return "SASB-COMPESA: Gerador de Relatório de Inspeção em PDF"

@app.route('/sasb/relatorio', methods=['GET'])
def obter_relatorio():
    # Crie o arquivo PDF usando o ReportLab
    buffer = BytesIO()
    pdf = canvas.Canvas(buffer)
    pdf.drawString(100, 750, "Relatório de Inspeção")
    pdf.save()
    
    # Crie a resposta do Flask com o arquivo PDF em memória
    buffer.seek(0)

    # Converte o objeto PDF em HTML
    pdf_bytes = buffer.getvalue()
    pdf_string = pdf_bytes.decode('latin-1')
    html = pdf_string.encode('ascii', 'xmlcharrefreplace').decode()

    response = Response(html, mimetype='text/html')
    
    # response = make_response(buffer.read())
    
    # response.headers['Content-Type'] = 'application/pdf'
    # response.headers['Content-Disposition'] = 'attachment; filename=relatorio.pdf'
    
    return response

if __name__ == '__main__':
    app.run(debug=True)

## Run 'python app.py' to initialize this API