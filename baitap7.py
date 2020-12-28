def binhphuong(n):
   return n*n
 
 # viet boi Quantrimang.com
number = (5, 10, 15, 20)
ketqua = map(binhphuong, number)
 
 # chuyen map object thanh list
print(list(ketqua))

def is_leap(year):
    leap = False
    
    # Write your logic here
    
    if year % 100 == 0:

        if year % 400 == 0:
            leap = True
        else:
            leap = False

    elif year % 4 == 0:
        leap = True

    else: 
        pass

    return leap

year = int(input("Enter year: "))
print(is_leap(year))
my_list = ["4", "5", "6", "7"]
new_map = map(int, my_list)
for i in new_map:
    print(i)
A = set()
a = input("a: ")
A.update(a)
a = input("a: ")
A.update(a.split(" "))
# b = input("b: ")
# b = input("b: ")
M = set(map(int, A))
# A = set(a.split(" "))
# B = set(b.split(" "))

print(M)
print(B)

M = set(map(int, A))
N = set(map(int, B))

D = N.difference(M)
for i in sorted(D):
    print(i)

A = set()
B = set()
a = input("a: ")
A.update(a.split(" "))
a = input("a: ")
A.update(a.split(" "))

b = input("b: ")
B.update(b.split(" "))
b = input("b: ")
B.update(b.split(" "))

C = A.symmetric_difference(B)
D = set(map(int, C))

for i in sorted(D):
    print(i)
if __name__ == '__main__':
    x = int(input("x: "))
    y = int(input("y: "))
    z = int(input("z: "))
    n = int(input("n: "))

    A = list()
    B = list()

    for i in range(0, x+1):
        for j in range(0, y+1):
            for k in range(0, z+1):
                A.append([i, j , k])
    
    # print(A)

    for items in A:
        s = 0
        for x in range(len(items)):
            s += items[x]
        if s != n :
            B.append(items)
        else:
            pass
    
    print(B)
        # print(s)
import array
if __name__ == '__main__':
    # n = int(input("n: "))
    arr = array.array(map(int, input("arr: ").split(" ")))
    new_arr = sorted(arr)
    for items in new_arr:
        if items == new_arr[-1]:
            new_arr.remove(items)
        else:
            pass
        # print(items)
    
    print(new_arr[-2])
    
    print(arr)

a = list([5, 6])
print(a[-2])
            
if __name__ == '__main__':
    # n = int(input("n: "))
    arr = list(map(int, input("arr: ").split(" ")))

    new_arr = sorted(arr)
    my_arr = list()
    for items in range(len(new_arr) - 1):
        if new_arr[items] != new_arr[len(new_arr) - 1]:
            my_arr.append(new_arr[items])
        else:
            pass
    
    print(my_arr[-1])

A = [['Harry', 37.21], ['Berry', 37.21], ['Tina', 37.2], ['Akriti', 41], ['Harsh', 39]]
# print(sorted(A))
# B = map(int, A[])
B = sorted(A)
mark = []
name = (input("name: ").split(" "))
score = (input("score: ").split(" "))
scores = list(map(float, score))

name = input("name: ")
A = list(name.split(" "))










