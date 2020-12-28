                                                #Python if...else
                                                #Python for...loop   
#continue                                             
thislist = ["apple", "banana", "cherry", "orange", 4]
for i in thislist:
    if i == "orange":
        continue
    print(i)

#break
thislist = ["apple", "banana", "orange", 4]
for i in thislist:
    if i == "orange":
        break
    print(i)

#range()
for i in range(6): #range(6) là giá trị từ 0-5, không lấy 6
    print(i)

for i in range(10, 20): #giá trị từ 10-19, không lấy 20
    print(i)

for i in range(5, 45, 5): #giá trị từ 5-40, không lấy 45 với bước nhảy là 5
    print(i)

#else in for...loop
for i in range(6):
    print(i)
else: print("Done!")

#for...loop lồng nhau
thislist = ["apple", "banana", "cherry"]
mylist = ["red", "blue", "yellow"]
for i in thislist:
    for j in mylist:
        print(i, ":", j)

                                            #Python functions
#creat a function
#trong python, khai báo func ngta dùng từ khoá def
def my_func():
    print("Thái Bảo đep trai")
my_func()

#argument
def my_func1(name):
    print(name, "đẹp trai")

my_func1("Thái Bảo")
my_func1("A Bảo")
my_func1("Mr.Bảo")

#number of arguments
def my_func2(name, age):
    print(name, ":", age)

my_func2("Bảo", 24)

my_func2("Ý", 19)
def func(name, age, sex):
    print(name, age, sex)

func(name = "Bảo", sex = "male", age = 24)

#arbitrary arguments, *args
def my_function(a , b, *args):
    return a, b, args

print(my_function(1, 2, 3, 5, 7))

#keyword arguments
def my_function1(a, b, c):
    return a, b, c

print(my_function1(a = 1, c = 4, b = 3))

#Arbitrary Keyword Arguments, **kwargs
def myfunc2(**kwargs):
    for key, value in kwargs.items():
        print(key, value)

# thisdict = dict(car = "BMW", color = "black", year = "2025")
myfunc2(car = "BMW", color = "black", year = "2025")

thisdict = dict(car = "BMW", color = "black")
print(thisdict)

thisdict = {
    "car" : "BMW",
    "color" : "black"
}
print(thisdict)

#Passing a List as an Argument
def my_func3(a):
    print(a)

b = [1, 2, 3]
my_func3(b)

#return value
def my_func4(a):
    return a + 4

print(my_func4(4))

# The pass Statement
def my_func5():
    pass      #đặt pass để không bị lỗi khi hàm không có nội dung

#Recursion
def giaithua(k):
    if k >= 1:
        if k == 1:
            return 1
        else: 
            return k * giaithua(k-1)

x = 10
print(giaithua(x))





