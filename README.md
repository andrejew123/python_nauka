# Ogólne założenia.
Już na tym etapie będziemy sprawdzać szybkość wykonywania Waszych skryptów. Postarajcie się tworzyć je tak, by działały jak najszybciej.

Aby sprawdzić jak Wasz skrypt działa, odpalacie jedynie skrypt timer.py, a on sprawdzi resztę.

Wersja pythona >= 3.6.5

## Pamiętaj!!!
Edytujesz pliki zadanie1.py, zadanie2.py itd. możesz dorabiać różne do tego funkcje, ale nie zmieniaj nazwy obecnie istniejącej. To ma być Twoja funkcja budująca, na podstawie której będziesz w returnie zwracać rezultat.


# Zadanie 1.
Funkcja przyjmuje dwa argumenty:

1. Obecny wiek ojca (lata)
2. Obecny wiek syna (lata)

Niech obliczy, ile lat temu ojciec miał dwa razy tyle lat ile syn w chwili obecnej (albo, za ile lat
będzie dwukrotnie starszy)

# Zadanie 2.
Funkcja przyjmuje jeden argument:

1. String

Twoim zadaniem jest usunąć wszystkie duplikaty ze stringa pozostawiając pierwsze
pojawienie się tego wyrazu.

### Input:
```python
string = ‘alpha beta beta gamma gamma gamma delta gamma delta beta alpha gamma’
```
### Output:
```python
‘alpha beta gamma delta’
```
# Zadanie 3.
Funkcja przyjmuje jeden argument:

1. n będący liczbą o nieokreślonej wielkości

Twoim zadaniem jest stworzenie funkcji generującej trójkąt Pascala do n’tego poziomu.
### Input:
```python
n = 4
```
### Output:
```python
[[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
```
# Zadanie 4.
Funkcja przyjmuje jeden argument:

1. n będący liczbą o nieokreślonej wielkości. (liczba krzeseł)

W poczekalni jest n liczba krzeseł w rzędzie. Krzesła są ponumerowane od 1 do n. Gdzie 1
jest najbliżej wejścia (które równocześnie jest wyjściem).

Z jakiegoś powodu, ludzie kierują się wyborem krzeseł w poniższy sposób:
1. Znaleźć miejsce jak najdalej od innej osoby jak to możliwe.
2. Znaleźć miejsce jak najbliżej wyjścia.

Dla 10 krzeseł i pacjentów wygląda to następująco.

Krzesło 1 2 3 4 5 6 7 8 9 10

Pacjent 1 7 5 8 3 9 4 6 10 2

Twoim zadaniem jest znalezienie ostatniego krzesła zajętego przez pacjenta jako int.

# Zadanie 5.
Funkcja przyjmuje jeden argument:
1. string będący sentencją lub lista stringów zawierających sentencje.

Firma marketingowa spędza mnóstwo czasu na tworzeniu hashtagów, pomóż im stworzyć
Hashtag generator!

Masz założenia:
1. output musi zaczynać się od (#)
2. Wszystkie wyrazy muszą zaczynać się z dużej litery!
3. Jeżeli finalny rezultat ma więcej niż 140 znaków powinno zwrócić False
4. Jeżeli input jest pusty musi zwrócić False
5. Jeżeli argument jest listą, ma zwrócić rezultat w postaci stringa, który zostanie
wyprintowany.
### Input:
```python
“Siema budujemy hashtag generator”
```
### Output
```python
“#SiemaBudujemyHashtagGenerator”
```
### Input
```python
“No i       bedzie           fajny”
```
### Output
```python
“#NoIBedzieFajny”
```
### Input
```python
“"
```
### Output
```python
False
```
### Input
```python
[“Taki tam”, “Kolejny bedzie”, “hashtag bys miala co robić”, “”]
```
### Output
```python
“#TakiTam”
“#KolejnyBedzie”
“#HashtagBysMialaCoRobić”
False
```
