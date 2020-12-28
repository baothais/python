                                                # Kế thừa
class Person:
    pass
    # constructor
    def __init__(self, name):
        self.name = name
    
    # to get name
    def getName(self):
        return self.name
    
    # to check if this person is employee
    def isEmployee(self):
        return False
    
class Employee(Person):
    # here we return True
    def isEmployee(self):
        # self.nameEmployee = nameEmployee
        return True

def main1():
    print("Câu 1: Kế thừa lớp cha")
    name = input("Enter your name: ")

    emp = Person(name)
    print("%s, %s" %(emp.getName(), emp.isEmployee()))

    name = input("Enter Employee's name: ")

    emp = Employee(name)
    emp.isEmployee()
    print("%s, %s" %(emp.getName(), emp.isEmployee()))

if __name__=="__main__":
    main1()

# kiểm tra 1 lớp có phải là con của lớp khác không ta dùng hàm isssubclass()
class Base(object):
    pass    # Empty class

class Derived(Base):
    pass    # Empty class

def main2():
    print("\nCâu 2: Kiểm tra 1 lớp có phải là con của lớp khác không")
    print(issubclass(Derived, Base))
    print(issubclass(Base, Derived))

    b = Base()
    d = Derived()

    print(isinstance(b, Derived))
    print(isinstance(d, Base))

if __name__=="__main__":
    main2()

# Object class - lớp đối tượng: đối tượng là gốc rễ của tất cả các lớp
# "class Test(object):" <==> "class Test:"

# đa kế thừa
class Base1():
    def __init__(self, str1):
        self.str1 = str1
    
    # def getBase1(self):
    #     return self.str1

class Base2():
    def __init__(self, str2):
        self.str2 = str2
    
    # def getBase2(self):
    #     return self.str2

class Base3(Base1, Base2):
    def __init__(self, str1, str2):
        # calling constructors of Base1 and Base2 classes
        Base1.__init__(self, str1)
        Base2.__init__(self, str2)
    
    def getBase3(self):
        return f"{self.str1} & {self.str2}" 

def main3():
    print("\nCâu 3: Đa kế thừa")
    str1 = input("Enter str1: ")
    str2 = input("Enter str2: ") 

    obj = Base3(str1, str2)
    print(obj.getBase3())

    # print(obj.str1)

if __name__=="__main__":
    main3()

# truy cập các thành viên của lớp cha tại lớp con
# (*)sử dụng tên lớp cha
class Base4(object):
    def __init__(self, x):
        self.x = x
    
class Base5(Base4):
    def __init__(self, x, y):
        # Base4.__init__(self, x)       # C1: kế thừa hàm __init__ của lớp cha.
        Base4.x = x                     # C2: sử dụng tên lớp cha để truy cập thuộc tính lớp cha
        self.y = y 
    
    def getBase5(self):
        return f"x: {Base4.x}; y: {self.y}"

def mainL():
    print("\nCâu 4: Sử dụng tên lớp cha để truy cập các thành viên lớp cha")
    x = input("Enter x: ")
    y = input("Enter y: ")

    obje = Base5(x, y)
    print(obje.getBase5())

if __name__=="__main__":
    mainL()

# (*) sử dụng hàm super()
class Base6(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
class Derived1(Base6):
    def __init__(self, x, y):
        super(Derived1, self).__init__(x, y)
    
    def getDerived1(self):
        return f"x: {self.x}; y: {self.y}"
    
def mainK():
    print("\nCâu 5: Truy cập thành viên lớp cha by hàm super()")
    x = input("Enter x: ")
    y = input("Enter y: ")

    objec = Derived1(x, y)
    print(objec.getDerived1())

if __name__=="__main__":
    mainK()



