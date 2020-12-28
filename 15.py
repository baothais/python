A = list(map(int, input("n: ").split(" ")))

for i in range(len(A)-1):
    if A[i]==A[i+1]:
        A = list(map(int, input("Nhap lai list: ").split(" ")))
    else:
        print(A)

import math

def GIaIthua(n):
    n = float(input('Nhap n: '))
    if n==1 or n==0:
        return 1
    else:
        return n*GIaIthua(n-1)

if __name__=='__main__':
    n = float(input('Nhap n: '))
    print(GIaIthua(n))





