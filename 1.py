# реализовать дескрипторы для любых двух классов

class NonString:
    def __set__(self, instance, value):
        try:
            int(value)
        except ValueError:
            raise ValueError("Введена строка, ожидалось чсило")
        instance.__dict__[self.my_attr] = value

    def __set_name__(self, owner, my_attr):
        self.my_attr = my_attr


class MathExpression:
    first_coeff = NonString()
    second_coeff = NonString()

    def __init__(self, third_coeff, fourth_coeff, first_coeff=5, second_coeff=6):
        self._third_coeff = third_coeff
        self._fourth_coeff = fourth_coeff
        self.first_coeff = first_coeff
        self.second_coeff = second_coeff

    def math_result(self):
        return self._third_coeff * self._fourth_coeff / self.first_coeff + self.second_coeff


answer = MathExpression(3, 4)
result = answer.math_result()
print(f'ответ: {result}')
