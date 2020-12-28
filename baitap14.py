from math import sqrt
def printTong(n):
    a : int
    s=0
    while n!=0:
        a = int(n%10)
        s += a
        n = int(n/10)
    return s

if __name__=='__main__':
    n = int(input('enter n: '))
    print(f'Tong cua cac so trong {n} la: {printTong(n)}')
for i in range(2, int(sqrt(50))):
    print(i)
def checkSoNguyenTo(a):
    return all(a%i != 0 for i in range(2, int(sqrt(a))+1))

def printSoNguyenTo(n):
    for i in range(2, n+1):
        if checkSoNguyenTo(i):
            print(i)

if __name__=="__main__":
    n = int(input('enter n: '))
    printSoNguyenTo(n)

def checkSoNguyenTo(n):
    dem=0
    for i in range(1, int(sqrt(n))+1):
        if n%i==0:
            dem += 1
    if dem==1:
        return True
    return False

def printSoNguyenTo(n):
    for i in range(2, n+1):
        dem=0
        for j in range(1, int(sqrt(i))+1):
            if i%j == 0:
                dem+=1
        if dem==1:
            print(i)

if __name__=="__main__":
    n = int(input("Enter n: "))
    if checkSoNguyenTo(n):
        print(f'{n} la so nguyen to')
    else:
        print(f'{n} khong phai la so nguyen to')
    printSoNguyenTo(n)

def printTichSoNguyenTo(n):
    mylist=[]
    for i in range(2, n):
        if all(i%j != 0 for j in range(2, int(sqrt(i))+1)):
            while n%i==0:
                mylist.append(str(i))
                n = int(n/i)
    print(('*').join(mylist))

if __name__=="__main__":
    n = int(input('enter n: '))
    print(f'Tich cac so nguyen to cua {n} la: ',end='')
    printTichSoNguyenTo(n)

    

    
