# !pip install reportlab==3.6.12

from reportlab.platypus import Paragraph
from reportlab.lib.utils import ImageReader

from mocks.formulario import obter_formulario
from utils.anexos import agrupar_anexos
from utils.formatacao import obter_dimensoes, obter_espacamentos, obter_estilos, obter_fator_redutor_imagem, obter_margens
from utils.paginacao import atualizar_num_pagina

""" GERAÇÃO DA PÁGINA 5 DO DOCUMENTO """

dimensoes = obter_dimensoes()
estilos = obter_estilos()
margens = obter_margens()
espacamentos = obter_espacamentos()

questoes = obter_formulario()

def gerar_pag_5(canvas, altura_texto, num_pagina):
    # Finaliza a página anterior e adiciona uma nova página em branco. 
    canvas.showPage()

    # Insere imagem de fundo
    canvas.drawImage("assets/background_page.png", x=0, y=0,
                     width=dimensoes['largura'], height=dimensoes['altura'])

    # Define o título e desenha na página

    texto = "ANEXOS"
    paragrafo = Paragraph(texto, estilos['titulo_centralizado'])
    largura_paragrafo, altura_paragrafo = paragrafo.wrap(dimensoes['largura'] - margens['esquerda'] - margens['direita'],
                                                         dimensoes['altura'] - margens['superior'] - margens['inferior'])
    x = (dimensoes['largura'] - largura_paragrafo) / 2      # posição X para centralizar o texto
    y = (dimensoes['altura'] - altura_paragrafo) / 2        # posição Y para centralizar o texto
    paragrafo.drawOn(canvas, x, y)

    num_pagina = atualizar_num_pagina(canvas, num_pagina)

    anexos = agrupar_anexos(questoes)

    # Cria o objeto de imagem a partir da string base64

    num_figura = 1

    for i in range(0, len(anexos), 2):
        # Finaliza a página anterior e adiciona uma nova página em branco. 
        canvas.showPage()

        # Insere imagem de fundo
        canvas.drawImage("assets/background_page.png", x=0, y=0, width=dimensoes['largura'], height=dimensoes['altura'])
        
        altura_texto = margens['superior']

        sub_imagens = anexos[i:i+2]

        for j in range(len(sub_imagens)):
            imagem_base64 = sub_imagens[j][0]
            imagem_obj = ImageReader(imagem_base64)

            largura_imagem, altura_imagem = imagem_obj.getSize()

            largura_imagem = obter_fator_redutor_imagem() * largura_imagem
            altura_imagem = obter_fator_redutor_imagem() * altura_imagem

            paragrafo = Paragraph(f'<img src="{imagem_base64}" width="{largura_imagem}" height="{altura_imagem}" />', estilos['texto'])
            largura_paragrafo, altura_paragrafo = paragrafo.wrap(dimensoes['largura'] - margens['esquerda'] - margens['direita'],
                                                                 dimensoes['altura'] - margens['superior'] - margens['inferior'])
            x = (dimensoes['largura'] - largura_imagem) / 2        # posição X para centralizar a imagem
            altura_texto += altura_paragrafo + altura_imagem + espacamentos['linhas']
            paragrafo.drawOn(canvas, x, dimensoes['altura'] - altura_texto)
            
            texto_legenda = sub_imagens[j][1]
            paragrafo = Paragraph(texto_legenda, estilos['legenda'])
            largura_paragrafo, altura_paragrafo = paragrafo.wrap(dimensoes['largura'] - margens['esquerda'] - margens['direita'],
                                                                 dimensoes['altura'] - margens['superior'] - margens['inferior'])
            x = (dimensoes['largura'] - largura_paragrafo) / 2     # posição X para centralizar a legenda
            altura_texto += altura_paragrafo + espacamentos['linhas']
            paragrafo.drawOn(canvas, x, dimensoes['altura'] - altura_texto)

            num_figura += 1

        num_pagina = atualizar_num_pagina(canvas, num_pagina)

    return altura_texto, num_pagina