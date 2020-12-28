"""like facebook"""
def likes(names):
    #your code here
    if names==[]:
        return('no one likes this')
    elif len(names)==1:
        return(f'{names[0]} likes this')
    elif len(names)==2:
        return(f'{names[0]} and {names[1]} like this')
    elif len(names)==3:
        return(f'{names[0]}, {names[1]} and {names[2]} like this')
    else:
        return(f'{names[0]}, {names[1]} and {len(names)-2} orthers like this')

if __name__=='__main__':
    names = input().split()
    print(likes(names))

"""Given n, take the sum of the digits of n. If that value has more than one digit, 
continue reducing in this way until a single-digit number is produced. 
The input will be a non-negative integer."""
def digital_root(n):
    sum_n=0
    string_n = str(n)
    for i in string_n:
        sum_n+=int(i)
    if len(str(sum_n))>1:
        return digital_root(sum_n)
    return sum_n

if __name__=='__main__':
    n = int(input('Nhap n: '))
    print(digital_root(n))

"""Your task is to make a function that can take any non-negative integer 
as an argument and return it with its digits in descending order. 
Essentially, rearrange the digits to create the highest possible number."""
def descending_order(num):
    string_num = str(num)
    list_num = [i for i in string_num]
    list_num.sort(reverse=True)
    return int(('').join(list_num))

if __name__=='__main__':
    num = int(input())
    print(descending_order(num))

"""In this little assignment you are given a string of space separated numbers, 
and have to return the highest and lowest number."""
def high_and_low(numbers):
    list_numbers = list(map(int, numbers))
    list_numbers.sort()
    return f'{list_numbers[-1]} {list_numbers[0]}'

if __name__=='__main__':
    numbers = input('Enter your numbers: ').split()
    print(high_and_low(numbers))

"""Complete the method/function so that it converts dash/underscore delimited 
words into camel casing. The first word within the output should be capitalized only 
if the original word was capitalized (known as Upper Camel Case, also often referred 
to as Pascal case)."""
def to_camel_case(text):
    for i in text:
        if i=='_':
            old_list_text = [i for i in text.split('_')]
            new_list_text = [old_list_text[j].title() for j in range(1, len(old_list_text))]
            new_list_text.insert(0, old_list_text[0])
            return ('').join(new_list_text)
        elif i=='-':       
            old_list_text = [i for i in text.split('-')]
            new_list_text = [old_list_text[j].title() for j in range(len(old_list_text))]
            return ('').join(new_list_text)

if __name__=='__main__':
    text = input('Enter text: ')
    print(to_camel_case(text))

"""Create a function named divisors/Divisors that takes an integer n > 1
and returns an array with all of the integer's divisors(except for 1 and the
number itself), from smallest to largest. If the number is prime return the
string '(integer) is prime' (null in C#) (use Either String a in Haskell and"""
def divisors(integer):
    mylist = [i for i in range(2, integer) if integer%i==0]
    if mylist==[]:
        return '{} is prime'.format(integer)
    return mylist

print(divisors(integer=13))

"""In mathematics, a square number or perfect square is an integer that is the square of an integer; 
in other words, it is the product of some integer with itself."""
from math import sqrt
def is_square(n):
    print(n)
    if n==0:
        return True
    elif n<0:
        return False
    return n%sqrt(n)==0

if __name__=='__main__':
    n = int(input('Enter n: '))
    print(is_square(n))


              

