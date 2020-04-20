from sys import argv

name, salary, hours, bonus = argv

try:
    salary = int()
    hours = int()
    bonus = int()
    wage = (salary * hours) + bonus
    print('Заработная плата сотрудника: {wage}')
except ValueError:
    print('Введено не правильно.')

