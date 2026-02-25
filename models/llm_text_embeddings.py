import ollama

EMBED_MODEL = 'nomic-embed-text'

def get_text_embedding_using_ollama(text:str):
    
    if text:
        response = ollama.embed(
            model=EMBED_MODEL,
            input=text,
        )

        return response["embeddings"]
    
    return None

def get_embeddings(entity_type:list):
    embed_type = []
    
    for entry in entity_type:
        new_entry = []
        for [entity, type] in entry:
            embed = get_text_embedding_using_ollama(entity)[0]
            new_entry.append([embed, type])
        embed_type.append(new_entry)

    return embed_type