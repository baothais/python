# bai 22
if __name__=="__main__":
    mylist = []
    for i in range(int(input("Nhap so luong hoc sinh: "))):
        mytuple = tuple(input("Nhap input: ").split(" "))
        mylist.append(mytuple)

    print(sorted(mylist))

# Bai 23
def print_n(n):
    for j in range(n):
        if j%7 == 0:
            yield j

for i in print_n(n=100):
    print(i)

# Bai 24
string = 'New to Python or choosing between Python 2 and Python 3? Read Python 2 or Python 3'
str = string.split(" ")
 
count={}
for i in str:
    if i in count:
        count[i]+=1
    else:
        count[i]=1
    i = count[i]

print(count)

count[1] = "hello"
print(count)

# Bai 25
A = lambda x: x+y
print(A(10, 9))

# Bai 26
A = lambda x: str(x)
print(A(10))

Bai 27

list_int = list(map(int, input("Enter list_int: ").split(" ")))
newlist = list(set(list_int))

print(newlist)

A = list(map(int, input("Nhap toa do diem A: ").split(", ")))
B = list(map(int, input("Nhap toa do diem B: ").split(", ")))

# if A[0] == -(B[0]) and A[1] == -(B[1]):
#     print("2 diem A va B doi dien nhau")
# else:
#     print("2 diem A va B khong doi dien nhau")

while A[0] != -(B[0]) or A[1] != -(B[1]):
    A = list(map(int, input("Nhap toa do diem A: ").split(", ")))
    B = list(map(int, input("Nhap toa do diem B: ").split(", ")))
else:
    print("2 diem A va B doi dien nhau")

def print_pt_doc_nhat():
    mylist = list(map(int, input("Enter list: ").split(" ")))
    list1 = sorted(mylist)
    list2 = []
    
    for i in range(len(list1)-2):
        if list1[i] == list1[i+1]:
            list2.append(list1[i])
            list2.append(list1[i+1])

    return list(set(list1) - set(list2))

if __name__=="__main__":
    print(print_pt_doc_nhat())

A = [[1, 2, 3], [4, 5, 6], [3, 4, 1]]
B = []

for i in range(len(A)-2):
    if A[i][2] > A[i+1][2]:
        if A[i][2] > A[i+2][2] and A[i+2][2] < A[i+1][2]:
            B.append(A[i+2])
            B.append(A[i+1])
            B.append(A[i])
        
        else:
            B.append(A[i+1])
            B.append(A[i])
            B.append(A[i+2])
    else:
        if A[i+1][2] > A[i+2][2] and A[i+2][2] < A[i][2] :
            B.append(A[i+2])
            B.append(A[i])
            B.append(A[i+1])
        
        else:
            B.append(A[i])
            B.append(A[i+1])
            B.append(A[i+2])

print(B)
import time
A = [x for x in range(1000, 3001)]
start = time.time()
for i in range(len(A)):
    B = str(A[i])
    s = 0
    for j in range(len(B)):
        if int(B[j])%2 == 0:
            s += 1
            if s == 4:
                print(B + ", ")
end = time.time() - start
print(end)
x = 11
A = [x for x in range(1000, 3001) if x%2 == 0]
print(A)




    
            




        

























