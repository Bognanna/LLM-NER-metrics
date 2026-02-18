http://scikit.ml/ <- biblioteka pythonowa do multilabelingu

https://www.boundaryml.com/ <- structured output

### Do przejrzenia
https://openreview.net/forum?id=feAbrMXGMh
- metryka complementary
- spoczko do porównania jak przeprowadzali testy
- używali P@1 - proportion of correct answers on the first try
- mierzyli korelację między wskazaniami metryki a tym jak dobrze radził sobie dany model
- zmierzyli to dla 4 dziedzin: programowania, matematyki, fizyki, medycyny
- wybrali 2 modele na których przeprowadzili testy - jeden jako główny model a drugi jako weryfikacja wyników
https://aclanthology.org/2025.coling-main.538/
- metryka poprawności parafraz
- skorzystali z datasetów MRPC i PAWS
- PAWS powstał po to, żeby oszukać metryki bazujące na podobieństiwe leksykalnym: “flights from New York to Florida” and “flights from Florida to New York”
- specjalnie skorzystali z nieopublikowanych datasetów, żeby uniknąć sytuacji, w której LLM na którym testują metrykę był uczony na tych datasetach
- MCPG bazujący na Monte-Carlo Tree Search: “a very old and rusted train parked on the tracks.” and “a very old and dirty train is parked in the grass.”
- opisują jak podeszli do przygotowania datasetu wygenerowanego przez LLM oraz przedstawiają użyte prompty: “Trading volume was incredibly light at 500.22 million shares, below an already thin 611.45 million exchanged at the same point Thursday.” and “The trading volume was significantly lower than usual on this day, with only 500.22 million shares exchanged compared to 611.45 million shares traded at the same time the previous day.”
- korzystali też HC dataset, który był w pełni stworzony przez człowieka
- opisują całkiem dokładnie jak podeszli do testowania metryki 
https://arxiv.org/abs/2511.16846
- metryka zwięzłości danej odpowiedzi, liczona w liczbie możliwych słów do usunięcia przez llm
- WikiEval dataset: human-annotated benchmark, trójki question-context-answe + GPT-4 który rozszerzył odpowiedzi
- dodatkowo 3 ludzkich sędziów
- porównanie metryki z human-annotated wyliczyli dla tego Spearman's rank correlation
- generative AI declaration
https://aclanthology.org/2024.findings-acl.126/
- revision distance metric do mierzenia jakości generowanego tekstu
- metryka, której wartość jest generowana przez LLM
- dwa datasety: easy-writing task, challenge-writing task
- podzielili sobie model na słabe i mocne w realizowaniu zadania pisania
- porównali jak różne metryki Rouge 1, 2, L, Bert-Score, GPT-Score oceniają jakoś pisania słabych i mocnych modeli, a następnie % wyrazili zmianę oceny, pokazując, że ich metryka dała największą różnicę
- porównują za pomocą Spearman correlation wyniki z human evaluation score
- human evaluation: Chosen and Rejected text