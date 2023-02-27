import json

def obter_questoes():
    with open('request_body_sample.json') as f:
        data = json.load(f)

        return data