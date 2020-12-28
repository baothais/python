mylist = list(map(int, input().split(" ")))
newlist = [x for x in mylist if mylist.count(x)==1]
print(newlist)


from collections import Counter
mylist = list(map(int, input().split(" ")))
counter = Counter(mylist)

newlist = [ count in counter.items() if count == 1]
print(newlist)

list_in = list(map(int, input().split(" ")))
list_in.sort()
list_out = list(filter(lambda entry: not(entry in list_in[list_in.index(entry) + 1:]), list_in))
print(list_out)

mylist = list(input("Enter string: ").split(" "))
mydict = dict()
for i in mylist:
    mydict[i] = mylist.count(i)

print(mydict)


A = lambda x: x+(-x)
print(A(2))

A = lambda x: x
print(A(10))

def print_int_to_str(i):
    return str(i)

print(print_int_to_str(10))

def print_tong_str(x, y):
    return int(x) + int(y)
print(print_tong_str('10', '20'))

A = lambda x, y: int(x) + int(y)
print(A('20', '30'))

def noi_chuoi(x, y):
    return x+ " " +y
print(noi_chuoi("Hello", "Thai Bao"))

A = lambda x, y: x + " " + y
print(A("Hello", "Thai Bao"))

def print_chuoi(x, y):
    if len(x) > len(y):
        return x
    elif len(x) == len(y):
        return x+ '\n' +y
    else:
        return y

print(print_chuoi("Hello", "World!"))

A = lambda x, y: x if len(x) > len(y) else (y if len(x) <len(y) else x + '\n' + y)
print(A('Hello', 'World'))

print((lambda x: "Day la so chan" if x%2 == 0 else "Day la so le")(115))

mydict = {}
for i in range(1, 4):
    mydict[i] = i**2

print(mydict)

mydict = {i : i**2 for i in range(1,4)}
print(mydict)

mylist = list(map(int, input().split(" ")))
newdict = {x: mylist.count(x) for x in mylist if mylist.count(x) == 1}

print(newdict)

mylist = list(input().split(" "))
newdict = {x: mylist.count(x) for x in mylist}

print(newdict)

def print_Dict():
    mydict = {x: x**2 for x in range(1,21)}
    for i in mydict.values():
        print(i, end=' ')
if __name__=="__main__":
    print_Dict()
    print('\n')

def print_Dict_values():
    mydict = {x: x**2 for x in range(1, 21)}
    mylist = [str(value) for value in mydict.values()]
    return mylist

print((", ").join(print_Dict_values()))

def print_list():
    mylist = [x**2 for x in range(1, 21)]
    # newlist = [mylist[i] for i in range(len(mylist)) if i < 5]
    # newlist = [i for i in mylist if mylist.index(i) < 5]
    # return newlist
    return mylist[5:]

if __name__=="__main__":
    print(print_list())

mylist = [x**2 for x in range(1, 21)]
mytuple = tuple(mylist)
print(mytuple)

mytuple = (1, 2, 3, 4, 5 ,6, 7, 8, 9, 10)
mylist = [x for x in mytuple if x%2 == 0]
print(tuple(mylist))

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
    
    def info(self):
        return f'{self.title} by {self.author}'

if __name__=="__main__":
    print('\n.....')
    b1 = Book(title= 'The Alchemist', author= 'Paulo Coelho')
    print(b1.info())

    b2 = Book(title= 'Harry Potter 1', author= 'Harry Potter 1')
    print(b2.info())

    b3 = Book(title= 'Odyssey', author= 'Homer')
    print(b3.info())
    print('.....\n')

class Vietnam:
    def __init__(self, name, language):
        self.name = name
        self.language = language
    def printVN(self):
        return self.name, self.language

if __name__=="__main__":
    Vn = Vietnam('Hanoi', 'Tieng Viet')
    print(Vn.printVN())






