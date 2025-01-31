import math  # Импортируем модуль math для вычисления квадратного корня

class Point:
    def __init__(self, x, y):
        self.x = x  # Координата x
        self.y = y  # Координата y

    def show(self):
        print(f"({self.x}, {self.y})")
    def move(self, dx, dy):
        self.x += dx  # Изменяем координату x
        self.y += dy  # Изменяем координату y

    def dist(self, other_point):
        return math.sqrt((self.x - other_point.x) ** 2 + (self.y - other_point.y) ** 2)

# Создание двух точек
p1 = Point(1, 2)  # Точка с координатами (1,2)
p2 = Point(4, 6)  # Точка с координатами (4,6)

# Выводим расстояние между точками
print(p1.dist(p2))  # Ожидаемый вывод: 5.0