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

    def __add__(self, other):
        if type(other) not in (int, float, Number):
            raise TypeError(
                "Можно производить операции только с действительными или вещественными числами, либо объектами класса Number"
            )
        s = other
        if type(other) == Number:
            s = other.value
        return Number(self.value + s)

    def __radd__(self, other):
        return self + other

    def __iadd__(self, other):
        if type(other) not in (int, float, Number):
            raise TypeError(
                "Можно производить операции только с действительными или вещественными числами, либо объектами класса Number"
            )
        s = other
        if type(other) == Number:
            s = other.value
        self.value = self.value + s
        return self


a = Number(1)
a += 100
print(a.__dict__)
