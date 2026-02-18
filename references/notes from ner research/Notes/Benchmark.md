### Celem benchmarku jest przetestowanie działania metryki. Na chwilę, każda przykład w benchmarku składa się z 4 pól:

"Sentence", "Perfect", "Good", "OK"
- Czy powinnam się na czymś wzorować tworząc benchmark?
- **Odp:** Nie, gdyż nie ma na czym.
- Czy nie powinnam się pozbyć "Sentence"? Teoretycznie dla sprawdzenia działania metryki potrzebuję jedynie zbioru gold_entites oraz zbiorów predicted_entities.
- **Odp:** Tak, sentence nam nie jest do niczego potrzebne.
- Co z tagami i granicami? Problem NER uwzględnia nie tylko wykrycie jakiejś encji, ale przypisanie jej również etykiety oraz zaznaczenie granic:
		tak wyglądają przykładowe dane dla jednego z paperów, które czytałam: {"doc_key": "data/train/20807-104709-ECHO_REPORT.txt_1047_1094", "sentences": [["The", "mitral", "valve", "leaflets", "are", "mildly", "thickened", "."]], "ner": [[[1, 1, "Disease_Disorder"], [3, 3, "Disease_Disorder"], [6, 6, "Disease_Disorder"]]], "relations": [[[1, 1, 3, 3, "Combined"], [1, 1, 6, 6, "Combined"], [3, 3, 1, 1, "Combined"], [3, 3, 6, 6, "Combined"], [6, 6, 1, 1, "Combined"], [6, 6, 3, 3, "Combined"]]], "dep": [{"nodes": [[3], [3], [3], [0, 1, 2, 6], [6], [6], [3, 4, 5, 7], [6]]}]}
	Zauważmy, że w tym przypadku w ogóle nie padają słowa z encji, a jedynie granice tych słów i tagi. Encje uznaje się, za dobrze przewidzianą, jeżeli zarówno jest ten sam label oraz granice:
		- sprawdzanie granic wydaje się mijać z celem w przypadku encji generowanych przez LLM
		- dopisanie tagów wydaje się być formalnością - w przypadku benchmarku dałabym losowe abstrakcyjne oznaczenia np. T1, T2, T3 i dała kilka przykładów w których dla "Good" i "Ok" są przypisane inne tagi niż dla "Perfect" - w większości przykładów olałabym kwestię tagów i zawsze dawała poprawne, żeby skupić się na tym jak semantycznie daje sobie radę metryka
- **Odp:** Nie ma potrzeby uwzględniania granic.
- Czy jest jakieś nazewnictwo, którego powinnam się trzymać, nazywając poszczególne pola w benchmarku? Czy może zostać "Perfect", "Good", "OK", a może powinnam przejść na "Ground_Truth", "Predicted_1", "Predicted_2", "Predicted_3" ?

- **Uwagi**: 
1) 3 benchmarki? Same dobre tagi, same dobre zdania, mix dobrych i złych tagów i zdań.

- Jeżeli zostawiamy zdania, to przechodzę do punktu niżej:

### Na ten moment benchmark jest stworzony tak, że sugeruje iż najlepsze encje, to te słowo w słowo do tego co jest w zdaniu. Czy takie podejście jest poprawne?
- Czy dążę do tego, żeby punktować niezmienioną kolejność słów w encji?
	{"Sentence": "body swelling, wrists","Perfect": ["body swelling", "swelling wrists"],"Good": ["swelling body", "swelling wrists"], "Ok": ["swelling body", "swelling wrist"]},
- Czy opisowe encje powinny zostać skrócone? episodes of nausea -> nausea episodes
	{"Sentence": "episodes of nausea and vomiting","Perfect": ["episodes of nausea", "episodes of vomiting"],"Good": ["nausea", "vomiting"],"Ok": ["nausea and vomiting"]},
	{"Sentence": "the muscle and joints in my angles hurt","Perfect": ["the muscle in the angles hurt", "joints in the angles hurt"],"Good": ["the muscle hurt", "joints in my angles hurt"], "Ok": ["muscle ache", "joints ache"]},
- Couldn't - czy tu powinno być jakieś inne słowo w innym czasie?
	 {"Sentence": "i couldnt pass urine,when i eventualy did it was full of blood","Perfect": ["couldnt pass urine", "urine full of blood"],"Good": ["couldnt pass urine", "full of blood"], "Ok": ["urine", "blood"]},
- Pozostawiać dookreślenia czy też nie? (sometimes/ slightly)
	 {"Sentence": "I did take my blood pressure today though, and it was slightly elevated from the norm.","Perfect": ["blood pressure slightly elevated"],"Good": ["blood pressure"], "Ok": ["blood", "pressure"]},
      {"Sentence": "extreme pain in both shoulders, sometimes in the neck","Perfect": ["extreme pain in both shoulders", "extreme pain in the neck"],"Good": ["extreme pain in shoulders", "extreme pain in the neck"], "Ok": ["extreme pain", "shoulders", "neck"]},
- Czy powinnam korzystać z jakiegoś standardu znaków/słów? Tutaj encja z & zamiast and:
   {"Sentence": "Weak & wobbley ankles","Perfect": ["Weak & wobbley ankles"],"Good": ["Weak and wobbley ankles"], "Ok": ["Weak ankles", "wobbley ankles"]},
