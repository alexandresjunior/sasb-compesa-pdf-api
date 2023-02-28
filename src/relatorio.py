# !pip install reportlab==3.6.12

from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4

from src.paginas.pagina1 import gerar_pag_1
from src.paginas.pagina2 import gerar_pag_2
from src.paginas.pagina3 import gerar_pag_3
from src.paginas.pagina4 import gerar_pag_4
from src.paginas.pagina5 import gerar_pag_5
from src.paginas.capa import gerar_capa
from src.paginas.sumario import gerar_sumario

def gerar_relatorio(buffer, barragem, formulario):
    # Criar um canvas do tamanho padrão do formato A4.
    # c = canvas.Canvas("relatorio.pdf", pagesize=A4) # Salva em disco
    c = canvas.Canvas(buffer)

    gerar_capa(c)
    altura_texto, num_pagina = gerar_sumario(c)
    altura_texto, num_pagina = gerar_pag_1(c, num_pagina)
    altura_texto, num_pagina = gerar_pag_2(c, altura_texto, num_pagina)
    altura_texto, num_pagina = gerar_pag_3(c, altura_texto, num_pagina)
    altura_texto, num_pagina = gerar_pag_4(c, altura_texto, num_pagina)
    altura_texto, num_pagina = gerar_pag_5(c, altura_texto, num_pagina)

    # Finalizar o canvas e salvar o conteúdo no buffer de memória.
    c.save()
