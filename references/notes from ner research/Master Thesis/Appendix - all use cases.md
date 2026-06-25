Use case 1.4
```
SENTENCE: Menstrual cramps present with or without vaginal bleeding.
GOLD_ENTITIES: [['menstrual cramps with vaginal bleeding', 'Symptom'], ['menstrual cramps without vaginal bleeding', 'Symptom']]
0-SHOT: [['menstrual cramps', 'Symptom'], ['vaginal bleeding', 'Symptom']]
FEW-SHOT: [['menstrual cramps', 'Symptom'], ['vaginal bleeding', 'Symptom']]
```

```
CDE: 0.14882194156765166 0.14882194156765166
EF: 0.0 0.0
CDEF-0.5: 0.9395719209682687 0.9395719209682687
CDEF-1.0: 0.9613567746519021 0.9613567746519021
PREC: 0.0 0.0
REC: 0.0 0.0
F1: 0 0 0 0
F1-SOFT: 1.0 1.0

```

Use case 1.5
```
SENTENCE: After the second pill the same progression of symptoms only now the abdominal gas,cramps and pain would be with me all day.
GOLD_ENTITIES: [['abdominal gas', 'Symptom'], ['abdominal cramps', 'Symptom'], ['abdominal pain', 'Symptom']]
0-SHOT: [['abdominal gas', 'Symptom'], ['cramps', 'Symptom'], ['pain', 'Symptom']]
FEW-SHOT: [['abdominal gas', 'Symptom'], ['cramps', 'Symptom'], ['pain', 'Symptom']]
```

```
CDE: 0.1263790903944034 0.1263790903944034
EF: 0.0 0.0
CDEF-0.5: 0.948801319576102 0.948801319576102
CDEF-1.0: 0.9673744299342727 0.9673744299342727
PREC: 0.3333333333333333 0.3333333333333333
REC: 0.3333333333333333 0.3333333333333333
F1: 0.3333333333333333 0.3333333333333333
F1-SOFT: 0.6666666666666666 0.6666666666666666

```


Use case 2.3

```

SENTENCE: The boy was diagnosed with a very bad lung infection that affected the lower part of his right lung.
GOLD_ENTITIES: [['lung infection of the lower part of right lung', 'Disease']]
0-SHOT: [['lung infection', 'Disease']]
FEW-SHOT: [['lung infection', 'Disease']]
```

```
CDE: 0.18487491599217287 0.18487491599217287
EF: 0.0 0.0
CDEF-0.5: 0.924657132982076 0.924657132982076
CDEF-1.0: 0.9515415846345043 0.9515415846345043
PREC: 0.0 0.0
REC: 0.0 0.0
F1: 0.0 0.0
F1-SOFT: 0.0 0.0
```
```