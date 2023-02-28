# !pip install reportlab==3.6.12

from reportlab.platypus import Paragraph

from utils.formatacao import obter_dimensoes, obter_estilos, obter_margens, obter_espacamentos
from utils.paginacao import atualizar_num_pagina


""" GERAÇÃO DA PÁGINA 1 DO DOCUMENTO """

dimensoes = obter_dimensoes()
estilos = obter_estilos()
margens = obter_margens()
espacamentos = obter_espacamentos()

def gerar_pag_1(canvas, num_pagina):
    # Finaliza a página anterior e adiciona uma nova página em branco.
    canvas.showPage()

    # Insere imagem de fundo
    canvas.drawImage("assets/background_page.png", x=0, y=0,
                     width=dimensoes['largura'], height=dimensoes['altura'])

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
    altura_texto += altura_paragrafo + \
        espacamentos['titulo'] + espacamentos['linhas']
    paragrafo.drawOn(canvas, margens['esquerda'],
                     dimensoes['altura'] - altura_texto)

    # Define o texto e desenha na página

    texto = "O presente relatório tem por objetivo apresentar os resultados da {{num_vistoria}}ª inspeção de segurança regular da barragem {{nome_barragem}}, sob a responsabilidade da {{titularidade}}. A vistoria foi realizada no dia {{data}}."
    paragrafo = Paragraph(texto, estilos['texto'])
    largura_paragrafo, altura_paragrafo = paragrafo.wrap(dimensoes['largura'] - margens['esquerda'] - margens['direita'],
                                                         dimensoes['altura'] - margens['superior'] - margens['inferior'])
    altura_texto += altura_paragrafo + \
        espacamentos['titulo'] + espacamentos['linhas']
    paragrafo.drawOn(canvas, margens['esquerda'],
                     dimensoes['altura'] - altura_texto)

    # Define o texto e desenha na página

    texto = "A Resolução APAC Nº 03/2017-DC, de 28 de dezembro de 2017, estabelece a periodicidade de execução ou atualização, a qualificação dos responsáveis técnicos, o conteúdo mínimo e o nível de detalhamento do Plano de Segurança da Barragem, das Inspeções de Segurança Regular e Especial, da Revisão Periódica de Segurança de Barragem e do Plano de Ação de Emergência, conforme art. 8º, 9º, 10º, 11º e 12º da Lei nº 12.334, de 20 de setembro de 2010, que estabelece a Política Nacional de Segurança de Barragens (PNSB)."
    paragrafo = Paragraph(texto, estilos['texto'])
    largura_paragrafo, altura_paragrafo = paragrafo.wrap(dimensoes['largura'] - margens['esquerda'] - margens['direita'],
                                                         dimensoes['altura'] - margens['superior'] - margens['inferior'])
    altura_texto += altura_paragrafo + \
        espacamentos['titulo'] + espacamentos['linhas']
    paragrafo.drawOn(canvas, margens['esquerda'],
                     dimensoes['altura'] - altura_texto)

    # Define o texto e desenha na página

    texto = "Os empreendedores, em face da sua experiência acumulada, têm a liberdade de adotar seus próprios modelos de ficha de inspeção e relatório, devendo, no entanto, levar em consideração os normativos emitidos pelas suas entidades fiscalizadoras."
    paragrafo = Paragraph(texto, estilos['texto'])
    largura_paragrafo, altura_paragrafo = paragrafo.wrap(dimensoes['largura'] - margens['esquerda'] - margens['direita'],
                                                         dimensoes['altura'] - margens['superior'] - margens['inferior'])
    altura_texto += altura_paragrafo + \
        espacamentos['titulo'] + espacamentos['linhas']
    paragrafo.drawOn(canvas, margens['esquerda'],
                     dimensoes['altura'] - altura_texto)

    # Define o texto e desenha na página

    texto = "A inspeção foi realizada visando à verificação das condições estruturais e operacionais do empreendimento após o período construtivo, e a avaliação das ações corretivas e investigativas recomendadas na vistoria anterior."
    paragrafo = Paragraph(texto, estilos['texto'])
    largura_paragrafo, altura_paragrafo = paragrafo.wrap(dimensoes['largura'] - margens['esquerda'] - margens['direita'],
                                                         dimensoes['altura'] - margens['superior'] - margens['inferior'])
    altura_texto += altura_paragrafo + \
        espacamentos['titulo'] + espacamentos['linhas']
    paragrafo.drawOn(canvas, margens['esquerda'],
                     dimensoes['altura'] - altura_texto)

    # Define o subtítulo e desenha na página

    texto = "1.2 DADOS DA BARRAGEM"
    paragrafo = Paragraph(texto, estilos['subtitulo'])
    largura_paragrafo, altura_paragrafo = paragrafo.wrap(dimensoes['largura'] - margens['esquerda'] - margens['direita'],
                                                         dimensoes['altura'] - margens['superior'] - margens['inferior'])
    altura_texto += altura_paragrafo + \
        espacamentos['titulo'] + espacamentos['linhas']
    paragrafo.drawOn(canvas, margens['esquerda'],
                     dimensoes['altura'] - altura_texto)

    # Define o texto e desenha na página

    texto = "<b>Nome:</b> Barragem {{nome_barragem}}."
    paragrafo = Paragraph(texto, estilos['texto'])
    largura_paragrafo, altura_paragrafo = paragrafo.wrap(dimensoes['largura'] - margens['esquerda'] - margens['direita'],
                                                         dimensoes['altura'] - margens['superior'] - margens['inferior'])
    altura_texto += altura_paragrafo + \
        espacamentos['titulo'] + espacamentos['linhas']
    paragrafo.drawOn(canvas, margens['esquerda'],
                     dimensoes['altura'] - altura_texto)

    # Define o texto e desenha na página

    texto = "<b>Empreendedor ou Responsável Legal:</b> {{titularidade}}."
    paragrafo = Paragraph(texto, estilos['texto'])
    largura_paragrafo, altura_paragrafo = paragrafo.wrap(dimensoes['largura'] - margens['esquerda'] - margens['direita'],
                                                         dimensoes['altura'] - margens['superior'] - margens['inferior'])
    altura_texto += altura_paragrafo + \
        espacamentos['titulo'] + espacamentos['linhas']
    paragrafo.drawOn(canvas, margens['esquerda'],
                     dimensoes['altura'] - altura_texto)

    # Define o texto e desenha na página

    texto = "<b>Localização:</b> {{municipio}} - {{estado}}."
    paragrafo = Paragraph(texto, estilos['texto'])
    largura_paragrafo, altura_paragrafo = paragrafo.wrap(dimensoes['largura'] - margens['esquerda'] - margens['direita'],
                                                         dimensoes['altura'] - margens['superior'] - margens['inferior'])
    altura_texto += altura_paragrafo + \
        espacamentos['titulo'] + espacamentos['linhas']
    paragrafo.drawOn(canvas, margens['esquerda'],
                     dimensoes['altura'] - altura_texto)

    # Define o texto e desenha na página

    texto = "<b>Outorga de Captação:</b> {{outorga_captacao}}."
    paragrafo = Paragraph(texto, estilos['texto'])
    largura_paragrafo, altura_paragrafo = paragrafo.wrap(dimensoes['largura'] - margens['esquerda'] - margens['direita'],
                                                         dimensoes['altura'] - margens['superior'] - margens['inferior'])
    altura_texto += altura_paragrafo + \
        espacamentos['titulo'] + espacamentos['linhas']
    paragrafo.drawOn(canvas, margens['esquerda'],
                     dimensoes['altura'] - altura_texto)

    # Define o texto e desenha na página

    texto = "<b>Outorga de Construção:</b> {{outorga_construcao}}."
    paragrafo = Paragraph(texto, estilos['texto'])
    largura_paragrafo, altura_paragrafo = paragrafo.wrap(dimensoes['largura'] - margens['esquerda'] - margens['direita'],
                                                         dimensoes['altura'] - margens['superior'] - margens['inferior'])
    altura_texto += altura_paragrafo + \
        espacamentos['titulo'] + espacamentos['linhas']
    paragrafo.drawOn(canvas, margens['esquerda'],
                     dimensoes['altura'] - altura_texto)

    # Define o texto e desenha na página

    texto = "<b>Data da Construção:</b> {{outorga_construcao}}."
    paragrafo = Paragraph(texto, estilos['texto'])
    largura_paragrafo, altura_paragrafo = paragrafo.wrap(dimensoes['largura'] - margens['esquerda'] - margens['direita'],
                                                         dimensoes['altura'] - margens['superior'] - margens['inferior'])
    altura_texto += altura_paragrafo + \
        espacamentos['titulo'] + espacamentos['linhas']
    paragrafo.drawOn(canvas, margens['esquerda'],
                     dimensoes['altura'] - altura_texto)

    # Define o texto e desenha na página

    texto = "<b>Responsável pela Construção:</b> {{responsavel_construcao}}."
    paragrafo = Paragraph(texto, estilos['texto'])
    largura_paragrafo, altura_paragrafo = paragrafo.wrap(dimensoes['largura'] - margens['esquerda'] - margens['direita'],
                                                         dimensoes['altura'] - margens['superior'] - margens['inferior'])
    altura_texto += altura_paragrafo + \
        espacamentos['titulo'] + espacamentos['linhas']
    paragrafo.drawOn(canvas, margens['esquerda'],
                     dimensoes['altura'] - altura_texto)

    # Define o subtítulo e desenha na página

    texto = "1.3 PRINCIPAIS CARACTERÍSTICAS"
    paragrafo = Paragraph(texto, estilos['subtitulo'])
    largura_paragrafo, altura_paragrafo = paragrafo.wrap(dimensoes['largura'] - margens['esquerda'] - margens['direita'],
                                                         dimensoes['altura'] - margens['superior'] - margens['inferior'])
    altura_texto += altura_paragrafo + \
        espacamentos['titulo'] + espacamentos['linhas']
    paragrafo.drawOn(canvas, margens['esquerda'],
                     dimensoes['altura'] - altura_texto)

    # Define o texto e desenha na página

    texto = "<b>Bacia:</b> {{bacia_hidrografica}}."
    paragrafo = Paragraph(texto, estilos['texto'])
    largura_paragrafo, altura_paragrafo = paragrafo.wrap(dimensoes['largura'] - margens['esquerda'] - margens['direita'],
                                                         dimensoes['altura'] - margens['superior'] - margens['inferior'])
    altura_texto += altura_paragrafo + \
        espacamentos['titulo'] + espacamentos['linhas']
    paragrafo.drawOn(canvas, margens['esquerda'],
                     dimensoes['altura'] - altura_texto)

    # Define o texto e desenha na página

    texto = "<b>Curso d’água barrado:</b> {{curso_de_agua_barrado}}."
    paragrafo = Paragraph(texto, estilos['texto'])
    largura_paragrafo, altura_paragrafo = paragrafo.wrap(dimensoes['largura'] - margens['esquerda'] - margens['direita'],
                                                         dimensoes['altura'] - margens['superior'] - margens['inferior'])
    altura_texto += altura_paragrafo + \
        espacamentos['titulo'] + espacamentos['linhas']
    paragrafo.drawOn(canvas, margens['esquerda'],
                     dimensoes['altura'] - altura_texto)

    # Define o texto e desenha na página

    texto = "<b>Finalidade:</b> {{finalidade}}."
    paragrafo = Paragraph(texto, estilos['texto'])
    largura_paragrafo, altura_paragrafo = paragrafo.wrap(dimensoes['largura'] - margens['esquerda'] - margens['direita'],
                                                         dimensoes['altura'] - margens['superior'] - margens['inferior'])
    altura_texto += altura_paragrafo + \
        espacamentos['titulo'] + espacamentos['linhas']
    paragrafo.drawOn(canvas, margens['esquerda'],
                     dimensoes['altura'] - altura_texto)

    num_pagina = atualizar_num_pagina(canvas, num_pagina)

    return altura_texto, num_pagina
