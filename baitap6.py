def print_diem():
    n = int(input("Enter n: "))
    mydict = dict()

    for _ in range(n):
        name = input("Enter name: ")
        studen_mark = list(map(float, input("score: ").split(" ")))
        mydict[name] = studen_mark
    
    query_name = input("Enter query_name: ") 

    return '{:.2f}'.format(sum(mydict[query_name])/len(mydict[query_name]))

if __name__=="__main__":
    print(print_diem())

if __name__=="__main__":
    a = int(input("Enter a: "))
    b = int(input("Enter b: "))
    c = int(input("Enter c: "))
    d = int(input("Enter d: "))

    print(a**b + c**d)

for i in range(1, int(input("n: "))):
    print((10**(i)//9)*i)

if __name__=="__main__":
    a = lambda x: x + 11*x + 111*x +1111*x
    print(a(int(input("x: "))))
from re import search
if __name__=="__main__":
    A = list(input("Nhap password: ").split(","))

    for items in A:
        if len(items) >= 6 and len(items) <= 12:
            if search("[a-z]", items):
                if search("[0-9]", items):
                    if search("[A-Z]", items):
                        if search("[$#@]", items):
                            print(items)

if __name__=="__main__":
    N = int(input("Enter N: "))
    mylist = []
    for i in range(0, N):
        command = input("Enter command: ").strip()
        if command == 'print':
            print(mylist)
        elif command == 'sort':
            mylist.sort()
        elif command == 'pop':
            mylist.pop()
        elif command == 'reverse':
            mylist.reverse()
        else:
            if command == 'insert':
                number_list = list(map(int, input("Enter number_list: ").split(" ")))
                mylist.insert(number_list[0], number_list[1])
            else:
                number = int(input("Enter number: "))
                if command == 'append':
                    mylist.append(number)
                elif command == 'remove':
                    mylist.remove(number)

if __name__ == '__main__':
    n = int(input("b: "))
    integer_list = map(int, input("n: ").split(" "))
    t = tuple(integer_list)
    print(hash(t))

def print_asd(a):
    for i in a:
        if i % 2 == 0:
            continue
        else:       
            return False

    return True

if __name__=="__main__":
    a = list(map(int, input("n: ").split(" ")))
    if print_asd(a):
        print("x")
    else:
        print("y")
                    

