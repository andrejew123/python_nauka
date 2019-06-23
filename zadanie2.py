def check_duplicates(sentence):
    lista = sentence.split(" ")
    x = []
    for i in lista:
        if i not in x:
            x.append(i)
    return ' '.join(x)

assert check_duplicates("alpha beta beta gamma gamma gamma delta gamma delta beta alpha gamma") == 'alpha beta gamma delta'
