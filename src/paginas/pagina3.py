# !pip install reportlab==3.6.12

from reportlab.platypus import Paragraph
from mocks.formulario import obter_formulario

from utils.formatacao import obter_dimensoes, obter_estilos, obter_margens, obter_espacamentos
from utils.paginacao import atualizar_num_pagina, criar_nova_pagina
from utils.inspecao import gerar_ficha_inspecao


""" GERAÇÃO DA PÁGINA 3 DO DOCUMENTO """

dimensoes = obter_dimensoes()
estilos = obter_estilos()
margens = obter_margens()
espacamentos = obter_espacamentos()

questoes = obter_formulario()

def gerar_pag_3(canvas, altura_texto, num_pagina):
    criar_nova_pagina(canvas)

    # Define o título e desenha na página

    texto = "2. FICHA DE INSPEÇÃO"
    paragrafo = Paragraph(texto, estilos['titulo'])
    largura_paragrafo, altura_paragrafo = paragrafo.wrap(dimensoes['largura'] - margens['esquerda'] - margens['direita'],
                                                         dimensoes['altura'] - margens['superior'] - margens['inferior'])
    altura_texto = margens['superior'] + \
        altura_paragrafo + espacamentos['titulo']
    paragrafo.drawOn(canvas, margens['esquerda'],
                     dimensoes['altura'] - altura_texto)

    # Define o texto e desenha na página

    texto = "Apresenta-se, a seguir, a Ficha de Inspeção da Barragem {{nome_barragem}}. O registro fotográfico das anomalias identificadas será apresentado sequencialmente."
    paragrafo = Paragraph(texto, estilos['texto'])
    largura_paragrafo, altura_paragrafo = paragrafo.wrap(dimensoes['largura'] - margens['esquerda'] - margens['direita'],
                                                         dimensoes['altura'] - margens['superior'] - margens['inferior'])
    altura_texto += altura_paragrafo + espacamentos['linhas']
    paragrafo.drawOn(canvas, margens['esquerda'],
                     dimensoes['altura'] - altura_texto)

    num_pagina = atualizar_num_pagina(canvas, num_pagina)

    num_pagina = gerar_ficha_inspecao(canvas, num_pagina, questoes, altura_texto)

    return altura_texto, num_pagina