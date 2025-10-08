Zestaw 3 metryk:
- precision & recall dla tego ile w ogóle encji udało się znaleźć LLMowi, czy jakiś nie zhalucynował i nie ma ich za dużo (stopień pokrycia)
- max avg cos sim of embeddings (jakość dopasowania)
	- zamiast max, możliwe jakieś mądrzejsze przeróbki (np. wpierw algorytm zachłanny do dopasowania jak największej liczby embeddingów, a potem max dla reszty)
	- należy sformułować aksjomaty dla metryki, dzięki którym będziemy wiedzieli, czy potrzebny jest np. zakres <-1;1>

1) Wykorzystanie embeddingów:
	- średnia? odległość wychwyconych przez LLM encji od przygotowanych złotych encji
	- wyzwania:
		- metryka zależna od modelu embeddingowego/gotowego zbioru embeddingów
			- w przypadku zbioru: dużo pojęć medycznych, niekoniecznie muszą one występować w zbiorze (np. nazwy leków)
		- kolejność encji może być inna niż występują one w zdaniu:
			- przeszukiwać wszystkie permutacje i szukać dającej najmniejszy błąd?
			- jak to się ma do klątwy wielowymiarowości? 
		- co w przypadku gdy jakiejś encji zabraknie lub dodana zostanie jakaś nadmiarowa?
		- encje mają też często swoje kategorie (np. miejsce, osoba) - należałoby to uwzględnić przy metryce
2) LLM jako sędzia?
		- niby się da, ale to raczej na użytek własny, niż żeby gdzieś opublikować:
			- problem z ewaluacją,
			- brak przewidywalnego zachowania sędziego
3) A co jakby skupić się na granicach i kategoriach?
	- wygenerowane propozycje encji nie są nam potrzebne, jeżeli mamy dostęp do oryginalnego tekstu i otrzymamy od LLM dane dotyczące początku i końca encji oraz typu encji, można też wymagać od LLM, by każdemu z słów przydzielił odpowiednią kategorię (brak, miejsce1, miejsce2, ..., osoba1, osoba2, ...) lub kilka kategorii
	- propozycja promptu:
		- wpierw LLM dostaje całe zdanie wraz z opisanym poleceniem dotyczącym wyłapania w nim encji według schematu
		- następnie po kolei jest pytany o każde słowo w zdaniu i jako odpowiedź zwraca nazwę encji i jej numer (w przypadku kilku encji tego samego typu w zdaniu)
		- jeżeli słowo należy do kilku encji, można pokusić się o multilabeling
	- ewaluacja wtedy może odbywać się 0-1 albo słowo jest przypisane do dobrej kategorii albo nie
	- wyzwania:
		- halucynowanie nazw encji
		- LLM nie są stworzone do liczenia, a tu pojawia się motyw z zliczaniem kolejnych wystąpień tej samej kategorii encji
	- czy ja już tutaj nie odbiegam od pierwotnego celu opracowania metryki?
		- czy ma ona służyć do oceny jakości zwróconych przez LLM encji, czy do oceny tego, czy 2 zdania mają to samo znaczenie, gdyż zawierają encje będące swoimi synonimami?
4) Levenshtein distance
	- wykorzystany dla całego zdania i wykrytych w nim encji


### Podejścia do LLMów przy NER:
#### LLM generuje propozycje encji wraz z etykietami
- odległość embeddingów od siebie
#### LLM przypisuje etykietę do każdego słowa
- levenshtein distance dla ciągu zaproponowanych etykiet
