# Zadanie 1 -- Dziwna permutacja.
Na wstępie otrzymujesz wektory, których długość jest od 3 do 20, wektorów może być kilka, tak więc Twoja funkcja powinna przyjmować *args.

Z tych wektorów masz zwrócić inta, który będzie oznaczał ile jest możliwych na nich permutacji, z tym że...

Permutacja ma być niepełna czyli. Otrzymujesz 2 wektory:
```python
Wektor1 = (1,2,3)
Wektor2 = (11,12,13)
```
Permutacje zgodne to:
```python
[(1,2,3,11,12,13), (1,2,11,12,3,13), (1,11,2,3,12,13), (1,11,2,12,3,13), (11,12,13,1,2,3), (11,12,1,2,13,3), (11,1,12,13,2,3), (11,1,12,2,13,3)]
```
Tak więc wynikiem dla Wektora1 oraz 2 będzie 8.

### Założenia
1. Wartości z nie mogą się przeplatać tzn. nie może być np: (3,2,11,13,12,1), musi zostać zachowany ciąg liczb z wektorów, który niekoniecznie ułożony jest od najmniejszego do największego.
2. Mają występować ciągi n-elementowe np. (1,2,11,12...) Gdzie jak widzisz występuje 1 oraz 2 ale tuż po nich z tej samej pozycji dodawane są wartości z wektora2.
3. Maksymalna możliwa liczba wektorów: 5
4. Maksymalna długość pojedynczego wektora: 20

### Dodatkowo
Napisz proof of concept swojej kombinacji rozwiązania tego zadania.

# Zadanie 2 -- Liczby pierwsze
Stwórz funkcję zwracającą sumę liczb pierwszych poniżej lub równej argumentowi. n może być na prawdę duże ;-)

### Przykład
```python
n = 10
2 + 3 + 5 + 7 = 17
```
### Output
```python
17
```
# Zadanie 3 -- Kalkulator po literkach
Stwórz klasę, która będzie obsługiwać kalkulator literkowy.

d - dodaj 1 (na starcie jest 0)

o - odejmij 1

p - weź do kwadratu

w - wypluj (dodaj do listy obecna wartość)

* niepoprawne wartości powinny zostać zignorowane

### Przykład
```python
jakasklasa.funkcjawewnatrz("dddpowpw") ==> [8, 64]
```
# Zadanie 4. -- Zbuduj drzewko
Masz zaimplementować drzewko używając dict'ów, gdzie:
1. Klucze są prefixami
2. Wartość wynosi None lub kontynuacja drzewka

### Przykład
```python
>>> funkcja_budujaca_drzewko("trie")
{'t': {'tr': {'tri': {'trie': None}}}}
>>> funkcja_budujaca_drzewko("A","to", "tea", "ted", "ten", "i", "in", "inn")
{'A': None, 't': {'to': None, 'te': {'tea': None, 'ted': None, 'ten': None}}, 'i': {'in': {'inn': None}}}
>>> funkcja_budujaca_drzewko("true", "trust")
{'t': {'tr': {'tru': {'true': None, 'trus': {'trust': None}}}}}
```
# Zadanie 5. -- Piwomida.
Firma w której pracujesz przekazała pracownikom X pieniedzy na zabawę, stwierdziliście, że kupicie za wszystko piwa po cenie Y, z których zbudujecie piwną piramidę.

Dla przykładu, dostaliście od szefa 220 złotych, gdzie jedno piwo kupujecie za 4 złote. W efekcie funkcja powinna wypluć liczbę 5, ponieważ 5 pięter możemy z nich zbudować (licząc od góry każde piętro ma piw: 1,4,9,16,25).

Przemyśl dokładnie założenia jakie powinna spełniać ta funkcja i spraw by była odporna na błędy wywoławcze.

Dodatkowo napisz do tej funkcji generator, który wygeneruje 1000 X i Y, a następnie 1000 razy wywoła tę funkcję. W X ma znajdować się wartość od -100 do 100000000, Y ma być w przedziale -1 do 5.

# Zadanie 6. -- Trójkąt.

Budujesz n-piętrowy trójkąt. np. 5 pięter wygląda tak:

----------

            1

          2 4 2

        3 6 9 6 3

      4 8 12 16 12 8 4

    5 10 15 20 25 20 15 10 5

----------

Chodzi o to, ze dane n pietro dodaje do siebie n az uzyska n^2, a nastepnie zmniejsza sie o n az uzyska ponownie wartosc rowna danemu piętru.

Twoim zadaniem będzie obliczenie dla n'tego piętra trzech rzeczy:

1. Całkowita suma

2. Suma liczb parzystych

3. Suma liczb nieparzystych

Które zawarte będą w Twojej wynikowej liscie, gdzie [Calkowita suma, Suma liczb parzystych, Suma liczb nieparzystych].

### Przyklad
```python
>>> multiplies(1)

[1, 0, 1]

>>> multiplies(2)

[9, 8, 1]

>>> multiplies(3)

[36, 20, 16]
```
Pamietaj! chcialbym aby to zadanie bylo rozwalone matematycznie, wiec postaraj sie znalezc jakies logiczne rozwiazanie. Dla n = 10000000 ma się wykonywać poniżej 10 sekund. Zaś dla 1000000 poniżej sekundy.

