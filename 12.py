# class variable & static variable
class CSStudent_1:
    stream = "Hello World"                         # Class variable: bien thuoc ve lop
    
    def __init__(self, name, roll):
        self.name = name                           # Instance variable: bien thuoc ve the hien/doi tuong cua lop
        self.roll = roll                           # Instance variable

def mani1():
    # stream = input("Enter stream: ")          
    name = input("Enter name: ")
    roll = input("Enter roll: ")

    a = CSStudent_1(name, roll)
    b = CSStudent_1(name, roll)

    print(a.stream)
    print(b.stream)

    print(a.name)
    print(b.name)
    
    print(a.roll)
    print(b.roll)

    print(CSStudent_1.stream)

if __name__=="__main__":
    mani1()

# Thay doi cac bien thanh vien trong python

# doi class variable bang cach su dung doi tuong
class CSStudent_2:

    stream = "cse"

    def __init__(self, name, roll):
        self.name = name
        self.roll = roll

def main2():
    name = input("Enter name: ")
    roll = input("Enter roll: ")

    cs_1 = CSStudent_2(name, roll)
    cs_2 = CSStudent_2(name, roll)
    print("Initially:")

    print(f"cs_1.stream = {cs_1.stream}")
    print(f"cs_2.stream = {cs_2.stream}\n")

    cs_1.stream = "ece"
    print("After changing cs_1.stream:")

    print(f"cs_1.stream = {cs_1.stream}")
    print(f"cs_2.stream = {cs_2.stream}")

if __name__=="__main__":
    main2()

# thay doi class variable bang class name: recommend
class CSStuden_3:
    stream = "cse"

    def __init__(self, name, roll):
        self.name = name 
        self.roll = roll

def main3():
    cs_3 = CSStuden_3("Bao", 23)
    cs_4 = CSStuden_3("Y", 19)

    print(cs_3.stream)
    print(cs_4.stream)

    # print(cs_3.roll)
    # print(cs_4.roll)

    CSStuden_3.stream = "ece"
    
    print(cs_3.stream)
    print(cs_4.stream)

if __name__=="__main__":
    main3()

