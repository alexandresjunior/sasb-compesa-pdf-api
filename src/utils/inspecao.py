# !pip install reportlab==3.6.12

from reportlab.platypus import Paragraph, Table

from utils.formatacao import obter_dimensoes, obter_espacamentos, obter_estilos, obter_margens
from utils.paginacao import atualizar_num_pagina

dimensoes = obter_dimensoes()
estilos = obter_estilos()
margens = obter_margens()
espacamentos = obter_espacamentos()

""" GERAÇÃO DA FICHA DE INSPEÇÃO """


def gerar_ficha_inspecao(canvas, num_pagina, questoes, altura_texto):
    num_pagina_atual = num_pagina

    for questao in questoes:
        # Define o texto e desenha na página

        texto = f"<b>{questao['codigo']} - {questao['nome']}</b>"
        p_secao = Paragraph(texto, estilos['subtitulo'])
        largura_p_secao, altura_p_secao = p_secao.wrap(dimensoes['largura'] - margens['esquerda'] - margens['direita'],
                                                       dimensoes['altura'] - margens['superior'] - margens['inferior'])
        altura_texto += altura_p_secao + espacamentos['linhas']

        # Salva para imprimir o título da seção com a tabela
        altura_titulo = altura_texto

        if 'subsecoes' in questao:
            for subsecao in questao['subsecoes']:
                # Define o texto e desenha na página

                texto = f"<b>{subsecao['codigo']} - {subsecao['nome']}</b>"
                p_subsecao = Paragraph(texto, estilos['subtitulo'])
                largura_p_subsecao, altura_p_subsecao = p_subsecao.wrap(dimensoes['largura'] - margens['esquerda'] - margens['direita'],
                                                                        dimensoes['altura'] - margens['superior'] - margens['inferior'])
                altura_texto += altura_p_subsecao + espacamentos['linhas']

                # Salva para imprimir o título da subseção com a tabela
                altura_subtitulo = altura_texto

                dados = [
                    ["Item", 
                     "Localização / Anomalia",
                     "Situação", 
                     "Magnitude", 
                     "NP"],
                ]

                for item in subsecao['itens']:
                    dados.append(
                        [item['indice'], item['descricao'], item['resposta']['situacao']['sigla'],
                            item['resposta']['magnitude']['sigla'], item['resposta']['nivelPerigo']['sigla']]
                    )

                # Cria a tabela
                tabela = Table(
                    dados, style=estilos['tabela'], colWidths=dimensoes['colunas_tabela'])

                # Adiciona a tabela ao PDF
                largura_tabela, altura_tabela = tabela.wrap(dimensoes['largura'] - margens['esquerda'] - margens['direita'],
                                                            dimensoes['altura'] - margens['superior'] - margens['inferior'])
                altura_texto += altura_tabela + espacamentos['linhas']

                if (altura_texto > dimensoes['altura'] - margens['inferior']):
                    # Finaliza a página anterior e adiciona uma nova página em branco.
                    canvas.showPage()

                    # Insere imagem de fundo
                    canvas.drawImage("assets/background_page.png", x=0, y=0,
                                     width=dimensoes['largura'], height=dimensoes['altura'])

                    # Atualiza as alturas do titulo, subtitulo e tabela
                    altura_titulo = margens['superior'] + \
                        altura_p_secao + espacamentos['linhas']
                    altura_subtitulo = altura_titulo + \
                        altura_p_subsecao + espacamentos['linhas']
                    altura_texto = altura_subtitulo + \
                        altura_tabela + espacamentos['linhas']

                    num_pagina_atual = atualizar_num_pagina(canvas, num_pagina_atual)

                p_secao.drawOn(
                    canvas, margens['esquerda'], dimensoes['altura'] - altura_titulo)
                p_subsecao.drawOn(
                    canvas, margens['esquerda'], dimensoes['altura'] - altura_subtitulo)
                tabela.drawOn(
                    canvas, margens['esquerda'], dimensoes['altura'] - altura_texto)

            if 'itens' in questao:
                dados = [
                    ["Item", "Localização / Anomalia",
                        "Situação", "Magnitude", "NP"],
                ]

                for item in questao['itens']:
                    dados.append(
                        [item['indice'], item['descricao'], item['resposta']['situacao']['sigla'],
                            item['resposta']['magnitude']['sigla'], item['resposta']['nivelPerigo']['sigla']]
                    )

                # Cria a tabela
                tabela = Table(
                    dados, style=estilos['tabela'], colWidths=dimensoes['colunas_tabela'])

                # Adiciona a tabela ao PDF
                largura_tabela, altura_tabela = tabela.wrap(dimensoes['largura'] - margens['esquerda'] - margens['direita'],
                                                            dimensoes['altura'] - margens['superior'] - margens['inferior'])
                altura_texto += altura_tabela + espacamentos['linhas']

                if (altura_texto > dimensoes['altura'] - margens['inferior']):
                    # Finaliza a página anterior e adiciona uma nova página em branco.
                    canvas.showPage()

                    # Insere imagem de fundo
                    canvas.drawImage("assets/background_page.png", x=0, y=0,
                                     width=dimensoes['largura'], height=dimensoes['altura'])

                    # Atualiza as alturas do titulo, subtitulo e tabela
                    altura_titulo = margens['superior'] + \
                        altura_p_secao + espacamentos['linhas']
                    altura_texto = altura_titulo + \
                        altura_tabela + espacamentos['linhas']

                    num_pagina_atual = atualizar_num_pagina(canvas, num_pagina_atual)

                    p_secao.drawOn(
                        canvas, margens['esquerda'], dimensoes['altura'] - altura_titulo)
                    tabela.drawOn(
                        canvas, margens['esquerda'], dimensoes['altura'] - altura_texto)

    return num_pagina_atual