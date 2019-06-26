def check_duplicates(sentence):
    x = []
    [x.append(i) for i in sentence.split(" ") if i not in x ]
    return ' '.join(x)

assert check_duplicates("alpha beta beta gamma gamma gamma delta gamma delta beta alpha gamma") == 'alpha beta gamma delta'
# print(check_duplicates("alpha beta beta gamma gamma gamma delta gamma delta beta alpha gamma"))