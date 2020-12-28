# Đa hình(polymorphism) in Python
# các hàm có tính đa hình được tích hợp sẵn trong python
print("Câu 1: Ví dụ về các hàm có tính đa hình được tích hợp sẵn trong python")
print(len("Hello Word"))
print(len([20, "Hello", 30, 40, 0, 5, 30]))

# hàm có tính đa hình do người dùng tự định nghĩa
def add(x, y, z):
    return "Sum is %d" %(x + y + z)
    # return f"Sum is {x + y + z}"

def main1():
    print("\nCâu 2: Ví dụ hàm có tính đa hình do người dùng tự định nghĩa\n")
    x = int(input("Enter x: "))
    y = int(input("Enter y: "))
    z = int(input("Enter z: "))

    print(add(x, y, z))

if __name__=="__main__":
    main1()

# đa hình với các phương thức của lớp
class VietNam:
    def capital(self):
        return "Ha Noi is the capital of Viet Nam."
    
    def language(self):
        return "Vietnamese is the most widely spoken language of Viet Nam."

    def type(self):
        return "Viet Nam is a developing conutry."
    
class USA:
    def capital(self):
        return "Washington, D.C. is the capital of USA"
    
    def language(self):
        return "English is the primary language of USA."

    def type(self):
        return "USA is a developed country."

def main2():
    print("\nCâu 3: Đa hình với các phương thức của lớp\n")

    obj1 = VietNam()
    obj2 = USA()

    for i in (obj1, obj2):
        print(i.capital())
        print(i.language())
        print(i.type())

if __name__=="__main__":
    main2()

# Đa hình và kế thừa
class Bird:
    def __init__(self, str1):
        self.str1 = str1
    
    def getString(self):
        return self.str1
    
    def setFlight(self, str2):
        self.str2 = str2

    def getFlight(self):
        return self.str2
    
class sparrow(Bird):
    def setFlight(self, str2, str3):
        Bird.str2 = str2
        self.str3 = str3

    def getFlight(self):
        return self.str3

class ostrich(Bird):
    def setFlight(self, str2, str4):
        Bird.str2 = str2
        self.str4 = str4
    
    def getFlight(self):
        return self.str4

def main3():
    str1 = input("Enter str1: ")
    str2 = input("Enter str2: ")
    str3 = input("Enter str3: ")
    str4 = input("Enter str4: ")

    obj1 = Bird(str1)
    obj2 = sparrow(str1)
    obj3 = ostrich(str1)

    print(obj1.getString())
    obj1.setFlight(str2)
    print("%s\n" %(obj1.getFlight()))

    print(obj2.getString())
    obj2.setFlight(str2, str3)
    print(obj2.getFlight())

    print(obj3.getString())
    obj3.setFlight(str2, str4)
    print(obj3.getFlight())

if __name__=="__main__":
    main3()




