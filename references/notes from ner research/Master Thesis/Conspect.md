1. **Abstract** Abstrakt - eng
2. **Streszczenie** Abstrakt - pl
3. **Acknowledgements** Podziękowania
4. **Introduction** Wstęp
	1. **Motivation**
		1. Szybki rozwój LLMów, szukanie dla nich kolejnych zastosowań (NER, Embeddingi)
		2. LLMy w NER
		3. Problem z nieadekwatnymi metrykami
	2. **Objective** Cel pracy
	3. **Scope of the work** Zakres prac
	4. **Structure of the thesis** Schemat pracy
5. **Glossary** Słowniczek ?
6. **Natural Language Processing** NLP (możliwe, że nie będzie potrzebne)
7. **Information Extraction**
	1. Opis zagadnienia
	2. Podział na zadania: NER, Relation Extraction, Event Extraction, ...
	3. Zastosowania
	4. NOTE: entity linking/entity disambiguation
8. **Named Entity Recognition**
	1. Opis zagadnienia
		1. Encje
		2. Klasy encji
	2. **Types of NER tasks** Podział na podproblemy w zależności od typów encji
		1. Flat
		2. Discontinuous
		3. Nested
		4. Joint Overapped ?
		5. Unified
	3. **Approaches to NER** Podejścia do problemu NER
		1. **Rule-based approaches**
			1. Regular Expressions
			2. Lexicon
		2. **Machine learning-based approaches**
			1. Sequence Labeling
			2. Sequence-to-sequence
			3. Span Based
			4. Layer Based
			5. Inne: Grid-tagging, Hypergraph Based, Object detection, Transition Based
		3. **Hybrid approaches**
	4. **Performance evaluation** Obecne metryki skuteczności zaproponowanych podejść
9. **Usage of Large Language Models in NER** **task** NER, a LLMy
	1. Podejście do problemu NER w oparciu o LLMy
	2. **Advantages** Przewagi rozwiązań opartych o LLMy nad starszymi podejściami
	3. **Challenges with evaluation** Problem związany z przełożeniem "tradycyjnych" metryk na podejście w oparciu o LLMy
		1. Czym różnią się odpowiedzi dawane przez LLMy od tradycyjnych metod brak boundaries, BIO-tagging i innych rzeczy, które można sprawdzić 0/1
		2. Dlaczego tradycyjne metryki nie dają sobie z tym rady
	4. **Current evaluation methods** Dotychczasowe próby rozwiązania tego problemu
		1. human evaluation
		2. F1 with soft matchnig
		3. LLM as a judge
10. **CDEF - a new metric for LLM performance evaluation in NER task** Propozycja nowej metryki: CDEF
	1. **Conditions to satisfy** Założenia względem metryki
	2. **Embeddings**
	3. **Two measures: CDE & EF** Dwie miary: CDE, EF
		1. **Cosinus Distance of Embeddings**
			1. Opis metryki
			2. Zapis matematyczny/algorytmiczny
			3. Algorytm dobierania w pary
		2. **Entities Found**
			1. Opis metryki
			2. Zapis matematyczny/algorytmiczny
	4. **CDEF as combination of CDE & EF** Złożenie CDE i EF do CDEF
	5. Podsumowanie CDE, EF, CDEF (range, optimal, worst)
11.  **Use Cases**
	1. Opis warunków testów na use casach:
		1. Wybór metryk, których zachowanie będzie porównywane z zachowaniem CDEF
		2. Wybór rodzajów encji
	2. **Discontinuous spans**
		1. Use Case 1
		2. Use Case 2
		3. ...
	3. **Long, descriptive spans**
		1. Use Case 1
		2. Use Case 2
		3. ...
	4. Typy błędów 
	5. **Summary** Podsumowanie wniosków z analizy use casów
12.  **Benchamark tests** Testy na Benchmarku
	1. **Benchmark description** Przedstawienie Benchmarku
		1. **Schema** Schemat
		2. **Data** Pochodzenie danych: CADEC + GPT-4o + praca manualna
	2. **Tests** Opis przebiegu testów
	3. **Conclusions** Wnioski z testów
13. **Conclusions** Podsumowanie/ **Limitations** Wskazanie dalszych prac/lLimitations
14. **Codebase** Repozytorium na GitHubie
15. **GenAI usage declaration** Deklaracja dotycząca wykorzystania generatywnego AI przy pracach
16. **Bibliography** Bibliografia


-------------------------------------------------------------------
Do rozważenia:
- typy błędów robionych przez GPT: Missing spans, Missing types, Unmentioned spans, Unannotated spans, Incorect span offsets, Undefined types, Incorrect types (to z pracy An Emperical Study ...) / podział na typy wzięty z pracy promotora - tam była mowa o błędach robionych przez ASR
- rozdział o LLMach
	- co wpływa na ich efektywność w zadaniu NER (model, prompt, dostęp do zewnętrznej wiedzy)
- przerzucić podrozdział o embeddingach do osobnego rozdziału

Sformułowanie problemu, zauważenie problemów, 

Książka: 
[https://link.springer.com/book/10.1007/978-3-031-88566-2](https://link.springer.com/book/10.1007/978-3-031-88566-2)

