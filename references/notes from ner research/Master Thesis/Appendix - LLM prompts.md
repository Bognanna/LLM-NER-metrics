```
prompt_1 = """

# Instruction

Analyze the sentence and extract from it all entities of types {types}.

Assign to them types from the below list.

Keep in mind, that entities could be discontinuous, long and descriptive.

  

## Sentence

{sentence}

  

## Types

{types}

"""

  

prompt_2 = """

# Instruction

Analyze the sentence and extract from it all entities of types {types}.

Assign to them types from the below list.

Keep in mind, that entities could be discontinuous, long and descriptive.

Base on below examples.

  

## Sentence

{sentence}

  

## Types

{types}

  

## Examples

### Example-1 discontinuous entity

- Sentence: "the muscle and joints in my angles hurt",

- Entities: [['the muscle in the angles hurt', 'Symptom'], ['joints in the angles hurt', 'Symptom']

### Example-2 discontinuous entity

 - Sentence: "lightheadedness and blurry vision when standing"

 - Entities: [['lightheadedness when standing', 'Symptom'], ['blurry vision when standing', 'Symptom']]

### Example-3 long, descriptive span

 - Sentence: "severe pain in the muscles in the shoulder area"

 - Entities: [['severe pain in the muscles in the shoulder area', 'Symptom']]

### Example-4 long, descriptive span

 - Sentence: "I did take my blood pressure today though, and it was slightly elevated from the norm."

 - Entities: [['blood pressure slightly elevated', 'Symptom']]

"""
```