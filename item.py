import string

class Student:
    def __init__(self, name, age, marks):
        self.name = self.check_name(name)
        self.age = self.check_age(age)
        self.marks = self.check_marks(marks)

    def __getitem__(self, value):
        return self.marks[value]

    def __setitem__(self, key, value):
        if type(value) != int or value < 0:
            raise TypeError('Оценка - целое число больше нуля!')
        self.marks[key] = value
    def __delitem__(self, value):
        del self.marks[value]

    @classmethod
    def check_name(self, name):
        if type(name) != str or name.strip(string.ascii_letters) != "":
            raise TypeError("Имя должно быть строкой из латинских букв")
        else:
            return name

    @classmethod
    def check_age(self, age):
        if type(age) != int or age < 0:
            raise TypeError("Возраст - это целое число больше нуля")
        else:
            return age

    @classmethod
    def check_marks(self, marks):
        if type(marks) != list:
            raise TypeError("Оценки студента должны быть представлены в виде [x,x,x]")
        z = all(list(map(lambda x: type(x) == int and x > 0, marks)))
        if z:
            return marks
        else:
            raise TypeError("Оценки - целые числа больше нуля")


nikita = Student("Nikita", 24, [1, 4, 3, 5])
nikita[1] = 4
del nikita[2]
print(nikita.__dict__)
