                                        # Hướng đối tượng trong Python
# 7.1 class 
class Person:
    pass
    def printName(self, name, age):
        self.name = name
        self.age = age
        print(f"Name is {self.name}; Age is {self.age}")

def main(): 
    name = input("Enter your name: ")
    age = input("Enter your age: ")
    person_1 = Person()
    person_1.printName(name, age)

if __name__ == "__main__":
    main()

# 7.2 
class PyStudent:
    pass
    def __init__(self, stream, roll):
        self.stream = stream
        self.roll = roll
        print(f"student stream is {self.stream}; student roll is {self.roll}")

PyStudent("CS102", 101)

# 7.3
class ABC:
    #init method or hàm khởi tạo
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    #method
    def printNameX(self):
        return self.name

    def printAgeX(self):
        return self.age

#create name and age are parameters not properties
name = input("Enter your name: ")
age = input("Enter your age: ")

def mainX():
    #create object
    abcd = ABC(name, age)

    # Cách in thứ 1:
    print("Cách in thứ 1:")
    print("Your name and age are ", end= "")
    print(abcd.printNameX(), abcd.printAgeX(), sep= " and ", end="\n\n")

    # Cách in thứ 2:
    print("Cách in thứ 2:")
    print("Your name is: ", abcd.printNameX(), " Your age is: ", abcd.printAgeX(), sep="" ,end="\n\n")

    #Cách in thứ 3:
    print("Cách in thứ 3:")
    print(f"Your name is {abcd.printNameX()} and age is {abcd.printAgeX()}")

if __name__=="__main__":
    mainX()

# 7.4: Instance variable và Class variable
class YourPerson:
    #class variable
    name = "Thái Bảo"

    def __init__(self, age, height):
        # instance variable
        self.age = age
        self.height = height

    def setSex(self, sex):
        self.sex = sex
    
    def getSex(self):
        return self.sex

def mainY():
    age = input("Enter your age: ")
    height = input("Enter your height: ")
    sex = input("Enter your sex: ")

    a = YourPerson(age, height)

    print(f"\nYour age is {a.age} and Your height is {a.height}", end="\n\n")

    a.setSex(sex)
    print(f"Your sex is {a.getSex()}")

if __name__=="__main__":
    mainY()
class CSStudent: 
      
    # Class Variable 
    stream = 'cse'      
      
    # The init method or constructor 
    def __init__(self, roll): 
          
        # Instance Variable 
        self.roll = roll             
  
    # Adds an instance variable  
    def setAddress(self, address): 
        self.address = address 
      
    # Retrieves instance variable     
    def getAddress(self):     
        return self.address    
  
# Driver Code 
def mainZ():
    roll = input("Enter roll: ")
    address = input("Enter your address: ")
    a = CSStudent(roll) 
    a.setAddress(address) 
    print(a.getAddress()) 

if __name__=="__main__":
    mainZ()

# che dấu dữ liệu: sử dụng hai dấu gạch dưới liên tiếp (tức là __) trước tên của các thuộc tính, và các thuộc tính đó sẽ không thể được nhìn thấy trực tiếp, khi ở bên ngoài lớp
class MyClass:
    # hidden member of class
    __hiddenVariable = 10

    # A member method that changes
    # __hiddenVariable
    def add(self, increment):
        self.__hiddenVariable += increment
        return self.__hiddenVariable

def mainO():
    increment = int(input("Enter increment: "))

    a = MyClass()
    print(f"Hello {a.add(increment)}")
    # print(a.__hiddenVariable)             # thuộc tính bị ẩn nên không thể in    
    print(a._MyClass__hiddenVariable)       # sử dụng ._(name class) + tên thuộc tính bị ẩn:   a._MyClass__hiddenVariable để in

if __name__=="__main__":
    mainO()

# in ra các đối tượng
class Test:
    pass
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __repr__(self):
        return "From str method of Test: a is %s, b is %s" %(self.a, self.b)
    
    def __str__(self):
        return "Test a: %s and b: %s" %(self.a, self.b)

def mainK():
    a = input("Enter a: ")
    b = input("Enter b: ")

    x = Test(a, b)
    
    print("Cách in 1:")
    print(x.__repr__())     
    print(x.__str__())

    print("\nCách in thứ 2:")
    print([x])                # this calls __repr__()
    print(x)                  # this calls __str()__

if __name__=="__main__":
    mainK()


















