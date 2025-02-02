class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def show(self):
        print (f"({self.x},{self.y})")
    def move(self, x, y):
        self.x += x
        self.y += y
    def dist(self, point):
        return ((self.x - point.x)**2 + (self.y - point.y)**2)**0.5 
    

point1 = Point(1, 2)
point2 = Point(3, 4)

print("Initial coordinates:")
point1.show(), point2.show()

print("\nNew coordinates:")
point1.move(2, 3), point2.move(4, 5)
point1.show(), point2.show()

print("\nDistance between the two points:")
print(point1.dist(point2))