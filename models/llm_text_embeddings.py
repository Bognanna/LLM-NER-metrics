import ollama

EMBED_MODEL = 'nomic-embed-text'

def get_text_embedding_using_ollama(text:str) -> list:
    
    if text:
        response = ollama.embed(
            model=EMBED_MODEL,
            input=text,
        )

        return response["embeddings"]
    
    return None

def get_embeddings(entity_type:list) -> list:
    embed_type = []

    for [entity, type] in entity_type:
        embed = get_text_embedding_using_ollama(entity)[0]
        embed_type.append([embed, type])

    return embed_type

def get_embeddings_for_list(list_of_entities:list) -> list:
    list_of_embeddings = []

    for entry in list_of_entities:
        list_of_embeddings.append(get_embeddings(entry))

    return list_of_embeddings