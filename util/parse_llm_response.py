import json

def parse_response(response:str) -> list:
    response = json.loads(response)
    
    entities = []

    for e in response['entities']:
        entity = e['entity'].lower()
        type = e['type']
        entities.append([entity, type])

    return entities