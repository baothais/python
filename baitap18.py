"""Complete the solution so that it splits the string into pairs of two characters.
If the string contains an odd number of characters then it should replace the
missing second character of the final pair with an underscore ('_')."""
def solution(s):
    list_s=[]
    if len(s)%2!=0:
        s+='_'
    for i in range(0, len(s), 2):
        list_s.append(s[i:i+2])
    return list_s

if __name__=='__main__':
    s = input('Enter s: ')
    print(solution(s))

"""Move the first letter of each word to the end of it, then add "ay" to the end of
the word. Leave punctuation marks untouched."""
def pig_it(text):
    old_list_s = [x for x in text.split()]
    new_list_s=[]
    for i in range(len(old_list_s)):
        if not old_list_s[i].isalpha():
            new_list_s.append(old_list_s[i])
        else:
            new_list_s.append(old_list_s[i][1:]+old_list_s[i][0]+'ay')
    return (' ').join(new_list_s)

if __name__=='__main__':
    text = input('Enter text: ')
    print(pig_it(text))

"""Write a function that will find all the anagrams of a word from a list. You will
be given two inputs a word and an array with words. You should return an
array of all the anagrams or an empty array if there are none."""
def anagrams(word, words):
    # new_words=[]
    # for i in range(len(words)):
    #     if all(word.count(w)==words[i].count(w) for w in word) and len(word)==len(words[i]):
    #         new_words.append(words[i])
    # return [x for x in new_words if new_words.count(x)>=1]
    return [x for x in words if sorted(x)==sorted(word)]

if __name__=='__main__':
    word = input('Enter word:')
    words = input('Enter words: ').split()
    print(anagrams(word, words))

"""The parameter of the function findNb (find_nb, find-nb, findNb) will be
an integer m and you have to return the integer n such as n^3 + (n-1)^3 + ...
+ 1^3 = m if such a n exists or -1 if there is no such n."""
def find_nb(m):
    sum_m = 0
    n = 1
    while sum_m < m:
        sum_m+=n**3
        if sum_m==m:
            return n
        n+=1
    return -1

if __name__=='__main__':
    m = int(input('Enter m: '))
    print(find_nb(m))

"""Persistent Bugger."""
def persistence(n):
    dem=0
    while n>9:
        multiply=1
        for i in str(n):
            multiply*=int(i)
        n = multiply
        dem+=1
    return dem

if __name__=='__main__':
    print(persistence(39))

"""Your order, please"""
def order(sentence):
    if sentence!='':
        list_sentence = sentence.split()
        for i in list_sentence:
            for j in i:
                if j.isalpha():
                    return list_sentence.sort(key=int(j))
    return sentence

if __name__=='__main__':
    sentence = input('Enter sentence: ')
    print(order(sentence))

# https://www.codewars.com/kata/55c45be3b2079eccff00010f/train/python