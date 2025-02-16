import math

sides = int(input("Input number of sides: "))
length = int(input("Input the length of a side: "))

area = round(sides * length**2 / (4 * math.tan(math.pi/sides)))

print(f"The area of the polygon is: {area}")