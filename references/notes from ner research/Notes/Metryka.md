Założenia: 
- analogiczna do F1-score
- zakres wartości <0;1>

Zmieniamy zakres wartości AvgCSE i FEM do <0;1>
A=(AvgCSE+1)/2
B=(FEM+1)/2

Metryka = 2AB/(A+B) = \[(AvgCSE+1)\*(FEM+1)]\\\[(AvgCSE+1)+(FEM+1)]

**Uwagi**:
1) Zamiast F1-score, inspiruj się F-beta score - do rozważenia przetestowanie różnych wartości
2) Aktualnie AvgCSE jest najlepsze dla 1, a FEM dla 0, należy to zmienić robiąc z AvgCSE na przykład dystans cosinusowy, a nie odległość, a w FEM kombinując z wartością bezwzględną.

**-> Average Cosinus Similarity of Embeddings** (AvgCSE)

V1, ..., Vn - wektory embeddingowe złotych encji
X1, ..., Xm - wektory embeddingowe wygenerowanych encji

CSE = Sc(Va, Xb) jeżeli tag(a) == tag(b) inaczej 0
AcgCSE = SUM(CSE)/(|CSE| + epsilon)

 sposób dobrania w pary, zależny od podejścia:
 a) Podejście zachłanne
 - spośród zbiorów encji V, X wybieramy parę (Va, Xb), taką dla której Sc(Va,Xb) jest największe
 - usuwamy Va, Xb z zbiorów V,X
 - sprawdzamy czy któryś ze zbiorów jest pusty:
	 - TAK: kończymy dobieranie w pary, wyliczamy AvgCSE dla powstałych par
	 - NIE: wracamy do punktu (1)
b) Podejście wyczerpujące
- dla wszystkich możliwych kombinacji par V,X wyliczane jest AvgCSE
- wybierana jest kombinacja z największym AvgCSE
 
 Finalna wersja metryki opiera się o podejście zachłanne przy dobieraniu w pary, jednak w pracy przedstawię też podejście brute force, żeby porównać czemu wybrałam pierwszą opcję.

Wartości tej metryki są w granicach <-1;1>

Możliwość zastosowania wygładzenia Laplace'a, aby uniknąć przypadków dzielenia przez 0 przy wyliczaniu średniej.

**Pytanie:** Jak podejść do zapisu metryki w pracy?:
a) zapis matematyczny, tak jak byśmy zapisywali wzór: czy wtedy pomijam opis dobierania w pary?
b) zapis algorytmiczny - pozwala wyjaśnić proces dobierania encji w pary

**Odp:** zapis algorytmiczny jest spoczko

**Pytanie**: Jak podejść do tagów - czy powinny być one elementem wzoru?
**Odp:** Tagi uwzględniane już przed parowaniem, jeżeli encje mają 2 różne tagi, to przypisujemy im wartość podobieństwa 0.

**Uwagi:** 
1) Zastanów się czy chcesz średnią arytmetyczną czy jakąś inną.
2) Do tagów mogą przydać się pydantic enum albo boundary machine learning.

**-> Found Entities Measure** (FEM?)

2\*|wygenerowane_encje|/(|wygenerowane_encje| + |złote_encje|) -1

- <-1;0) LLM wygenerował za mało encji
- 0 LLM wygenerował tyle samo encji co w zbiorze złotych encji
- (0; 1> LLM wygenerował za dużo encji
  
**Pytanie:** Czy mogę zostawić tą metrykę bez żadnej poprawki w mianowniku? Nikt nie będzie liczył jej dla sytuacji gdy nie byłoby ani wygenerowanych_encji ani złotych_encji

**Odp:** Tak, mogę.