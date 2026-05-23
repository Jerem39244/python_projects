class Shape:
    def __init__(self, width, height):
        self.width = width
        self.height = height

class Rectangle(Shape):
    def area(self):
        return self.width * self.height

class Triangle(Shape):
    def area(self):
        return 0.5 * self.width * self.height


width = int(input("What is the width: "))
height = int(input("What is the height: "))
shape_chosen = input("What shape do you want? Enter r for rectangle or t for triangle: ").lower()


if shape_chosen == 'r':
    my_rect = Rectangle(width, height)
    print(f"Rectangle area: {my_rect.area()}")
elif shape_chosen == 't':
    my_tri = Triangle(width, height)
    print(f"Triangle area: {my_tri.area()}")
else:
    print("Please choose t or r")
