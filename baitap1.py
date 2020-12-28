import math
PI = math.pi
# Bài 1: Viết chương trình nhập tên, năm sinh để in ra tên tuổi. VD: sn 1996 => 24 tuổi
def Person(name, year_of_birthday):
    age = 2020 - int(year_of_birthday)
    print("Your name's", name)
    print("You're born in", year_of_birthday)
    print("You're", age, "year old.")

print("Bài 1:")
name = input("Enter your name: ")
year_of_birthday = input("Enter your year of birthday: ")

Person(name, year_of_birthday)   #gọi hàm Person

# Bài 2: Tính chu vi, diện tích hình tròn
def Hinhtron(r):
    C = 2 * PI * r
    S = r * r * PI
    print("Chu vi hình tròn là:",C)
    print("Diện tích hình tròn là:",S)

print("\nBài 2:")
r = int(input("Nhập bán kính: "))

Hinhtron(r)

# Bài 3: Tính diện tích, thể tích hình trụ
def Hinhtru(h, r):
    S = 2 * PI * r * (r + h)
    V = PI * r * r * h
    print("Diện tích hình trụ là:", S, "cm2")
    print("Thể tích hình trụ là:", V, "cm3")

print("\nBài 3:")
r = int(input("Nhập bán kính: "))
h = int(input("Nhập chiều cao: "))

Hinhtru(h, r)

# Bài 4: Tính giá trị biểu thức
def Bieuthuc(x):
    y1 = 4 * (x * x + 10 * x * math.sqrt(x) + 3 * x + 1 )
    y2 = (math.sin(PI * x * x) + math.sqrt(x * x + 1))/(math.exp(2 * x) + math.cos((PI / 4) * x))
    print("y1 =", y1, ", y2 =", y2)

print("\nBài 4:")
x = int(input("Nhập x: "))
Bieuthuc(x)

# Bài 5: Tính tổng các chữ số nguyên có 2 chữ số
def Sum(n):
    tong = 0
    while n < 10 or n > 99:
        n = int(input("Nhập sai, nhập lại: "))
    else:
        a = int(n%10)
        n = int(n/10)
        tong = a + n 
    return tong

print("\nBài 5:")
n = int(input("Nhập số nguyên có 2 chữ số: "))
print("Tổng là:", Sum(n))

# Bài 6: Tính số tờ tiền (50000, 20000, 10000, 5000, 2000, 1000) từ số tiền bạn đã nhập
# def tinh_so_to_tien(tien):

# 	loai_tien = [50000,20000,10000,5000,2000,1000]

# 	for i in loai_tien:
# 	    so_to = tien/i
# 	    print("co %d to %d nghin dong" %(so_to, i))
# 	    tien = tien%i

# n = input("Nhập số tiền: ")``
# tinh_so_to_tien(n)







