import math
# Bai 13:
def bieuThuc(C, D, H):
    A = list(D.split(","))

    for i in range(0,len(A)):
        Q.append(int(math.sqrt((2 * C * int(A[i])/H))))
    
    print(f"Ket qua bieu thuc la: {Q}. QUA DINH IDOL OI")

D = input("Enter D: ")
C = 50
H = 30
Q = []

bieuThuc(C, D, H)

# Bai 14
def print_bang_chu_Cai(str1):
    A = list(str1.split(","))

    A.sort()
    return A
    

str1 = input("Enter string: ")

print(print_bang_chu_Cai(str1))

# Bai 15
def print_in_Hoa(s):
    return s.upper()

s = input("Enter string: ")
print(print_in_Hoa(s))

# Bai 16
def print_Chuoi(s):
    A = list(s.split(" "))
    
    for i in sorted(set(A)):            # set(A) là lấy những phần tử trùng lặp trong A thành 1 phần tử, còn phần tử không trùng lặp vẫn lấy bth.
        Q.append(i)                     # Sử dụng set để loại bỏ dữ liệu trùng lặp tự động.  

    return Q

s = input("Enter string: \n")
Q = []
print("\n")
print(" ".join(print_Chuoi(s)))         # str.join() chuoi.join tao thanh 1 chuoi

# Bai 17
def print_nhi_Phan(np):
    A = list(np.split(","))
    
    for i in range(len(A)):
        B = A[i]
        x = 0
        for j in range(len(B)):
            x += int(B[j]) * (2 ** (3 - j))

        if (x % 5 == 0):
            print(B)

np = input("Enter day nhi phan: ")

print_nhi_Phan(np)

# Bai 18
def print_so_Chan():
    for i in range(1000, 3001):
        if i % 2 == 0:
            A.append(str(i))

A = []
print_so_Chan()
print(" ".join(A))

# Bai 19
# C1
def print_number_letter(s):
    dem_int = 0
    dem_str = 0

    for i in s:
        if i.isdigit():
            dem_int += 1
        
        elif i.isalpha():
            dem_str += 1
        
        else:
            pass

    return dem_int, dem_str

s = input("Enter your string: ")

print("So chu so va so chu cai lan luot la: ")
print(print_number_letter(s))

# C2
dem_str = 0
dem_int = 0
s = input("Enter your string: ")

for i in s:
    if i.isdigit():
        dem_int += 1
    
    elif i.isalpha():
        dem_str += 1

    else:
        pass

print(f"So chu so la: {dem_str} and So chu cai la: {dem_int}")

# Bai 20
def print_dem_chu(s):
    dem_thuong = 0
    dem_hoa = 0

    for i in s:
        if i.islower():
            dem_thuong += 1
        
        elif i.isupper():
            dem_hoa += 1
        
        else:
            pass
    return dem_hoa, dem_thuong

if __name__=="__main__":
    s = input("Enter your string: ")

    print("So chu hoa va So chu thuong lan luot la: ")
    print(print_dem_chu(s))



































 





