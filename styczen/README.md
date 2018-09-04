# Winda

Zaprojektujesz windę.
Ludzie czekają w kolejce na różnych piętrach, czekając na windę.
Niektórzy ludzie chcą jechać w góre, niektórzy w dół.
Piętro na które chcą jechać reprezentuje ich numer.

# Zasady
### Zasady windy
1. Winda kieruje się tylko w górę i dół.
2. Każde piętro ma dwa guziki - w góre i w dół (oprócz ostatniego i pierwszego piętra)
3. Winda nigdy nie zmienia kierunku do póki nie będzie więcej osób chcących wsiąść / wysiąść w obecnym kierunku.
4. Kiedy jest pusta, winda stara się być mądra, więc:
4.1 Jeżeli jadąc do góry opróżni się, może pojechać wyżej, by zgarnąć osobę z najwyższego piętra.
4.2 Analogicznie jadąc w dół opróżni się i jest pusta, może pojechać niżej, by zgarnąć osobę z najniższego piętra.
5. Winda ma maksymalną pojemność osób podawaną przez użytkownika.
6. Zawołana winda zatrzyma się na piętrze nawet gdy jest pełna i nikt nie wysiada.
7. Jeżeli winda jest pusta i nie ma dodatkowych osób do zabrania, wraca ona na parter.

### Zasady ludzi
1. Ludzie stoją w ,,kolejce" do windy, która kolejno reprezentuje wejście do windy.
2. Wszyscy ludzie mogą jechać w górę i w dół.
3. Tylko ludzie jadący w tym samym kierunku mogą wsiąść do windy.
4. Jeżeli osoba nie może wsiąść do windy bo jest pełna, ponownie naciska guzik w górę lub w dół.

### Zadanie
1. Zabierz wszystkich ludzi na piętra, na których chcą się znaleźć kierując się wyżej wymienionymi zasadami.
2. Zwróć listę wszystkich pięter na których winda się zatrzymała.

### Input
1. queues - jest listą kolejek ludzi na każdym piętrze budynku.
1.1 Wysokość budynku uwarunkowana ilością list wewnątrz.
1.2 0 jest piętrem przy ziemi.
1.3 Nie na wszystkich piętrach są ludzie.
1.4 Numery oznaczają piętra, na które ludzie chcą się dostać.
2. capacity - maksymalna liczba ludzi, która może wsiąść do windy.

### Sprawdzanie parametrów
1. Ludzie chcą dostać się na piętro, które nie istnieje.
2. Ludzie chcą dostać się na piętro, na którym obecnie się znajdują.
3. Budynek ma mniej niż 2 piętra.
4. Piwnice

W pierwszych dwóch wypadkach, taka osoba nie wsiada do windy, pozostaje na swoim piętrze a winda go omija.
W trzecim wypadku, zwracany jest wynik False, ponieważ winda nie ma tutaj racji bytu.
W czwartym przypadku, winda nigdy nie zjeżdża do piwnicy, więc osoba chcąca tam zjechać ląduje na parterze, skąd musi zejść schodami.

### Output
Lista wszystkich pięter na których winda się zatrzymała.

## Przykłady wywołania
queues = ( (),   (),    (5,5,5), (),   (),    (),    () )

winda = Lift(queues, 5)

winda.theLift()

------------
queues = ( (),   (),    (1,1),   (),   (),    (),    () )

winda = Lift(queues, 5)

winda.theLift()

------------
queues = ( (),   (3,),  (4,),    (),   (5,),  (),    () )

winda = Lift(queues, 5)

winda.theLift()

------------
queues = ( (),   (0,),  (),      (),   (2,),  (3,),  () )

winda = Lift(queues, 5)

winda.theLift()

## Output wywołań
[0, 2, 5, 0] 

[0, 2, 1, 0]

[0, 1, 2, 3, 4, 5, 0]

[0, 5, 4, 3, 2, 1, 0]
