1. Implementacja
	1. Benchmark
		- [x] Wywalić sentence
		- [x] Dodać tagi, tworząc 3 rodzaje przykładów w benchmarku: test encji (tagi zawsze dobre), test tagów (encje zawsze dobre), test wszystkiego (zarówno tagi jak i encje mogą być błędne)
		- [ ] Poprawić encje: ujednolicenie zaimków (?), ujednolicenie form czasowników (?), ujednolicenie kolejności słów (?)
		- [x] Dodać id do każdego tripla
		- [x] Poprawić test_types
	2. Use Cases
		- [x] Spisać Use Cases
	3. Metryka
		- [x] Fbeta-score zamiast F1-score
		- [x] Ujednolicić miary tak, aby obydwie były najlepsze dla 1 i najgorsze dla 0 (albo odwrotnie)
		- [x] Zaimplementować metrykę w jej ostatecznej formie
		- [x] Poprawić sposób podawania danych do metryk, tak żeby nie było wymagane używanie for in zip
		- [x] Poprawić sposób podawania danych do get_embeddings, tak żeby nie trzeba było pakować encji w listę
	4. Testy
		- [x] Przetestować metrykę w obu wersjach na Use Cases
		- [x] Przeprowadzić testy na benchmarku
		- [x] Zbadaj zachowanie dla beta=0.0 przy mix i sim
		- [x] Dodać do testów use case testy na zwykłych metrykach
		- [x] Porównanie działania metryk na use case
		- [ ] Zaplanować testy na podstawie innych prac
		- [ ] Utworzyć zbiór testowy
		- [ ] Przeprowadzić testy

2. Praca
	1. Abstrakt
	2. Wstęp
	3. Opis problemu NER
	4. Opis podejść do problemu NER
	5. Opis mierzenia jakości rozwiązań 
	6. Wskazanie wad dotychczasowych metryk w odniesieniu do rozwiązań opartych o LLM
	7. Propozycja nowej metryki
	8. Przedstawienie sposobów doboru w pary
	9. Opis prac programistycznych ( ? )
	10. Opis testów wykonanych na metryce
	11. Przedstawienie wyników testów
	12. Podsumowanie
	13. Wskazanie dalszych prac
	14. Deklaracja dotycząca wykorzystania generatywnego AI przy pracach
	15. Inne:
		- [ ] Założyć projekt na overleafie
		- [ ] Dostosować templatkę
		- [ ] Rozpisać strukturę pracy
