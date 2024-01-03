class Number:
    def __init__(self, value):
        self.check(value)
        self.value = value

    @classmethod
    def check(cls, value):
        if type(value) not in (int, float):
            raise TypeError(
                "Значение может быть действительным или вещественным числом"
            )

    @classmethod
    def chek_in_operation(self, other):
        if type(other) not in (int, float, Number):
            raise TypeError(
                "Можно производить операции только с действительными или вещественными числами, либо объектами класса Number"
            )
        s = other
        if type(other) == Number:
            s = other.value
        return s

    def __eq__(self, other):
        s = self.chek_in_operation(other)
        return self.value == s

    def __lt__(self, other):
        s = self.chek_in_operation(other)
        return self.value < s

    def __le__(self, other):
        s = self.chek_in_operation(other)
        return self.value <= s


a = Number(1)
b = Number(3)
print(a > b, a < b, a == b, a != b, a >= b, a <= b)
