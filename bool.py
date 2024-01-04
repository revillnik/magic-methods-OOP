class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __len__(self):
        return len((self.x, self.y))

    def __bool__(self):
        return any((self.x, self.y))


a = Point(0, 0)
b = Point(10, 2)
if not a:
    print("Данная точка лежит в начале координат")
else:
    print("Данная точка имеет координаты")
print(len(a))