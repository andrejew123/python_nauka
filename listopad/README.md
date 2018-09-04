# Zadanie 1 -- Dziwna permutacja.
Na wstępie otrzymujesz wektory, których długość jest od 3 do 20, wektorów może być kilka, tak więc Twoja funkcja powinna przyjmować *args.

Z tych wektorów masz zwrócić inta, który będzie oznaczał ile jest możliwych na nich permutacji, z tym że...

Permutacja ma być niepełna czyli. Otrzymujesz 2 wektory:

Wektor1 = (1,2,3)

Wektor2 = (11,12,13)

Permutacje zgodne to:

[(1,2,3,11,12,13), (1,2,11,12,3,13), (1,11,2,3,12,13), (1,11,2,12,3,13), (11,12,13,1,2,3), (11,12,1,2,13,3), (11,1,12,13,2,3), (11,1,12,2,13,3)]

Tak więc wynikiem dla Wektora1 oraz 2 będzie 8.

### Założenia
1. Wartości z nie mogą się przeplatać tzn. nie może być np: (3,2,11,13,12,1), musi zostać zachowany ciąg liczb z wektorów, który niekoniecznie ułożony jest od najmniejszego do największego.
2. Mają występować ciągi n-elementowe np. (1,2,11,12...) Gdzie jak widzisz występuje 1 oraz 2 ale tuż po nich z tej samej pozycji dodawane są wartości z wektora2.
3. Maksymalna możliwa liczba wektorów: 5
4. Maksymalna długość pojedynczego wektora: 20
