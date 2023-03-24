"""
1. Пользователь вводит месяц в виде целого числа от 1 до 12.
Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
Напишите два варианта решения: через list и через dict.

Пример:
Введите номер месяца: 10
Результат через список: Осень
Результат через словарь: Осень
"""

# решение с помощью list


month_list = [[12, 1, 2, 'Зима'], [3, 4, 5, 'Весна'], [6, 7, 8, 'Лето'], [9, 10, 11, 'Осень']]

month_num = int(input('Введите порядковый номер месяца в году (1..12): '))
if month_num in range(1, 13):
    for i, el in enumerate(month_list):
        if month_num in el[0:3]:
            print(f'Введенный номер месяца относится к сезону {el[3]}')
            break
else:
    print('Введен некорректный номер месяца!')

# решение с помощью dict

"""

dict = {1: 'Зима',
        2: 'Зима',
        3: 'Весна',
        4: 'Весна',
        5: 'Весна',
        6: 'Лето',
        7: 'Лето',
        8: 'Лето',
        9: 'Осень',
        10: 'Осень',
        11: 'Осень',
        12: 'Зима'
        }
month = int(input('Номер месяца: '))
i = dict[month]
print(i)

"""
