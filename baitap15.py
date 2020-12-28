""" ham tim so doi xung """
def checkSoDX(n):
    x = y = 0
    z = n
    while z!=0:
        x=int(z%10)
        y=y*10 + x
        z = int(z/10)
    return y==n

def printSoDX():
    for i in range(100000, 1000000):
        if checkSoDX(i):
            print(i)

if __name__=='__main__':
    printSoDX()
    print(len(printSoDX()))

""" ham doi thap phan sang nhi phan """
def chuyenDoiNP(n):
    listNP=[]
    # s=''
    while n!=0:
        x = int(n%2)
        n = int(n/2)
        listNP.insert(0, str(x))
        # s += str(x)
    return listNP
    # return s[::-1]

if __name__=='__main__':
    n = int(input('Nhap n: '))
    print(('').join(chuyenDoiNP(n)))
    # print(chuyenDoiNP(n))

""" ham xoa khoang trang """
def xoaSpace(s):
    a=''
    for i in s:
        if not i.isspace():
            a += i
    return a

if __name__=='__main__':
    s = input('Nhap chuoi: ')
    print(xoaSpace(s))

l = [x for x in input('Nhap chuoi: ') if not x.isspace()]
print(('').join(l))

""" ham kiem tra so chan or le """
def checkChanLe(n):
    return n%2==0

if __name__=='__main__':
    n = int(input('Nhap n: '))
    if checkChanLe(n):
        print('n la so chan')
    else: 
        print('n la so le')

