import math
# Bài 8
def Divided():
    for i in range(2000, 3201):
        if (i % 7 == 0 and i % 5 != 0):
            print(f"{i}", end= " ")
        
def main1():
    print("Bài 1: Các số chia hết cho 7 nhưng không phải bội của 5 nằm trong đoạn 2000 và 3200:\n")
    Divided()
    # print("\n-------------------------------------------------------------------------------------------")

if __name__=="__main__":
    main1()

# Bài 9
def GiaiThua(n):
    if n == 1:
        return 1
        
    return GiaiThua(n-1) * n

def main2():
    n = int(input("Enter n: "))
    while n <= 0:
        n = int(input("Wrong! Enter n again, please!: "))
    else:
        print(f"Giai thừa của {n} là {GiaiThua(n)}")

if __name__=="__main__":
    main2()

# Bài 10
dic = dict()
def printDict(n):
    for i in range(n+1):
        dic[i] = i*i 

    return dic

def main3():
    n = int(input("Enter n: "))

    print(printDict(n))

if __name__=="__main__":
    main3()

def print_List_Tuple(str):
    lis = list(str.split(", "))
    tup = tuple(lis)

    return f"lis = {lis} & tup = {tup}"

def main4():
    str = input("Enter str: ")

    print(print_List_Tuple(str))

if __name__=="__main__":
    main4()

# Bai 11
class in_Chu_Hoa:

    def setString(self, str1):
        self.str1 = str1
    
    def printString(self):
        return self.str1.upper()

def main5():
    str1 = input("Enter str: ")

    ich = in_Chu_Hoa()
    ich.setString(str1)
    print(ich.printString())

if __name__=="__main__":
    main5()

# Bai 12
class binhPhuong:

    def __init__(self, n):
        self.n = n
    
    def tinhBinhPhuong(self):
        return pow(self.n, 2)
    
def main6():
    n = int(input("Enter n: "))

    bp = binhPhuong(n)
    print("Binh phuong cua %d la: " %n, end= "")
    print(bp.tinhBinhPhuong())

if __name__=="__main__":
    main6()

    


    

        
