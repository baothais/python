try:
    print(5/0)
    raise ZeroDivisionError("division by zero")
except ZeroDivisionError as zeroDivisionerror:
    print(f'{zeroDivisionerror}')

class attributeError(Exception):
    def __init__(self, mismatch):
        self.mismatch = mismatch
try:
    raise attributeError("attribute error!")
except attributeError as ae:
    print(f'{ae}')

email = input("Enter your email: ").split("@")
print(f'username: {email[0]}\ncompanyname: {email[1]}')

s = [int(x) for x in input().split(' ') if x.isnumeric()]
print(s)

def add(param1, param2):
    while (param1 > 1000 and param1 < -1000) and (param2 > 1000 or param2 < -1000):
        param1 = int(input("Enter param1 again: "))
        param2 = int(input("Enter param2 again: "))
    else:
        return param1 + param2

if __name__=="__main__":
    param1 = int(input("Enter param1: "))
    param2 = int(input("Enter param2: "))
    print(add(param1, param2))

mylist = list(filter(lambda x: x!=1, map(int, input().split(' '))))
print(mylist)

mylist = list(map(lambda x: x+x, [x for x in range(1, 100)]))
print(mylist)

n = int(input())
mylist = [x for x in range(1, 10) if x%2==0 else x+1]
print(mylist)

l = [x**2 if x%2==0 else x**3 for x in range(1, 6)]
print(l)

def split_and_join(line):
    return '-'.join(line)

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)

string = "abracadabra"
print(list(string))

def mutate_string(string, position, character):
    return string[:position] + character + string[position+1:] 

if __name__ == '__main__':
    s = input()
    i, c = input().split(' ')
    s_new = mutate_string(s, int(i), c)
    print(s_new)

a, b = input().split()
print(f'{a}, {b}')

string = 'ABCDCCDC'
substring = 'CDC'

if substring in string:
    print(string.count(substring))



