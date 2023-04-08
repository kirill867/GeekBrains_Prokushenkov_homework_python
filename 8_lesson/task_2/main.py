"""
2. Задание на закрепление знаний по модулю json. Есть файл orders
в формате JSON с информацией о заказах. Написать скрипт, автоматизирующий
его заполнение данными.

Для этого:
Создать функцию write_order_to_json(), в которую передается
5 параметров — товар (item), количество (quantity), цена (price),
покупатель (buyer), дата (date). Функция должна предусматривать запись
данных в виде словаря в файл orders.json. При записи данных указать
величину отступа в 4 пробельных символа;
Проверить работу программы через вызов функции write_order_to_json()
с передачей в нее значений каждого параметра.

ПРОШУ ВАС НЕ УДАЛЯТЬ ИСХОДНЫЙ JSON-ФАЙЛ
ПРИМЕР ТОГО, ЧТО ДОЛЖНО ПОЛУЧИТЬСЯ

{
    "orders": []
}

вам нужно подгрузить JSON-объект
и достучаться до списка, который и нужно пополнять
а потом сохранять все в файл
"""


import json


class Orders:
    def __init__(self, orders_file):
        self.orders_file = orders_file
        self.order_list = []
        self.load_orders()

    def __str__(self):
        res = ''
        for order in self.order_list:
            res += f"Товар: {order['item']}\n" \
                   f"Количество: {order['quantity']}\n" \
                   f"Цена: {order['price']}\n" \
                   f"Покупатель: {order['buyer']}\n" \
                   f"Дата: {order['date']}\n\n"
        return res

    def add_order(self, order):
        self.order_list.append(order)

    def data_to_file(self):
        return {'orders': self.order_list}

    def load_orders(self):
        with open(self.orders_file) as orders_stream:
            data = json.load(orders_stream)
            for order in data['orders']:
                self.order_list.append(order)

    def write_order_to_json(self, order_data, res_file="my_orders.json"):
        self.add_order(order_data)
        with open(res_file, "w") as orders_stream:
            json.dump(self.data_to_file(), orders_stream, indent=4)
            print("JSON записан")


obj = Orders("orders.json")

obj.write_order_to_json({'item': 'компьютер',
                         'quantity': 30,
                         'price': 50000,
                         'buyer': 'Peter',
                         'date': '11.02.2023'})
