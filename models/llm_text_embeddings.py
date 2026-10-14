import ollama

EMBED_MODEL = 'nomic-embed-text'

def get_text_embedding_using_ollama(
        text:str, embed_model:str=EMBED_MODEL) -> list:
    
    if text:
        response = ollama.embed(
            model=embed_model,
            input=text,
        )

        return response["embeddings"]
    
    return None

def get_embeddings(entity_type:list, embed_model:str=EMBED_MODEL) -> list:
    embed_type = []

    for [entity, type] in entity_type:
        embed = get_text_embedding_using_ollama(entity, embed_model)[0]
        embed_type.append([embed, type])

    return embed_type

def get_embeddings_for_list(list_of_entities:list, embed_model:str=EMBED_MODEL) -> list:
    list_of_embeddings = []

    for entry in list_of_entities:
        list_of_embeddings.append(get_embeddings(entry, embed_model))

    return list_of_embeddings