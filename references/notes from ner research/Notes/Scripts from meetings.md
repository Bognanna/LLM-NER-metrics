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