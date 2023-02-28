def substituir_placeholders(textos, barragem):
    resultado = []

    for texto in textos:
        texto = texto.replace("{{num_vistoria}}", "A DEFINIR")
        texto = texto.replace("{{nome_barragem}}", str(barragem['nome']))
        texto = texto.replace("{{data}}", "A DEFINIR")
        texto = texto.replace("{{titularidade}}", str(barragem['titularidade']))
        texto = texto.replace("{{municipio}}", str(barragem['localizacao']['municipio']))
        texto = texto.replace("{{estado}}", str(barragem['localizacao']['estado']))
        texto = texto.replace("{{outorga_captacao}}", str(barragem['outorgaCaptacao']))
        texto = texto.replace("{{data_construcao}}", "A DEFINIR")
        texto = texto.replace("{{outorga_construcao}}", str(barragem['outorgaObraHidrica']))
        texto = texto.replace("{{responsavel_construcao}}", "A DEFINIR")
        texto = texto.replace("{{bacia_hidrografica}}", str(barragem['detalhes']['bacia']))
        texto = texto.replace("{{curso_de_agua_barrado}}", "A DEFINIR")
        texto = texto.replace("{{finalidade}}", "A DEFINIR")
        texto = texto.replace("{{sistema_coordenadas}}", "A DEFINIR")
        texto = texto.replace("{{latitude}}", str(barragem['localizacao']['latitude']))
        texto = texto.replace("{{longitude}}", str(barragem['localizacao']['longitude']))
        texto = texto.replace("{{volume}}", "A DEFINIR")
        texto = texto.replace("{{area_inundada}}", str(barragem['detalhes']['areaInundadaM2']))
        texto = texto.replace("{{cota}}", "A DEFINIR")
        texto = texto.replace("{{area_bacia_hidraulica}}", str(barragem['detalhes']['areaBaciaHidraulicaM2']))
        texto = texto.replace("{{area_bacia_hidrografica}}", str(barragem['detalhes']['areaBaciaHidrograficaKm2']))
        texto = texto.replace("{{tipo_barragem}}", str(barragem['detalhes']['tipo']))
        texto = texto.replace("{{cota_coroamento}}", str(barragem['detalhes']['cotaCoroamentoM']))
        texto = texto.replace("{{largura_crista}}", "A DEFINIR")
        texto = texto.replace("{{altura_maxima}}", "A DEFINIR")
        texto = texto.replace("{{comprimento_barragem}}", "A DEFINIR")
        texto = texto.replace("{{comprimento_vertedor}}", "A DEFINIR")
        texto = texto.replace("{{cota_soleira}}", "A DEFINIR")
        texto = texto.replace("{{risco}}", str(barragem['seguranca']['classificacaoDeRisco']))
        texto = texto.replace("{{dpa}}", str(barragem['seguranca']['danoPotencialAssociado']))
        texto = texto.replace("{{npgb}}", "A DEFINIR")

        resultado.append(texto)
    
    return resultado