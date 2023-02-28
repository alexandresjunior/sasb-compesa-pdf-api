# !pip install reportlab==3.6.12

from reportlab.platypus import Paragraph

from src.utils.formatacao import obter_dimensoes, obter_estilos, obter_margens, obter_espacamentos
from src.utils.paginacao import atualizar_num_pagina, criar_nova_pagina
from src.utils.barragem import substituir_placeholders

""" GERAÇÃO DA PÁGINA 2 DO DOCUMENTO """

dimensoes = obter_dimensoes()
estilos = obter_estilos()
margens = obter_margens()
espacamentos = obter_espacamentos()

def gerar_pag_2(canvas, altura_texto, num_pagina, barragem):
    criar_nova_pagina(canvas)

    textos = [
        "<b>Sistema de Coordenadas:</b> {{sistema_coordenadas}}.",
        "<b>Latitude:</b> {{latitude}}.",
        "<b>Longitude:</b> {{longitude}}.",
        "<b>Capacidade do Reservatório:</b> aproximadamente {{volume}}. Fonte: Volume I do Plano de Segurança da Barragem (PSB).",
        "<b>Área Inundada:</b> aproximadamente {{area_inundada}} na cota {{cota}}. Fonte: Volume I do Plano de Segurança da Barragem (PSB).",
        "<b>Área da Bacia Hidráulica:</b> aproximadamente {{area_bacia_hidraulica}}. Fonte: Volume I do Plano de Segurança da Barragem (PSB).",
        "<b>Área da Bacia Hidrográfica:</b> aproximadamente {{area_bacia_hidrografica}}. Fonte: Volume I do Plano de Segurança da Barragem (PSB).",
        "<b>Tipo de Barragem:</b> {{tipo_barragem}}.",
        "<b>Cota do Coroamento:</b> aproximadamente {{cota_coroamento}}. Fonte: Volume I do Plano de Segurança da Barragem (PSB).",
        "<b>Largura da Crista:</b> aproximadamente {{largura_crista}}.",
        "<b>Altura Máxima:</b> aproximadamente {{altura_maxima}}, não considerando a fundação. Fonte: PE3D.",
        "<b>Comprimento da Barragem:</b> aproximadamente {{comprimento_barragem}} (medida realizada em campo com uma trena).",
        "<b>Comprimento do Vertedor:</b> aproximadamente {{comprimento_vertedor}} (medida realizada em campo com uma trena).",
        "<b>Cota da Soleira:</b> aproximadamente {{cota_soleira}}. Fonte: Volume I do Plano de Segurança da Barragem (PSB).",
        "<b>Classificação da Barragem Segundo Órgão Fiscalizador:</b> Risco {{risco}}, Dano Potencial Associado {{dpa}} (conforme Resolução CNRH nº 143/2012).",
        
    ]
    
    textos = substituir_placeholders(textos, barragem)

    # Define o texto e desenha na página

    texto = textos[0]
    paragrafo = Paragraph(texto, estilos['texto'])
    largura_paragrafo, altura_paragrafo = paragrafo.wrap(dimensoes['largura'] - margens['esquerda'] - margens['direita'],
                                                         dimensoes['altura'] - margens['superior'] - margens['inferior'])
    altura_texto = margens['superior'] + altura_paragrafo + espacamentos['linhas']
    paragrafo.drawOn(canvas, margens['esquerda'],
                     dimensoes['altura'] - altura_texto)

    # Define o texto e desenha na página

    texto = textos[1]
    paragrafo = Paragraph(texto, estilos['texto'])
    largura_paragrafo, altura_paragrafo = paragrafo.wrap(dimensoes['largura'] - margens['esquerda'] - margens['direita'],
                                                         dimensoes['altura'] - margens['superior'] - margens['inferior'])
    altura_texto += altura_paragrafo + espacamentos['linhas']
    paragrafo.drawOn(canvas, margens['esquerda'],
                     dimensoes['altura'] - altura_texto)

    # Define o texto e desenha na página

    texto = textos[2]
    paragrafo = Paragraph(texto, estilos['texto'])
    largura_paragrafo, altura_paragrafo = paragrafo.wrap(dimensoes['largura'] - margens['esquerda'] - margens['direita'],
                                                         dimensoes['altura'] - margens['superior'] - margens['inferior'])
    altura_texto += altura_paragrafo + espacamentos['linhas']
    paragrafo.drawOn(canvas, margens['esquerda'],
                     dimensoes['altura'] - altura_texto)

    # Define o texto e desenha na página

    texto = textos[3]
    paragrafo = Paragraph(texto, estilos['texto'])
    largura_paragrafo, altura_paragrafo = paragrafo.wrap(dimensoes['largura'] - margens['esquerda'] - margens['direita'],
                                                         dimensoes['altura'] - margens['superior'] - margens['inferior'])
    altura_texto += altura_paragrafo + espacamentos['linhas']
    paragrafo.drawOn(canvas, margens['esquerda'],
                     dimensoes['altura'] - altura_texto)

    # Define o texto e desenha na página

    texto = textos[4]
    paragrafo = Paragraph(texto, estilos['texto'])
    largura_paragrafo, altura_paragrafo = paragrafo.wrap(dimensoes['largura'] - margens['esquerda'] - margens['direita'],
                                                         dimensoes['altura'] - margens['superior'] - margens['inferior'])
    altura_texto += altura_paragrafo + espacamentos['linhas']
    paragrafo.drawOn(canvas, margens['esquerda'],
                     dimensoes['altura'] - altura_texto)

    # Define o texto e desenha na página

    texto = textos[5]
    paragrafo = Paragraph(texto, estilos['texto'])
    largura_paragrafo, altura_paragrafo = paragrafo.wrap(dimensoes['largura'] - margens['esquerda'] - margens['direita'],
                                                         dimensoes['altura'] - margens['superior'] - margens['inferior'])
    altura_texto += altura_paragrafo + espacamentos['linhas']
    paragrafo.drawOn(canvas, margens['esquerda'],
                     dimensoes['altura'] - altura_texto)

    # Define o texto e desenha na página

    texto = textos[6]
    paragrafo = Paragraph(texto, estilos['texto'])
    largura_paragrafo, altura_paragrafo = paragrafo.wrap(dimensoes['largura'] - margens['esquerda'] - margens['direita'],
                                                         dimensoes['altura'] - margens['superior'] - margens['inferior'])
    altura_texto += altura_paragrafo + espacamentos['linhas']
    paragrafo.drawOn(canvas, margens['esquerda'],
                     dimensoes['altura'] - altura_texto)

    # Define o texto e desenha na página

    texto = textos[7]
    paragrafo = Paragraph(texto, estilos['texto'])
    largura_paragrafo, altura_paragrafo = paragrafo.wrap(dimensoes['largura'] - margens['esquerda'] - margens['direita'],
                                                         dimensoes['altura'] - margens['superior'] - margens['inferior'])
    altura_texto += altura_paragrafo + espacamentos['linhas']
    paragrafo.drawOn(canvas, margens['esquerda'],
                     dimensoes['altura'] - altura_texto)

    # Define o texto e desenha na página

    texto = textos[8]
    paragrafo = Paragraph(texto, estilos['texto'])
    largura_paragrafo, altura_paragrafo = paragrafo.wrap(dimensoes['largura'] - margens['esquerda'] - margens['direita'],
                                                         dimensoes['altura'] - margens['superior'] - margens['inferior'])
    altura_texto += altura_paragrafo + espacamentos['linhas']
    paragrafo.drawOn(canvas, margens['esquerda'],
                     dimensoes['altura'] - altura_texto)

    # Define o texto e desenha na página

    texto = textos[9]
    paragrafo = Paragraph(texto, estilos['texto'])
    largura_paragrafo, altura_paragrafo = paragrafo.wrap(dimensoes['largura'] - margens['esquerda'] - margens['direita'],
                                                         dimensoes['altura'] - margens['superior'] - margens['inferior'])
    altura_texto += altura_paragrafo + espacamentos['linhas']
    paragrafo.drawOn(canvas, margens['esquerda'],
                     dimensoes['altura'] - altura_texto)

    # Define o texto e desenha na página

    texto = textos[10]
    paragrafo = Paragraph(texto, estilos['texto'])
    largura_paragrafo, altura_paragrafo = paragrafo.wrap(dimensoes['largura'] - margens['esquerda'] - margens['direita'],
                                                         dimensoes['altura'] - margens['superior'] - margens['inferior'])
    altura_texto += altura_paragrafo + espacamentos['linhas']
    paragrafo.drawOn(canvas, margens['esquerda'],
                     dimensoes['altura'] - altura_texto)

    # Define o texto e desenha na página

    texto = textos[11]
    paragrafo = Paragraph(texto, estilos['texto'])
    largura_paragrafo, altura_paragrafo = paragrafo.wrap(dimensoes['largura'] - margens['esquerda'] - margens['direita'],
                                                         dimensoes['altura'] - margens['superior'] - margens['inferior'])
    altura_texto += altura_paragrafo + espacamentos['linhas']
    paragrafo.drawOn(canvas, margens['esquerda'],
                     dimensoes['altura'] - altura_texto)

    # Define o texto e desenha na página

    texto = textos[12]
    paragrafo = Paragraph(texto, estilos['texto'])
    largura_paragrafo, altura_paragrafo = paragrafo.wrap(dimensoes['largura'] - margens['esquerda'] - margens['direita'],
                                                         dimensoes['altura'] - margens['superior'] - margens['inferior'])
    altura_texto += altura_paragrafo + espacamentos['linhas']
    paragrafo.drawOn(canvas, margens['esquerda'],
                     dimensoes['altura'] - altura_texto)

    # Define o texto e desenha na página

    texto = textos[13]
    paragrafo = Paragraph(texto, estilos['texto'])
    largura_paragrafo, altura_paragrafo = paragrafo.wrap(dimensoes['largura'] - margens['esquerda'] - margens['direita'],
                                                         dimensoes['altura'] - margens['superior'] - margens['inferior'])
    altura_texto += altura_paragrafo + espacamentos['linhas']
    paragrafo.drawOn(canvas, margens['esquerda'],
                     dimensoes['altura'] - altura_texto)

    # Define o texto e desenha na página

    texto = textos[14]
    paragrafo = Paragraph(texto, estilos['texto'])
    largura_paragrafo, altura_paragrafo = paragrafo.wrap(dimensoes['largura'] - margens['esquerda'] - margens['direita'],
                                                         dimensoes['altura'] - margens['superior'] - margens['inferior'])
    altura_texto += altura_paragrafo + espacamentos['linhas']
    paragrafo.drawOn(canvas, margens['esquerda'],
                     dimensoes['altura'] - altura_texto)

    num_pagina = atualizar_num_pagina(canvas, num_pagina)

    return altura_texto, num_pagina