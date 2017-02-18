# level 10
from itertools import groupby


def lookandsay(i):
    digits = str(i)
    newdigits = []
    for k, g in groupby(digits):
        newdigits += [sum(1 for _ in g), k]
    return int("".join(map(str, newdigits)))


def conway(i):
    yield i
    while True:
        i = lookandsay(i)
        yield i


cw = conway(1)
for i in range(31):
    elem = str(next(cw))
    print(''.join(elem))
    print('{}{}{}'.format(i, ' - length: ', len(elem)))
