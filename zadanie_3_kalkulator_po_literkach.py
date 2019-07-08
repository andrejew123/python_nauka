class KalkulatorPoLiterkach():
    def liczenie_literek(x):
        num = 0
        lista = []
        for i in x:
            if i == "d":
                num = num+1
            elif i == 'o':
                num = num - 1
            elif i == "p":
                num = num ** 2
            elif i == 'w':
                lista.append(num)
        return lista
    
assert KalkulatorPoLiterkach.liczenie_literek("dddpowpw") == [8,64]
