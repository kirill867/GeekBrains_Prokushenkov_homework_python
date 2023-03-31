"""
Задание 4. Найти сумму n элементов следующего ряда чисел:
1 -0.5 0.25 -0.125 ...
Количество элементов (n) вводится с клавиатуры.
Пример:
Введите количество элементов: 3
Количество элементов - 3, их сумма - 0.75
Решите через рекурсию. В задании нельзя применять циклы.
Нужно обойтисть без создания массива!
"""


def sum_of_number(count_elements, sum_of_elements=0, digit=1):
    if count_elements == 0:
        print(f'Суума элементов = {sum_of_elements}')
    else:
        sum_of_elements = sum_of_elements + digit
        digit /= -2
        sum_of_number(count_elements - 1, sum_of_elements, digit)


count_elements = input('Введите количество элементов: ')
try:
    count_elements = int(count_elements)
except ValueError:
    print('Ввели не число')
else:
    (sum_of_number(count_elements))
