# Python Classes/Objects
# create a class         (để tạo 1 lớp dùng keyword class)
class Myclass:
    pass

print(Myclass)

#create a object         (tạo 1 đối tượng )
class Myclass:
    x = 5

a = Myclass()
print(a.x)

#the __init__()function
class Person:
    pass
    def __init__(self, name, age):
        self.name = name
        self.age = age

name = input("Enter your name: ")
age = input("Enter your age: ")
person_1 = Person(name, age)
print(person_1.name)
print(person_1.age)

def Sum():
    usd = int(input("USD = "))
    vnd = 22 * usd
    print("USD =", usd, "$ và", "VND =", vnd, "đồng")

Sum()

# object method 
class MyPerson:
    pass
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def Myfunc(self):
        print("Hello",self.name)

name = input("Enter your name:")
age = input("Enter your age:")
person_2 = MyPerson(name, age)
person_2.Myfunc()

class Vector2D:
    pass
    def Set(self, x, y):
        self.x = x
        self.y = y
        # print("x:", self.x, "and y:", self.y)

a = input("Enter x: ")
b = input("Enter y: ")
vec = Vector2D()    #vec là đối tượng của lớp Vector2D
vec.Set(a, b)       #truyền gía trị cho hàm Set
print(vec.x)        #in hoàng độ
print(vec.y)        #in tung độ







