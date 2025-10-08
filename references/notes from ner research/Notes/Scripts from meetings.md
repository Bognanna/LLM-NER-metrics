18.09.2025
Następne spotkanie 2.10 godz. 11:30

Co z przypadkiem:
"After the second pill the same progression of symptoms only now the abdominal gas,cramps and pain would be with me all day." ?
Adnotatorzy uznali tutaj 2 encje: "abdominal gas", "abdominal cramps and pain"

Ale już później: "The abdominal gas,cramps and discomfort"
Adnotatorzy uznali tutaj 3 encje: "abdominal gas", "abdominal cramps", "abdominal dyscomfort"

Jak oznaczać labele discontinuous encji?
	T6	ADR 152 161;166 181	abdominal cramps and pain
	T4	ADR 152 161;162 165	abdominal gas

Problematyczne przypadki:
1) Discountinuous entity
	- The patient reported **pain in the lower back** and occasionally **in the right leg**. (encja zaproponowana przez chat)
	- The patient experienced **shortness of breath on exertion** and sometimes **at rest**. (encja zaproponowana przez chat - czy tutaj, w ogóle czas powinien być uwzgledniony?)
	- I **walk up & down steps** properly, no longer **sideways** like a toddler. (encja wzięta z zbioru danych - czy nie powinna ona uwzględniać negacji? - opis symptomu)
	- Have stopped taking and immediatedly **muscle/joint pain** eased and sleeping much better. (encja wzięta z zbioru danych)
	- **Menstrual cramps** present **with** or **without** **vaginal bleeding**. (encja wzięta z zbioru danych - tu są 2 różne encje with/without)
2) Nested entity
	- He was prescribed **oral metformin 500 mg tablets**. (zaproponowane przez chat)
		- Nested:
			- “metformin” (drug)
			- “metformin 500 mg” (drug + dosage)
			- “oral metformin 500 mg tablets” (full medication entity)
	- The patient was treated with **intravenous vancomycin therapy**. (zaproponowane przez chat)
		- Nested:
			- “vancomycin” (drug)
			- “intravenous vancomycin therapy” (treatment)
	- Severe pain in the muscles in the shoulder area. (encja z zbioru danych - adnotatorzy uznali ją za jedną, nie doszukując się w niej mniejszych encji)
			- pain
			- severe pain
			- severe pain in the muscles
			- severe pain in the muscles in the shoulder area
	-  Vaginal bleeding when it was not time for my period. (encja z zbioru danych - adnotatorzy uznali ją za jedną, nie doszukując się w niej mniejszych encji)
		- vaginal bleeding,
		- vaginal bleeding when it was not time for my period
3) Long, descriptive entity span
	- Without this drug I was severly restricted and **could only walk less than 100 meters**. (encja z zbioru danych - opis symptomu)
	- Recently I've been feeling like my **stomach is full and empty at the same time** hard to explain. (encja z zbioru danych - opis symptomu)
	- The boy was diagnosed with **a very bad lung infection that affected the lower part of his right lung**. (zaproponowane przez chat)
	- The doctors started **strong medicine through a vein to treat swelling in the brain caused by the immune system attacking itself**. (zaproponowane przez chat)

Inne zaproponowane przez LLM:
1) Ambiguity between common and medical term:
	- _The patient complained of cold hands after taking the medication._  _(“cold” could be a symptom or just temperature.)_
2) Abbreviation with multiple expansions:
	- _The doctor noted that the patient had CHF and prescribed diuretics._  _(“CHF” = “Congestive Heart Failure” but could also mean “Congenital Hepatic Fibrosis.”)_
3) Drug name vs. brand name
	- _He was prescribed acetaminophen (Tylenol) for his headache._  _(Two names for the same drug, system must link them.)_
4) Temporal expression as medical entity context:
	- _Her hypertension worsened after six months of discontinuing therapy._  _(“six months” ties to clinical event.)_
5) Negation handling:
	- _The patient denies any history of diabetes or hypertension._  _(Entities appear but should be marked as negated.)_
6) Numeric and unit-related entity:
	- _Her blood pressure was 180/95 mmHg upon admission._  _(Mixed numeric + unit + medical measurement.)_
7) Rare or uncommon terminology:
	- _The biopsy showed Langerhans cell histiocytosis._  _(Low-frequency entity, challenging for NER models without domain training.)_

Odrzuciłam je dlatego, że wydają mi się niezbyt wymagające dla LLMów i wydają się nie wpływać na budowę metryki. Do rozważenie _negation handling_ .

TODO
1) Zdecydować się na 3 problematyczne przypadki, które chcemy rozwiązać. Przygotować po 3 przykłady dla każdego z takich przypadków.
2) Rozszerzyć benchmark do 50/100 przykładów. Uzupełnić go o przykłady, uwzględniające:
	- zaimki osobowe (my head hurts -> head hurts) - idealne przypadki, to encje bez zaimków
	- encje rozłączne
	- encje zagnieżdżone (czy znajdę jakiś dobry przykład?)
	- rozbicie encji (spuchnięty i bolący nadgarstek -> rozbicie na dwie encje: spuchnięty nadgarstek i bolący nadgarstek)
	- zamienienie miejscami słów: głowa mnie boli == boli mnie głowa
3) Przygotować test dla modelów embeddingowych i je przetestować:
	- zbiór 100 trójek synonimów, takich, że A jest bliżej do B niż do C
	- gemma3 albo qwen3?
	- mulitanguage, matrioszka
4) Dalej bawić się z tym drugim podejściem


28.08.2025
Następne spotkanie 18.09 godz 11:30
TODO
1) Przygotować "benchmark" - kilka przykładów co jest bardziej preferowane od czego:
		|Anna i Jan Kowalscy| < |Anna| |Jan Kowalscy| < |Anna Kowalska| |Jan Kowalski| < |Anna Kowalscy| |Jan Kowalscy| 
2) Dobracować metrykę, aby:
	   - spełniała zbiór benchmarkowy,
	   - działała na lokalnym embeddingu (do sprawdzenia gemma3, oraz zbiór subtokenów (eg. fasttext)) - wszystko co odpali się na ollamie jest ok,
	   - możemy bazować na wyciągnięciu metryk do listy,
	   - czy zależy mi również na wskazaniu granic danej encji?
3) Zaproponować metrykę dla podejścia w którym mamy do czynienia z multilabelingiem kolejnych słów


26.06.2025

Questions

1) [dataset_generation.ipynb] Which sentence tokenizer use?

	- NLTK and Spacy do not recognize following sentence as one:
	
	"Due to my arthritis getting progressively worse, to the point where I am in tears with the agony, gp's started me on 75 twice a day and I have to take it. every day for the next month to see how I get on, here goes."
	
	- Llama 3 recognize it as one sentence, but process text far more slower than tokenizers. Nevertheless I have a lot of time to run the whole pipeline and wait for the results.

2) [Organizational] How do want to arrange meetings during summer?

Notes from meeting
1) When Llama ends its task, send the sample from dataset.
2) Check if Cadec has nested and discontinuous entities.
3) NLTK/Spacy should be enough for sentence separation.
4) July dedicated for discovering metrics.
5) Data on campus - wstawiono nagrania https://www.youtube.com/@wmiiuam6164/videos