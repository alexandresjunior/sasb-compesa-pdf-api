# !pip install reportlab==3.6.12

from src.utils.formatacao import obter_dimensoes, obter_espacamentos, obter_estilos, obter_margens


""" GERAÇÃO DA CAPA DO DOCUMENTO """

dimensoes = obter_dimensoes()
estilos = obter_estilos()
margens = obter_margens()
espacamentos = obter_espacamentos()

""" PAGINAÇÃO DO DOCUMENTO """

def inicializar_paginacao():
    num_pagina = 2

    return num_pagina

def atualizar_num_pagina(canvas, num_pagina):
    texto_alinhado_direita = str(num_pagina)

    canvas.setFillColorRGB(0, 0, 0)  # define a cor do texto como azul
    canvas.setFont("Helvetica", 12)  # define a fonte como tamanho 12

    largura_texto = canvas.stringWidth(
        texto_alinhado_direita)  # obtém a largura do texto
    
    # define a posição x para alinhar à direita
    posicao_x = dimensoes['largura'] - largura_texto - margens['direita']
    
    # define a posição y para ficar na última linha da página
    posicao_y = margens['inferior'] / 1.5
    
    canvas.drawString(posicao_x, posicao_y, texto_alinhado_direita)

    num_pagina += 1