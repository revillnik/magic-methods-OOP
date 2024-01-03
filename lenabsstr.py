class Animals:
    def __init__(self, name):
        self.check_name(name)
        self.name = name

    @classmethod
    def check_name(self, name):
        if type(name) != str:
            raise TypeError("Имя должно быть строкой из букв")

    def __str__(self):
        print(f"Имя кошки: {self.name}")

cat = Animals("Lack")
print(cat)

class Point:
    def __init__(self, *args):
        self.coord = args

    def __len__(self):
        return len(self.coord)

    def __abs__(self):
        return list(map(abs, self.coord))

a = Point(1, -2, 3,1)
print(len(a))
print(abs(a))
