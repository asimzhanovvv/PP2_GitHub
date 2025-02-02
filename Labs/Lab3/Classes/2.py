class Shape:
    def area(self):
        area = 0
        print("Area of the shape is:" , area)

class Square(Shape):
    def __init__ (self,length):
        self.length = length

    def area(self):
        area = self.length*self.length
        print("Area of the square is: ", area)

example = Square(5)
example.area()

example1 = Shape()
example1.area()