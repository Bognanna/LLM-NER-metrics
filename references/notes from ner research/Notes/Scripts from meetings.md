26.02.2025
Do omówienia:
1. Co z abstrakcyjnym przypadkiem, gdy encje składają się z nic nieznaczącego zlepku liter i znaków? Czy badać w ogóle taki przypadek? Tradycyjne metryki dałyby po prostu wartość 0.
2. Czy edytować encje w benchmarku, skoro 1 do 1 pochodzą one z zbioru Cadec? Jak finalnie zedytować encje w benchmarku: ujednolicenie zaimków (?), ujednolicenie form czasowników (?), ujednolicenie kolejności słów (?), skrócenie opisowych form episodes of vomiting vs. vomiting episodes (?), zostawiać określenia np. sligtly (?), jakieś standardowe znaki np. and zamiast & (?)
3. Pisząc na jaką formę powinnam się zdecydować (bezosobowa czy też wszędzie I/We)?


Cel na ten tydzień:
- wyłapać wszystkie kwestie, które potrzebuję żeby kod był dopięty i profesjonalny:
	- pytania dotyczące benchmarku
	- potwierdzenie metryki

11.12.2025
Następne spotkanie 15.01.2025 godz. 11:30
Chcę ustalić do czego dążę, aby uznać pracę za skończoną:
-> dopracowana metryka - czy skupić się na 1, czy może dla pracy lepiej wyjdzie jak zaproponuję jeszcze 2. ? Czy może trzebaby się zastanowić na różnych odmianach tej metryki?
-> testy metryki, porównujące ją z innymi metrykami, na oficjalnych benchmarkach
-> poza benchmarkiem, to utworzyć też use cases (oczekiwania co do tego jak metryka powinna działać)
-> zebranie wszystkiego w pracę (chcę ją pisać po angielsku): wstęp, opis tego jak dotąd mierzono jakość NER, wyjaśnienie dlaczego ma to swoje problemy, przedstawienie metryki i wyjaśnienie jej zasad działania, implementacja metryki + opis prac programistycznych, przedstawienie wyników testów na benchmarku, wnioski, dalsze prace, bibliografia
-> szerszy opis tego, czym jest problem NER, related work - wprowadzenie encji nieciągłych z przykładami, metryki oceny, intent (akt dialogowy, byt w konwersacji - trochę jak encja, ale mniej konkretny np. typ kuchni + preferowana godzina + preferowana data rezerwacji), przedstawienie metryki, informacje o benchmarkach, podsumowanie
-> czym to się różni od paperów, które czytałam? Przecież tam przedstawiano nowe metody, a całość mieściła się z reguły na 14 stronach.


20.11.2025
Następne spotkanie 11.12.2025
-> poprawić benchamrk, tak żeby uwzględniał też tagi, oraz poprawki na mailu
-> na razie olewamy problem healthy/not healthy/ill
-> metrykę zrobić tak jak F1 score - dwa komponenty, a z nich średnia harmoniczna
-> poprawka laplasa (jak w naive bayes) przy dzieleniu przez 0 (https://towardsdatascience.com/laplace-smoothing-in-naive-bayes-algorithm-9c237a8bdece/)

TODO
* poprawić benchmark, tak aby zawierał tagi
* implementacja 2. metryki
* zaproponować metrykę w oparciu o F1 score/ średnią harmoniczną/f-beta score
* dodać poprawkę laplasa tam gdzie jest ryzyko dzielenia przez 0
* porównać dawane wyniki z istniejącymi podejściami
* zaimplementować precission/recall według propozcyji (2a/(a+b))

Do przegadania:
*-> ustawić jakiś treshold podpobieństwa dla którego w ogóle uznajemy 2 encje jako złączone razem? (na potrzeby found entities measure)*
*-> przedstawić aktualny stan drugiego podejścia*
-> będzie trzeba uwzględnić w benchamarku oraz przy metrykach gold_labels, jeżeli chcemy cokolwiek porównywać:
	- gold labels i predicted labels jako osobna lista,
	- podejście 0/1 - jeżeli label jest prawidłowo przypisany, mnożymy miarę podobieństwa * 1, jeżeli nie jest to * 0? <- to podejście oznacza, że nawet jeżeli LLM prawidłowo wskaże span, to jeżeli źle je oznaczy, to będzie otrzymywał najniższy wynik 0 - przypominamy, że skala aktualnie wynosi <-1;1>
-> porównywanie ze sobą metryk:
	- do rozważenia czy wszystko z zakresu <-1;0> nie sprowadzać do 0? Czy nam w ogóle zależy na rozróżnieniu nieskorelowanych ze sobą zdań od tych przeciwnych - albo inna opcja - (x+1)/2
	- zoinks z Ollamą i proponowanymi embeddingami: te o przeciwnym wydawałoby się znaczeniu, mają wartość dodatnią podobieństwa cosinusowego i i tak są bardziej podobne niż te nieskorelowane ze sobą
-> propozycja zmiany metryki liczby znalezionych encji na: 2*|generated|/(|generated|+|gold|) - 1, wtedy zakres metryki będzie wynosił <-1;1>, gdzie wynik <-1;0) oznacza nieznalezione encje, 0 - znalezione, (0;1> zhalucynowane encje - z minusów: gorszy w interpretacji niż poprzedni, z plusów - pozbywamy się +oo z zakresu
- co z dzieleniem przez 0? lepszym podejściem jest danie warunku, że jak 0 to 0, czy dodanie jakiejś mikro wartości do mianownika?


31.10.2025
Następne spotkanie: 13.11.2025 godz. 11:30
1) Problematyczne encje dopiero zostaną przejrzane przez promotora - zagubił się gdzieś mail
2) Możliwe, że benchamark będzie trzeba wzbogacić o jakieś nietypowe przykłady na które chat nie wpadł
3) Aby porównać nowe podejście z starym (max avg cos sim) starczy dać kilka przykładów dla których podejście a gorzej sobie radziło od podejścia b
4) Remisy w tabelce można rozwiązywać losowo (więc w sumie argmax() chyba może być)

