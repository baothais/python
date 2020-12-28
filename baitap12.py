s = input()
width = int(input())
q = ''
for i in s:
    q += i
    if len(q) == 4:
        print(q+'\n')

def areFollowingPatterns(strings, patterns):
    if len(strings) != len(patterns) or strings == [] or patterns == []:
        return False
    else:
        for i in range(len(strings)):
            for j in range(i+1, len(strings)):
                if strings[i] == strings[j]:
                    if patterns[i] == patterns[j]:
                        return True
    return False

if __name__=="__main__":
    strings = input().split()
    patterns = input().split()
    print(areFollowingPatterns(strings, patterns))

def reverseInParenthese(inputString):
    return inputString[::-1]

if __name__=="__main__":
    inputString = input()
    print(reverseInParenthese(inputString))

for x in range(1, int(input())+1):
    print(x)

from collections import Counter

mylist = list(map(int, input().split()))
print(Counter(mylist))
from collections import Counter

number_shoes = int(input())
size_shoes = list(map(int, input().split()))
counter = Counter(size_shoes)
customer = int(input())
money = 0

for i in range(customer):
    size, price = map(int, input().split())
    if counter[size]:
        money += price
        counter[size] -= 1

print(money)

s = 0
for i in range(1, int(input())+1):
    s += float(i/(i+1))
print('{:.2f}'.format(s))

def print_n(n):
    if n==0:
        return 0
    else:
        return print_n(n-1)+100

if __name__=="__main__":
    n = int(input())
    print(print_n(n))

def print_Fibonacci(n):
    while n<0:
        n = int(input())
    else:
        if n==0:
            return 0
        elif n==1:
            return 1
        else:
            return print_Fibonacci(n-1) + print_Fibonacci(n-2)

if __name__=='__main__':
    n = int(input())
    print(str(print_Fibonacci(n)))
def f(n):
    if n == 0: return 0
    elif n == 1: return 1
    else: return f(n-1)+f(n-2)
 #Bài Python 67, Code by Quantrimang.com
n=int(input("Nhập số n: "))
values = [str(f(x)) for x in range(0, n+1)]
print (", ".join(values))


