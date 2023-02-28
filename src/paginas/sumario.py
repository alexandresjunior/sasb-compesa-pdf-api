# !pip install reportlab==3.6.12

from reportlab.platypus import Paragraph

from utils.formatacao import obter_dimensoes, obter_espacamentos, obter_estilos, obter_margens
from utils.paginacao import atualizar_num_pagina, inicializar_paginacao

""" GERAÇÃO DO SUMÁRIO DO DOCUMENTO """

dimensoes = obter_dimensoes()
estilos = obter_estilos()
margens = obter_margens()
espacamentos = obter_espacamentos()


def gerar_sumario(canvas):
    # Finaliza a página anterior e adiciona uma nova página em branco.
    canvas.showPage()

    # Insere imagem de fundo
    canvas.drawImage("assets/background_page.png", x=0, y=0,
                     width=dimensoes['largura'], height=dimensoes['altura'])

    # Define o título e desenha na página

    texto = "SUMÁRIO"
    paragrafo = Paragraph(texto, estilos['titulo'])
    largura_paragrafo, altura_paragrafo = paragrafo.wrap(dimensoes['largura'] - margens['esquerda'] - margens['direita'],
                                                         dimensoes['altura'] - margens['superior'] - margens['inferior'])
    altura_texto = margens['superior'] + \
        altura_paragrafo + espacamentos['titulo']
    paragrafo.drawOn(canvas, margens['esquerda'],
                     dimensoes['altura'] - altura_texto)

    # Define o texto e desenha na página

    texto = "1. APRESENTAÇÃO"
    paragrafo = Paragraph(texto, estilos['texto'])
    largura_paragrafo, altura_paragrafo = paragrafo.wrap(dimensoes['largura'] - margens['esquerda'] - margens['direita'],
                                                         dimensoes['altura'] - margens['superior'] - margens['inferior'])
    altura_texto += altura_paragrafo + espacamentos['linhas']
    paragrafo.drawOn(canvas, margens['esquerda'],
                     dimensoes['altura'] - altura_texto)

    # Define o texto e desenha na página

    texto = "&nbsp;1.1 OBJETIVO"
    paragrafo = Paragraph(texto, estilos['texto'])
    largura_paragrafo, altura_paragrafo = paragrafo.wrap(dimensoes['largura'] - margens['esquerda'] - margens['direita'],
                                                         dimensoes['altura'] - margens['superior'] - margens['inferior'])
    altura_texto += altura_paragrafo + espacamentos['linhas']
    paragrafo.drawOn(canvas, margens['esquerda'],
                     dimensoes['altura'] - altura_texto)

    # Define o texto e desenha na página

    texto = "&nbsp;1.2 DADOS DA BARRAGEM"
    paragrafo = Paragraph(texto, estilos['texto'])
    largura_paragrafo, altura_paragrafo = paragrafo.wrap(dimensoes['largura'] - margens['esquerda'] - margens['direita'],
                                                         dimensoes['altura'] - margens['superior'] - margens['inferior'])
    altura_texto += altura_paragrafo + espacamentos['linhas']
    paragrafo.drawOn(canvas, margens['esquerda'],
                     dimensoes['altura'] - altura_texto)

    # Define o texto e desenha na página

    texto = "&nbsp;1.3 PRINCIPAIS CARACTERÍSTICAS"
    paragrafo = Paragraph(texto, estilos['texto'])
    largura_paragrafo, altura_paragrafo = paragrafo.wrap(dimensoes['largura'] - margens['esquerda'] - margens['direita'],
                                                         dimensoes['altura'] - margens['superior'] - margens['inferior'])
    altura_texto += altura_paragrafo + espacamentos['linhas']
    paragrafo.drawOn(canvas, margens['esquerda'],
                     dimensoes['altura'] - altura_texto)

    # Define o texto e desenha na página

    texto = "2. FICHA DE INSPEÇÃO"
    paragrafo = Paragraph(texto, estilos['texto'])
    largura_paragrafo, altura_paragrafo = paragrafo.wrap(dimensoes['largura'] - margens['esquerda'] - margens['direita'],
                                                         dimensoes['altura'] - margens['superior'] - margens['inferior'])
    altura_texto += altura_paragrafo + espacamentos['linhas']
    paragrafo.drawOn(canvas, margens['esquerda'],
                     dimensoes['altura'] - altura_texto)

    # Define o texto e desenha na página

    texto = "3. AVALIAÇÃO DO NÍVEL DE PERIGO DA BARRAGEM"
    paragrafo = Paragraph(texto, estilos['texto'])
    largura_paragrafo, altura_paragrafo = paragrafo.wrap(dimensoes['largura'] - margens['esquerda'] - margens['direita'],
                                                         dimensoes['altura'] - margens['superior'] - margens['inferior'])
    altura_texto += altura_paragrafo + espacamentos['linhas']
    paragrafo.drawOn(canvas, margens['esquerda'],
                     dimensoes['altura'] - altura_texto)

    # Define o texto e desenha na página

    texto = "4. RECOMENDAÇÕES"
    paragrafo = Paragraph(texto, estilos['texto'])
    largura_paragrafo, altura_paragrafo = paragrafo.wrap(dimensoes['largura'] - margens['esquerda'] - margens['direita'],
                                                         dimensoes['altura'] - margens['superior'] - margens['inferior'])
    altura_texto += altura_paragrafo + espacamentos['linhas']
    paragrafo.drawOn(canvas, margens['esquerda'],
                     dimensoes['altura'] - altura_texto)

    # Define o texto e desenha na página

    texto = "ANEXOS"
    paragrafo = Paragraph(texto, estilos['texto'])
    largura_paragrafo, altura_paragrafo = paragrafo.wrap(dimensoes['largura'] - margens['esquerda'] - margens['direita'],
                                                         dimensoes['altura'] - margens['superior'] - margens['inferior'])
    altura_texto += altura_paragrafo + espacamentos['linhas']
    paragrafo.drawOn(canvas, margens['esquerda'],
                     dimensoes['altura'] - altura_texto)
    
    num_pagina = inicializar_paginacao()

    num_pagina = atualizar_num_pagina(canvas, num_pagina)

    return altura_texto, num_pagina