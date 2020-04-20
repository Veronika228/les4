from itertools import count

for el in count(int(input('Введите начальное число:'))):
    print(el)


from itertools import cycle

for el in cycle(input('Введите список:')):
    print(el)
