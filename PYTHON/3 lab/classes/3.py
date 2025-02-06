class Shape:
    def __init__(self):
        pass  # Базовый класс, который пока не содержит функционала

# Класс Rectangle наследует класс Shape
class Rectangle(Shape):
    def __init__(self, length, width):
        super().__init__()  # Вызываем __init__() родительского класса Shape
        self.length = length  # Сохраняем длину прямоугольника
        self.width = width  # Сохраняем ширину прямоугольника

    def area(self):
        return self.length * self.width  # Вычисляем площадь прямоугольника (длина * ширина)

# Создаем объект прямоугольника с длиной 4 и шириной 5
rect = Rectangle(4, 5)

# Вызываем метод area() и печатаем результат
print(rect.area())  