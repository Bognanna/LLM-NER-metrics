from ollama import chat
from typing import ClassVar, List
from pydantic import BaseModel, field_validator

prompt = """
# Instruction
Analyze the sentence and extract from it all entities of types {types}. 
Assign to them types from the below list.
Keep in mind, that entities could be discontinuous, long and descriptive.

## Sentence
{sentence}

## Types
{types}
"""

class Entity(BaseModel):
    entity: str
    type: str

    allowed_types: ClassVar[List[str]] = []

    @field_validator("type")
    def validate_type(cls, v):
        if cls.allowed_types and v not in cls.allowed_types:
            raise ValueError(f"type must be one of {cls.allowed_types}")
        return v

class EntitiesList(BaseModel):
    entities: List[Entity]

def __set_types(types: List[str]):
    Entity.allowed_types = types

def get_entities_from_llm(sentence: str, types: List[str]) -> str:

    __set_types(types)

    response = chat(
        model='llama3.1',
        format=EntitiesList.model_json_schema(),
        messages=[
            {
                'role': 'user', 
                'content': prompt.format(sentence=sentence, types=types),
            }
        ],
        options={"temperature": 0}
    )

    return response.message.content