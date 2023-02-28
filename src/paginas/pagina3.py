# !pip install reportlab==3.6.12

from reportlab.platypus import Paragraph

from src.utils.formatacao import obter_dimensoes, obter_estilos, obter_margens, obter_espacamentos
from src.utils.paginacao import atualizar_num_pagina, criar_nova_pagina
from src.utils.inspecao import gerar_ficha_inspecao
from src.utils.barragem import substituir_placeholders


""" GERAÇÃO DA PÁGINA 3 DO DOCUMENTO """

dimensoes = obter_dimensoes()
estilos = obter_estilos()
margens = obter_margens()
espacamentos = obter_espacamentos()

def gerar_pag_3(canvas, altura_texto, num_pagina, barragem, formulario):
    criar_nova_pagina(canvas)

    textos = [
        "Apresenta-se, a seguir, a Ficha de Inspeção da Barragem {{nome_barragem}}. O registro fotográfico das anomalias identificadas será apresentado sequencialmente."
    ]
    
    textos = substituir_placeholders(textos, barragem)

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

    texto = textos[0]
    paragrafo = Paragraph(texto, estilos['texto'])
    largura_paragrafo, altura_paragrafo = paragrafo.wrap(dimensoes['largura'] - margens['esquerda'] - margens['direita'],
                                                         dimensoes['altura'] - margens['superior'] - margens['inferior'])
    altura_texto += altura_paragrafo + espacamentos['linhas']
    paragrafo.drawOn(canvas, margens['esquerda'],
                     dimensoes['altura'] - altura_texto)

    num_pagina = atualizar_num_pagina(canvas, num_pagina)

    num_pagina = gerar_ficha_inspecao(canvas, num_pagina, formulario, altura_texto)

    return altura_texto, num_pagina