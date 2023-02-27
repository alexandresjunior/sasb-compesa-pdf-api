# !pip install reportlab==3.6.12

from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.colors import Color
from reportlab.lib.units import cm
from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus import TableStyle

""" DEFINIÇÃO DOS ESTILOS DO DOCUMENTO """


def obter_dimensoes():
    # Define as dimensões do documento

    dimensoes = {
        "largura": A4[0],
        "altura": A4[1],
        "colunas_tabela": [0.9*cm, 9.5*cm, 1.75*cm, 2*cm, 0.85*cm]
    }

    return dimensoes


def obter_margens():
    # Define as margens do documento

    margens = {
        "esquerda": 3*cm,
        "direita": 3*cm,
        "superior": 3*cm,
        "inferior": 3*cm,
    }

    return margens


def obter_espacamentos():
    # Define espaçamento entre linhas

    espacamentos = {
        "titulo": 0.35*cm,
        "linhas": 0.25*cm,
    }

    return espacamentos


def obter_estilos():
    # Define os estilos

    # There are four possible values of alignment,
    # defined as constants in the module reportlab.lib.enums.
    # These are TA_LEFT, TA_CENTER or TA_CENTRE, TA_RIGHT and TA_JUSTIFY,
    # with values of 0, 1, 2 and 4 respectively.

    cor_azul_escuro = Color(0.23, 0.26, 0.61)

    estilo_capa = ParagraphStyle(name="texto_azul_negrito",
                                 fontName="Helvetica-Bold",
                                 fontSize=26,
                                 leading=30,
                                 textColor=cor_azul_escuro,
                                 alignment=1)

    estilo_titulo = ParagraphStyle(name='titulo',
                                   fontName='Helvetica-Bold',
                                   fontSize=14,
                                   leading=20,
                                   textColor=cor_azul_escuro)

    estilo_titulo_centralizado = ParagraphStyle(name='titulo',
                                                fontName='Helvetica-Bold',
                                                fontSize=14,
                                                leading=20,
                                                textColor=cor_azul_escuro,
                                                alignment=1)

    estilo_subtitulo = ParagraphStyle(name='subtitulo',
                                      fontName='Helvetica-Bold',
                                      fontSize=12,
                                      leading=16,
                                      textColor=cor_azul_escuro)

    estilo_texto = ParagraphStyle(name='texto_justificado',
                                  fontName='Helvetica',
                                  fontSize=12,
                                  leading=16,
                                  alignment=4)

    estilo_texto_centralizado = ParagraphStyle(name='texto_centralizado',
                                               fontName='Helvetica',
                                               fontSize=12,
                                               leading=16,
                                               alignment=1)

    estilo_legenda = ParagraphStyle(name='legenda',
                                    fontName='Helvetica',
                                    fontSize=11,
                                    leading=15,
                                    alignment=1)

    fator_redutor_imagem = 0.4

    # Define o estilo da tabela

    estilo_tabela = TableStyle([
        ('ALIGN', (0, 0), (-1, 0), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, 0), 9),
        ('ALIGN', (0, 1), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 1), (-1, -1), 'Helvetica'),
        ('FONTSIZE', (0, 1), (-1, -1), 8),
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('TEXT_WRAP', (0, 1), (-1, -1), True),
    ])

    estilos = {
        "capa": estilo_capa,
        "titulo": estilo_titulo,
        "titulo_centralizado": estilo_titulo_centralizado,
        "subtitulo": estilo_subtitulo,
        "texto": estilo_texto,
        "texto_centralizado": estilo_texto_centralizado,
        "legenda": estilo_legenda,
        "fator_redutor_imagem": fator_redutor_imagem,
        "tabela": estilo_tabela
    }

    return estilos

def obter_fator_redutor_imagem():
    return 0.4