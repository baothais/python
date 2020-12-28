from math import pi
class Circle:
    # ham khoi tao
    def __init__(self, r):
        self.r = r
    # ham tinh dien tich
    def printDienTich(self):
        return '{:.2f}'.format(self.r**2*pi)

if __name__=="__main__":
    circle = Circle(int(input()))
    print(circle.printDienTich())

class Hinhchunhat:
    def __init__(self, cd, cr):
        self.cd = cd
        self.cr = cr
    def dientich(self):
        return self.cd*self.cr

if __name__=="__main__":
    hcm = Hinhchunhat(int(input()), int(input()))
    print(hcm.dientich())

class Shape:
    def __init__(self, w):
        self.w = w
    def area(self):
        return 0

class Square(Shape):
    def __init__(self, w, l):
        Shape.__init__(self, w)
        self.l = l
    def area(self):
        return self.w*self.l

if __name__=="__main__":
    Square = Square(int(input()), int(input()))
    print(Square.area())

try:
    raise RuntimeError("something wrong")
except:
    raise

class RuntimeError(Exception):
    def __init__(self, mismatch):
        Exception.__init__(self, mismatch)
try:
    print ("And now, the Vocational Guidance Counsellor Sketch.")
    raise RuntimeError("Does not have proper hat")
    print ("This print statement will not be reached.")
except RuntimeError as problem:
    print ("Vocation problem: {0}".format(problem))

class ZeroDivisionError(Exception):
    def __init__(self, mismatch):
        Exception.__init__(self, mismatch)
try:
    A = 5/0
    raise ZeroDivisionError("division by zero")
    print("I think so too")
except ZeroDivisionError as problem:
    print(f'something wrong: {problem}')







