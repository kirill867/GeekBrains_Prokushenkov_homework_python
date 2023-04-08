"""
1. Задание на закрепление знаний по модулю CSV. Написать скрипт,
осуществляющий выборку определенных данных из файлов info_1.txt, info_2.txt,
info_3.txt и формирующий новый «отчетный» файл в формате CSV.

Для этого:

Создать функцию get_data(), в которой в цикле осуществляется перебор файлов
с данными, их открытие и считывание данных. В этой функции из считанных данных
необходимо с помощью регулярных выражений извлечь значения параметров
«Изготовитель системы», «Название ОС», «Код продукта», «Тип системы».
Значения каждого параметра поместить в соответствующий список. Должно
получиться четыре списка — например, os_prod_list, os_name_list,
os_code_list, os_type_list. В этой же функции создать главный список
для хранения данных отчета — например, main_data — и поместить в него
названия столбцов отчета в виде списка: «Изготовитель системы»,
«Название ОС», «Код продукта», «Тип системы». Значения для этих
столбцов также оформить в виде списка и поместить в файл main_data
(также для каждого файла);

Создать функцию write_to_csv(), в которую передавать ссылку на CSV-файл.
В этой функции реализовать получение данных через вызов функции get_data(),
а также сохранение подготовленных данных в соответствующий CSV-файл;

Пример того, что должно получиться:

Изготовитель системы,Название ОС,Код продукта,Тип системы

1,LENOVO,Windows 7,00971-OEM-1982661-00231,x64-based

2,ACER,Windows 10,00971-OEM-1982661-00231,x64-based

3,DELL,Windows 8.1,00971-OEM-1982661-00231,x86-based

Обязательно проверьте, что у вас получается примерно то же самое.

ПРОШУ ВАС НЕ УДАЛЯТЬ СЛУЖЕБНЫЕ ФАЙЛЫ TXT И ИТОГОВЫЙ ФАЙЛ CSV!!!
"""


import re


class Parcer():
    def __init__(self, source_files, result_file, search_list, ids=True):
        self.source_files = source_files
        self.result_file = result_file
        self._headers = search_list
        self.ids = ids

        self.write_to_csv()

    def get_data(self):
        res = [self._headers]
        count = 1
        for file in self.source_files:
            with open(file) as f_stream:
                file_data = f_stream.read()
                data_line = []
                for el in range(len(res[0])):
                    os_prod_reg = re.compile(rf'{self._headers[el]}:\s*\S*')
                    data_line.append(
                        (os_prod_reg.findall(file_data)[0].split()[-1]))
                if self.ids:
                    data_line.insert(0, str(count))
                res.append(data_line)
            count += 1
        return res

    def write_to_csv(self):
        data = self.get_data()
        with open(self.result_file, "w", encoding="utf8") as file_w:
            for data_string in data:
                file_w.write(','.join(data_string) + "\n")

# в init вызываем write_to_csv()
obj = Parcer(["info_1.txt", "info_2.txt", "info_3.txt"], "my_data_report.csv",
               ["Изготовитель системы", "Название ОС",
                "Код продукта", "Тип системы"])