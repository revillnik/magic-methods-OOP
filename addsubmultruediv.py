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
        s = self.chek_in_operation(other)
        return Number(self.value + s)

    def __radd__(self, other):
        return self + other

    def __iadd__(self, other):
        s = self.chek_in_operation(other)
        self.value = self.value + s
        return self

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

    def __sub__(self, other):
        s = self.chek_in_operation(other)
        return Number(self.value - s)

    def __rsub__(self, other):
        s = self.chek_in_operation(other)
        return Number(s - self.value)

    def __isub__(self, other):
        s = self.chek_in_operation(other)
        self.value = self.value - s
        return self

    def __mul__(self, other):
        s = self.chek_in_operation(other)
        return Number(self.value * s)

    def __rmul__(self, other):
        return self * other

    def __imul__(self, other):
        s = self.chek_in_operation(other)
        self.value = self.value * s
        return self

    def __truediv__(self, other):
        s = self.chek_in_operation(other)
        return Number(self.value / s)

    def __rtruediv__(self, other):
        s = self.chek_in_operation(other)
        return Number(s / self.value)

    def __itruediv__(self, other):
        s = self.chek_in_operation(other)
        self.value = self.value / s
        return self

    def __floordiv__(self, other):
        s = self.chek_in_operation(other)
        return Number(self.value // s)

    def __rfloordiv__(self, other):
        s = self.chek_in_operation(other)
        return Number(s // self.value)

    def __ifloordiv__(self, other):
        s = self.chek_in_operation(other)
        self.value = self.value // s
        return self

    def __mod__(self, other):
        s = self.chek_in_operation(other)
        return Number(self.value % s)

    def __rmod__(self, other):
        s = self.chek_in_operation(other)
        return Number(s % self.value)

    def __imod__(self, other):
        s = self.chek_in_operation(other)
        self.value = self.value % s
        return self


a = Number(3)
b = Number(4)
a %= 3
print(a.__dict__)
