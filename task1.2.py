def my_func():
    try:
        salary = int(input('Введите выработку в час:'))
        hours = int(input('Введите часы работы:'))
        bonus = int(input('Введите премию:'))
        wage = (salary * hours) + bonus
        print('Заработная плата сотрудника:', wage)
    except ValueError:
        return print('Введено не правильно.')


print(my_func())