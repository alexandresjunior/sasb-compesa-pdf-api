import json

def obter_formulario():
    with open('request_body_sample.json', 'r', encoding='utf-8') as f:
        data = json.load(f)

        return data['formulario']