# !pip install reportlab==3.6.12

from reportlab.platypus import Paragraph
from src.mocks.formulario import obter_questoes

from src.utils.formatacao import obter_dimensoes, obter_espacamentos, obter_estilos, obter_margens
from src.utils.paginacao import atualizar_num_pagina, inicializar_paginacao

""" GERAÇÃO DA PÁGINA 4 DO DOCUMENTO """

dimensoes = obter_dimensoes()
estilos = obter_estilos()
margens = obter_margens()
espacamentos = obter_espacamentos()

num_pagina = inicializar_paginacao()

questoes = obter_questoes()

def gerar_pag_4(canvas, altura_texto, num_pagina):
    # Finaliza a página anterior e adiciona uma nova página em branco. 
    canvas.showPage()

    # Insere imagem de fundo
    canvas.drawImage("background_page.png", x=0, y=0,
                     width=dimensoes['largura'], height=dimensoes['altura'])

    # Define o título e desenha na página

    texto = "3. AVALIAÇÃO DO NÍVEL DE PERIGO DA BARRAGEM"
    paragrafo = Paragraph(texto, estilos['titulo'])
    largura_paragrafo, altura_paragrafo = paragrafo.wrap(dimensoes['largura'] - margens['esquerda'] - margens['direita'],
                                                         dimensoes['altura'] - margens['superior'] - margens['inferior'])
    altura_texto = margens['superior'] + altura_paragrafo + espacamentos['titulo']
    paragrafo.drawOn(canvas, margens['esquerda'], dimensoes['altura'] - altura_texto)

    # Define o texto e desenha na página

    texto = "O Nível de Perigo Global da Barragem (NPGB) é {{npgb}}, consoante com o Art. 12º da Resolução nº 03/2017-DC de 28/12/2017, elaborada pela Agência Pernambucana de Águas e Climas (APAC)."
    paragrafo = Paragraph(texto, estilos['texto'])
    largura_paragrafo, altura_paragrafo = paragrafo.wrap(dimensoes['largura'] - margens['esquerda'] - margens['direita'],
                                                         dimensoes['altura'] - margens['superior'] - margens['inferior'])
    altura_texto += altura_paragrafo + espacamentos['linhas']
    paragrafo.drawOn(canvas, margens['esquerda'], dimensoes['altura'] - altura_texto)

    # Define o título e desenha na página

    texto = "4. RECOMENDAÇÕES"
    paragrafo = Paragraph(texto, estilos['titulo'])
    largura_paragrafo, altura_paragrafo = paragrafo.wrap(dimensoes['largura'] - margens['esquerda'] - margens['direita'],
                                                         dimensoes['altura'] - margens['superior'] - margens['inferior'])
    altura_texto += altura_paragrafo + espacamentos['titulo']
    paragrafo.drawOn(canvas, margens['esquerda'], dimensoes['altura'] - altura_texto)

    # Define o texto e desenha na página

    texto = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Phasellus elementum gravida dolor sed blandit. Nullam vel lobortis quam, id malesuada risus. Suspendisse potenti. In hac habitasse platea dictumst. Donec consequat odio non erat placerat, a ultricies sem hendrerit. Morbi semper blandit risus in sagittis. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla porttitor ullamcorper ante, vel maximus odio consequat et. Suspendisse vitae est finibus, porttitor orci id, pulvinar nulla. Cras eleifend lacus quis lacus pharetra, vitae pharetra magna lobortis. Duis commodo risus ac feugiat porta. Nulla dignissim magna quis nisl gravida, vitae interdum diam fermentum. Maecenas ac est eleifend, venenatis diam eget, gravida diam. Morbi maximus justo sed finibus interdum. Etiam sed efficitur nunc."
    paragrafo = Paragraph(texto, estilos['texto'])
    largura_paragrafo, altura_paragrafo = paragrafo.wrap(dimensoes['largura'] - margens['esquerda'] - margens['direita'],
                                                         dimensoes['altura'] - margens['superior'] - margens['inferior'])
    altura_texto += altura_paragrafo + espacamentos['linhas']
    paragrafo.drawOn(canvas, margens['esquerda'], dimensoes['altura'] - altura_texto)

    # Define o texto e desenha na página

    texto = "Recife, {{data}}."
    paragrafo = Paragraph(texto, estilos['texto'])
    largura_paragrafo, altura_paragrafo = paragrafo.wrap(dimensoes['largura'] - margens['esquerda'] - margens['direita'],
                                                         dimensoes['altura'] - margens['superior'] - margens['inferior'])
    altura_texto += altura_paragrafo + espacamentos['linhas']
    paragrafo.drawOn(canvas, margens['esquerda'], dimensoes['altura'] - altura_texto)

    # Define o texto e desenha na página

    texto = "Ciente,"
    paragrafo = Paragraph(texto, estilos['texto'])
    largura_paragrafo, altura_paragrafo = paragrafo.wrap(dimensoes['largura'] - margens['esquerda'] - margens['direita'],
                                                         dimensoes['altura'] - margens['superior'] - margens['inferior'])
    altura_texto += altura_paragrafo + espacamentos['linhas']
    paragrafo.drawOn(canvas, margens['esquerda'], dimensoes['altura'] - altura_texto)

    """### Assinaturas"""

    # Define o texto centralizado na página

    texto = "_______________________________________"
    paragrafo = Paragraph(texto, estilos['texto_centralizado'])
    largura_paragrafo, altura_paragrafo = paragrafo.wrap(dimensoes['largura'] - margens['esquerda'] - margens['direita'],
                                                         dimensoes['altura'] - margens['superior'] - margens['inferior'])

    x = (dimensoes['largura'] - largura_paragrafo) / 2 # posição X para centralizar o parágrafo
    altura_texto += altura_paragrafo + espacamentos['linhas'] + espacamentos['titulo']
    paragrafo.drawOn(canvas, margens['esquerda'], dimensoes['altura'] - altura_texto)

    # Define o texto centralizado na página

    texto = "{{nome_inspetor}}"
    paragrafo = Paragraph(texto, estilos['texto_centralizado'])
    largura_paragrafo, altura_paragrafo = paragrafo.wrap(dimensoes['largura'] - margens['esquerda'] - margens['direita'],
                                                         dimensoes['altura'] - margens['superior'] - margens['inferior'])

    x = (dimensoes['largura'] - largura_paragrafo) / 2 # posição X para centralizar o parágrafo
    altura_texto += altura_paragrafo + espacamentos['linhas'] + espacamentos['titulo']
    paragrafo.drawOn(canvas, margens['esquerda'], dimensoes['altura'] - altura_texto)

    # Define o texto centralizado na página

    texto = "{{ocupacao_inspetor}}"
    paragrafo = Paragraph(texto, estilos['texto_centralizado'])
    largura_paragrafo, altura_paragrafo = paragrafo.wrap(dimensoes['largura'] - margens['esquerda'] - margens['direita'],
                                                         dimensoes['altura'] - margens['superior'] - margens['inferior'])

    x = (dimensoes['largura'] - largura_paragrafo) / 2 # posição X para centralizar o parágrafo
    altura_texto += altura_paragrafo + espacamentos['linhas'] + espacamentos['titulo']
    paragrafo.drawOn(canvas, margens['esquerda'], dimensoes['altura'] - altura_texto)

    # Define o texto centralizado na página

    texto = "{{crea_inspetor}} – {{cpf_inspetor}}"
    paragrafo = Paragraph(texto, estilos['texto_centralizado'])
    largura_paragrafo, altura_paragrafo = paragrafo.wrap(dimensoes['largura'] - margens['esquerda'] - margens['direita'],
                                                         dimensoes['altura'] - margens['superior'] - margens['inferior'])

    x = (dimensoes['largura'] - largura_paragrafo) / 2 # posição X para centralizar o parágrafo
    altura_texto += altura_paragrafo + espacamentos['linhas'] + espacamentos['titulo']
    paragrafo.drawOn(canvas, margens['esquerda'], dimensoes['altura'] - altura_texto)

    # Define o texto centralizado na página

    texto = "_______________________________________"
    paragrafo = Paragraph(texto, estilos['texto_centralizado'])
    largura_paragrafo, altura_paragrafo = paragrafo.wrap(dimensoes['largura'] - margens['esquerda'] - margens['direita'],
                                                         dimensoes['altura'] - margens['superior'] - margens['inferior'])

    x = (dimensoes['largura'] - largura_paragrafo) / 2 # posição X para centralizar o parágrafo
    altura_texto += altura_paragrafo + espacamentos['linhas'] + espacamentos['titulo']
    paragrafo.drawOn(canvas, margens['esquerda'], dimensoes['altura'] - altura_texto)

    # Define o texto centralizado na página

    texto = "{{nome_responsavel_tecnico}}"
    paragrafo = Paragraph(texto, estilos['texto_centralizado'])
    largura_paragrafo, altura_paragrafo = paragrafo.wrap(dimensoes['largura'] - margens['esquerda'] - margens['direita'],
                                                         dimensoes['altura'] - margens['superior'] - margens['inferior'])

    x = (dimensoes['largura'] - largura_paragrafo) / 2 # posição X para centralizar o parágrafo
    altura_texto += altura_paragrafo + espacamentos['linhas'] + espacamentos['titulo']
    paragrafo.drawOn(canvas, margens['esquerda'], dimensoes['altura'] - altura_texto)

    # Define o texto centralizado na página

    texto = "Responsável Técnico pela Barragem"
    paragrafo = Paragraph(texto, estilos['texto_centralizado'])
    largura_paragrafo, altura_paragrafo = paragrafo.wrap(dimensoes['largura'] - margens['esquerda'] - margens['direita'],
                                                         dimensoes['altura'] - margens['superior'] - margens['inferior'])

    x = (dimensoes['largura'] - largura_paragrafo) / 2 # posição X para centralizar o parágrafo
    altura_texto += altura_paragrafo + espacamentos['linhas'] + espacamentos['titulo']
    paragrafo.drawOn(canvas, margens['esquerda'], dimensoes['altura'] - altura_texto)

    # Define o texto centralizado na página

    texto = "Gerente de Segurança de Barragens"
    paragrafo = Paragraph(texto, estilos['texto_centralizado'])
    largura_paragrafo, altura_paragrafo = paragrafo.wrap(dimensoes['largura'] - margens['esquerda'] - margens['direita'],
                                                         dimensoes['altura'] - margens['superior'] - margens['inferior'])

    x = (dimensoes['largura'] - largura_paragrafo) / 2 # posição X para centralizar o parágrafo
    altura_texto += altura_paragrafo + espacamentos['linhas'] + espacamentos['titulo']
    paragrafo.drawOn(canvas, margens['esquerda'], dimensoes['altura'] - altura_texto)

    # Define o texto centralizado na página

    texto = "_______________________________________"
    paragrafo = Paragraph(texto, estilos['texto_centralizado'])
    largura_paragrafo, altura_paragrafo = paragrafo.wrap(dimensoes['largura'] - margens['esquerda'] - margens['direita'],
                                                         dimensoes['altura'] - margens['superior'] - margens['inferior'])

    x = (dimensoes['largura'] - largura_paragrafo) / 2 # posição X para centralizar o parágrafo
    altura_texto += altura_paragrafo + espacamentos['linhas'] + espacamentos['titulo']
    paragrafo.drawOn(canvas, margens['esquerda'], dimensoes['altura'] - altura_texto)

    # Define o texto centralizado na página

    texto = "{{nome_diretor}}"
    paragrafo = Paragraph(texto, estilos['texto_centralizado'])
    largura_paragrafo, altura_paragrafo = paragrafo.wrap(dimensoes['largura'] - margens['esquerda'] - margens['direita'],
                                                         dimensoes['altura'] - margens['superior'] - margens['inferior'])

    x = (dimensoes['largura'] - largura_paragrafo) / 2 # posição X para centralizar o parágrafo
    altura_texto += altura_paragrafo + espacamentos['linhas'] + espacamentos['titulo']
    paragrafo.drawOn(canvas, margens['esquerda'], dimensoes['altura'] - altura_texto)

    # Define o texto centralizado na página

    texto = "{{diretoria_tecnica}}"
    paragrafo = Paragraph(texto, estilos['texto_centralizado'])
    largura_paragrafo, altura_paragrafo = paragrafo.wrap(dimensoes['largura'] - margens['esquerda'] - margens['direita'],
                                                         dimensoes['altura'] - margens['superior'] - margens['inferior'])

    x = (dimensoes['largura'] - largura_paragrafo) / 2 # posição X para centralizar o parágrafo
    altura_texto += altura_paragrafo + espacamentos['linhas'] + espacamentos['titulo']
    paragrafo.drawOn(canvas, margens['esquerda'], dimensoes['altura'] - altura_texto)

    atualizar_num_pagina(canvas, num_pagina)

    return altura_texto, num_pagina