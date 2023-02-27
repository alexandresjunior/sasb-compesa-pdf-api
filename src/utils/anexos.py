def agrupar_anexos(questoes):
    """ AGRUPAMENTO DOS ANEXOS DO FORMULÁRIO """

    anexos = []

    num_figura = 1

    for questao in questoes:
        if 'subsecoes' in questao:
            for subsecao in questao['subsecoes']:
                if 'itens' in subsecao:
                    for item in subsecao['itens']:
                        descricao = item['descricao']
                        situacao = item['resposta']['situacao']
                        magnitude = item['resposta']['magnitude']
                        nivelPerigo = item['resposta']['nivelPerigo']

                        for anexo in item['resposta']['anexos']:
                            source = f"data:image/jpg;base64,{anexo['base64']}"
                            legenda = f"<b>Figura {num_figura}:</b> {descricao} com situação classificada como {situacao['sigla']}, magnitude como {magnitude['sigla']} e nível de perigo igual a {nivelPerigo['sigla']}."

                            anexos.append([source, legenda])
                            num_figura += 1

        if 'itens' in questao:
            for item in questao['itens']:
                descricao = item['descricao']
                situacao = item['resposta']['situacao']
                magnitude = item['resposta']['magnitude']
                nivelPerigo = item['resposta']['nivelPerigo']

                for anexo in item['resposta']['anexos']:
                    source = f"data:image/jpg;base64,{anexo['base64']}"
                    legenda = f"<b>Figura {num_figura}:</b> {descricao} com situação classificada como {situacao['sigla']}, magnitude como {magnitude['sigla']} e nível de perigo igual a {nivelPerigo['sigla']}."

                    anexos.append([source, legenda])
                    num_figura += 1
    
    return anexos