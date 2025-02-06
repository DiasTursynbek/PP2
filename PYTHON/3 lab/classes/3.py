class Shape:
    def __init__(self):
        pass  

class Rectangle(Shape):
    def __init__(self, length, width):
        super().__init__()  
        self.length = length  
        self.width = width  

    def area(self):
        return self.length * self.width

rect = Rectangle(4, 5)

print(rect.area())  