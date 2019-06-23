import re

def hashtag_generator(argument):
    if len(argument) == 0:
        return False
    elif type(argument) == list:
        for i in argument:
            if len(i) == 0 or len(i) >= 140:
                print('False')
            else:
                print('#' + ''.join(str.title(i)).replace(" ", ""))
    else:
        return '#' + re.sub("[^a-zA-Z]", "", str.title(argument))


hashtag_generator(['Taki tam', 'Kolejny bedzie', 'hashtag bys miala co robić', ''])
assert hashtag_generator('No i       bedzie           fajny') == '#NoIBedzieFajny'