TODO:
- porównać dawane wyniki z tradycyjnymi wynikami
- zastanowić się jak przełożyć rezultaty tradycyjnych metryk na rezultaty opracowanej metryki
- <-1; + oo) <- jak to porównać z istniejącym paradygmantem (precission + recall)
- przy porównaniach przyjrzeć się f-beta score
- 2. podejście

Do przegadania:
-> problematyczne encje - czy miał Pan okazję spojrzeć na nie i potwierdzić, że zgadzamy się co do nich
-> użyłam chatu do rozszerzenia benchmarku do ponad 100 przykładów, mam nadzieję, że nie ma tam jakiś poważniejszych błędów, które bym miała przeoczyć
-> podejście 1.1 b daje lepsze rezultaty na benchmarku, czy jest sens zostawiać oba, żeby w pracy magisterskiej dać porównanie czemu b zostało wybrane kosztem a ? (lepiej dać podejście anegdotyczne)
-> do rozważenia przy podejściu 1.1 b: zastanowić się co z remisami w tabelce - zdać się na działanie argmax(), czy może w jakiś inny sposób decydować o tym, które dwie encje zostaną sparowane?






09.10.2025
Następne spotkanie 23.10 godz. 11:30
1) Na negacje istnieje jakiś negation detection algorithm z lat 90', więc problemu chyba nie musimy tykać.
2) Problem z nested wydaje się być dość na siłę - na to może być algorytm, który by rozszerzał istniejące już encje.
3) Pod uwagę bierzemy finalnie problemy: discontinuous, oraz long entity spans <- wydają się fajnie uzupełniać
4) Można przyjrzeć się z ciekawości jak inne metody radziły sobie z sequence tagging w przypadku, gdy jedno słowo było częścią kilku encji np. abdominal w :  "The abdominal gas,cramps and discomfort"
5) Niby jest opcja LLM as a judge, aczkolwiek mi się nie podoba, bo wtedy wyniki dawane przez metrykę przestają byś determistrzyne
6) Wyzwania dla metryki:
	1) Ground Truth = złoty standard,
	2) Utworzyć coś na wzór F1 score, obsługujące precission i recall - liczą liczbę dokładnych encji
	3) Do semantycznego podobieństwa można dać algorytm zahłanny na dobieranie encji w pary

TODO
Wysłać kilka przykładów zdań

18.09.2025
Następne spotkanie 2.10 godz. 11:30

Co z przypadkiem:
"After the second pill the same progression of symptoms only now the abdominal gas,cramps and pain would be with me all day." ?
Adnotatorzy uznali tutaj 2 encje: "abdominal gas", "abdominal cramps and pain"

Ale już później: "The abdominal gas,cramps and discomfort"
Adnotatorzy uznali tutaj 3 encje: "abdominal gas", "abdominal cramps", "abdominal dyscomfort"


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