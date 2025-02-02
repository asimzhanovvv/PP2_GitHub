class MyClass():
    
    def __init__ (self):
        self.string = ""

    def getString(self):
        self.string = str(input("Enter a string: "))

    def printString(self):
        print(self.string.upper())


example = MyClass()
example.getString()
example.printString()