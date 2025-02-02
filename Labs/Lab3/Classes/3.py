class Shape:
    def area(self):
        area = 0
        print("Area of the shape is:" , area)

class Rectangle(Shape):
    def __init__ (self,length,width):
        self.length = length
        self.width = width
    
    def area(self):
        area = self.length*self.width
        return("Area of the rectangle is: ", area) 
        # The Rectangle class has a method which can "compute" the area.
        # compute ≠ print, so we return the area instead of printing it.
    
example = Rectangle(5,4)
print(example.area())

example1 = Shape()
example1.area()
