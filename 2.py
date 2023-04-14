# реализовать метакласс. позволяющий создавать всегда один и тот же объект класса (см. урок)

class NonNull:
    def __set__(self, instance, value):
        if value == '':
            raise ValueError("Не введено значение")
        instance.__dict__[self.my_attr] = value

    def __set_name__(self, owner, my_attr):
        self.my_attr = my_attr


class Worker:
    name = NonNull()
    surname = NonNull()

    def __init__(self, name, surname, wage, bonus):
        self.name = name
        self.surname = surname
        self.wage = wage
        self.bonus = bonus

    def __str__(self):
        return f'{self.name} {self.surname}, оклад = {self.wage},' \
               f' премия = {self.bonus}'


worker = Worker('Александр', 'Сидоров', 1000, 2000)
print(worker)