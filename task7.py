from itertools import count
from math import factorial
n = int(input('Введите число:'))


def generator():
    for el in count(1):
        yield factorial(n)


fibo_gen = generator()
print(fibo_gen)

