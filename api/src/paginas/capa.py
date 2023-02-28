# !pip install reportlab==3.6.12

from reportlab.platypus import Paragraph

from src.utils.formatacao import obter_dimensoes, obter_espacamentos, obter_estilos, obter_margens
from src.utils.barragem import substituir_placeholders


""" GERAÇÃO DA CAPA DO DOCUMENTO """

dimensoes = obter_dimensoes()
estilos = obter_estilos()
margens = obter_margens()
espacamentos = obter_espacamentos()

def gerar_capa(canvas, barragem):
    textos = [
        "{{num_vistoria}}º RELATÓRIO DE INSPEÇÃO DE SEGURANÇA REGULAR DA BARRAGEM {{nome_barragem}}",
        "Recife, {{data}}."
    ]
    
    textos = substituir_placeholders(textos, barragem)

    # A imagem é adicionada ao canvas na posição (0, 0)
    # com uma largura e altura para preencher toda a página sem margens.
    canvas.drawImage("assets/background_cover.png", 0, 0,
                     dimensoes['largura'], dimensoes['altura'])

    # Define o texto centralizado na página

    texto = textos[0].upper()
    paragrafo = Paragraph(texto, estilos['capa'])
    largura_paragrafo, altura_paragrafo = paragrafo.wrap(dimensoes['largura'] - margens['esquerda'] - margens['direita'],
                                                         dimensoes['altura'] - margens['superior'] - margens['inferior'])

    x = (dimensoes['largura'] - largura_paragrafo) / 2  # posição X para centralizar o parágrafo
    y = (dimensoes['altura'] - altura_paragrafo) / 2    # posição Y para centralizar o parágrafo
    paragrafo.drawOn(canvas, x, y)

    # Define o texto na última linha da página alinhado à direita

    texto_alinhado_direita = textos[1]

    canvas.setFillColorRGB(0, 0, 0)  # define a cor do texto como azul
    canvas.setFont("Helvetica", 12)  # define a fonte como tamanho 12

    largura_texto = canvas.stringWidth(
        texto_alinhado_direita)  # obtém a largura do texto
    # define a posição x para alinhar à direita
    posicao_x = dimensoes['largura'] - largura_texto - margens['direita']
    # define a posição y para ficar na última linha da página
    posicao_y = 2 * margens['inferior']
    canvas.drawString(posicao_x, posicao_y, texto_alinhado_direita)
