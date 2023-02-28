# !pip install reportlab==3.6.12

from reportlab.platypus import Paragraph

from src.utils.formatacao import obter_dimensoes, obter_estilos, obter_margens, obter_espacamentos
from src.utils.paginacao import atualizar_num_pagina, criar_nova_pagina
from src.utils.barragem import substituir_placeholders


""" GERAÇÃO DA PÁGINA 1 DO DOCUMENTO """

dimensoes = obter_dimensoes()
estilos = obter_estilos()
margens = obter_margens()
espacamentos = obter_espacamentos()

def gerar_pag_1(canvas, num_pagina, barragem):
    criar_nova_pagina(canvas)

    textos = [
        "O presente relatório tem por objetivo apresentar os resultados da {{num_vistoria}}ª inspeção de segurança regular da barragem {{nome_barragem}}, sob a responsabilidade da {{titularidade}}. A vistoria foi realizada no dia {{data}}.",
        "A Resolução APAC Nº 03/2017-DC, de 28 de dezembro de 2017, estabelece a periodicidade de execução ou atualização, a qualificação dos responsáveis técnicos, o conteúdo mínimo e o nível de detalhamento do Plano de Segurança da Barragem, das Inspeções de Segurança Regular e Especial, da Revisão Periódica de Segurança de Barragem e do Plano de Ação de Emergência, conforme art. 8º, 9º, 10º, 11º e 12º da Lei nº 12.334, de 20 de setembro de 2010, que estabelece a Política Nacional de Segurança de Barragens (PNSB).",
        "Os empreendedores, em face da sua experiência acumulada, têm a liberdade de adotar seus próprios modelos de ficha de inspeção e relatório, devendo, no entanto, levar em consideração os normativos emitidos pelas suas entidades fiscalizadoras.",
        "A inspeção foi realizada visando à verificação das condições estruturais e operacionais do empreendimento após o período construtivo, e a avaliação das ações corretivas e investigativas recomendadas na vistoria anterior.",
        "<b>Nome:</b> Barragem {{nome_barragem}}.",
        "<b>Empreendedor ou Responsável Legal:</b> {{titularidade}}.",
        "<b>Localização:</b> {{municipio}} - {{estado}}.",
        "<b>Outorga de Captação:</b> {{outorga_captacao}}.",
        "<b>Outorga de Construção:</b> {{outorga_construcao}}.",
        "<b>Data da Construção:</b> {{data_construcao}}.",
        "<b>Responsável pela Construção:</b> {{responsavel_construcao}}.",
        "<b>Bacia:</b> {{bacia_hidrografica}}.",
        "<b>Curso d'água barrado:</b> {{curso_de_agua_barrado}}.",
        "<b>Finalidade:</b> {{finalidade}}."
    ]
    
    textos = substituir_placeholders(textos, barragem)

    # Define o título e desenha na página

    texto = "1. APRESENTAÇÃO"
    paragrafo = Paragraph(texto, estilos['titulo'])
    largura_paragrafo, altura_paragrafo = paragrafo.wrap(dimensoes['largura'] - margens['esquerda'] - margens['direita'],
                                                         dimensoes['altura'] - margens['superior'] - margens['inferior'])
    altura_texto = margens['superior'] + \
        altura_paragrafo + espacamentos['titulo']
    paragrafo.drawOn(canvas, margens['esquerda'],
                     dimensoes['altura'] - altura_texto)

    # Define o subtítulo e desenha na página

    texto = "1.1 OBJETIVO"
    paragrafo = Paragraph(texto, estilos['subtitulo'])
    largura_paragrafo, altura_paragrafo = paragrafo.wrap(dimensoes['largura'] - margens['esquerda'] - margens['direita'],
                                                         dimensoes['altura'] - margens['superior'] - margens['inferior'])
    altura_texto += altura_paragrafo + espacamentos['titulo'] + espacamentos['linhas']
    paragrafo.drawOn(canvas, margens['esquerda'],
                     dimensoes['altura'] - altura_texto)

    # Define o texto e desenha na página

    texto = textos[0]
    paragrafo = Paragraph(texto, estilos['texto'])
    largura_paragrafo, altura_paragrafo = paragrafo.wrap(dimensoes['largura'] - margens['esquerda'] - margens['direita'],
                                                         dimensoes['altura'] - margens['superior'] - margens['inferior'])
    altura_texto += altura_paragrafo + espacamentos['linhas']
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

    # Define o subtítulo e desenha na página

    texto = "1.2 DADOS DA BARRAGEM"
    paragrafo = Paragraph(texto, estilos['subtitulo'])
    largura_paragrafo, altura_paragrafo = paragrafo.wrap(dimensoes['largura'] - margens['esquerda'] - margens['direita'],
                                                         dimensoes['altura'] - margens['superior'] - margens['inferior'])
    altura_texto += altura_paragrafo + espacamentos['titulo'] + espacamentos['linhas']
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

    # Define o subtítulo e desenha na página

    texto = "1.3 PRINCIPAIS CARACTERÍSTICAS"
    paragrafo = Paragraph(texto, estilos['subtitulo'])
    largura_paragrafo, altura_paragrafo = paragrafo.wrap(dimensoes['largura'] - margens['esquerda'] - margens['direita'],
                                                         dimensoes['altura'] - margens['superior'] - margens['inferior'])
    altura_texto += altura_paragrafo + espacamentos['titulo'] + espacamentos['linhas']
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

    num_pagina = atualizar_num_pagina(canvas, num_pagina)

    return altura_texto, num_pagina
