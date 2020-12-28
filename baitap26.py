# """99 Bottles"""
# for i in range(99, 0, -1):
#     if i==1:
#         print("""1 bottle of beer on the wall, 1 bottle of beer.
# Go to the store and buy some more, 99 bottles of beer on the wall.""")
#     else:
#         print("""{} bottles of beer on the wall, {} bottles of beer.
# Take one down and pass it around, {} bottles of beer on the wall.""".format(i, i, i-1))
#         print()

# """Rock Paper Scissors"""
# import random
# def RockPaperScissors():
#     print('-------------------------------------------')
#     player = input('Moi ban chon (keo/bua/bao): ')
#     list_computer = ['keo', 'bua', 'bao']
#     computer = random.choice(list_computer)
#     while player!='keo' and player!='bua' and player!='bao':
#         player = input('Moi ban chon (keo/bua/bao): ')
#     else:
#         print('-------------------------------------------')
#         print('You select: {}'.format(player))
#         print('Computer select: {}'.format(computer))
#         print('-------------------------------------------')
#         if player==computer:
#             print('Draw')
#             print('-------------------------------------------')
#         else:
#             if player=='keo':
#                 if computer=='bua':
#                     print('Computer win')
#                     print('-------------------------------------------')
#                 else:
#                     print('You win')
#                     print('-------------------------------------------')
#             elif player=='bua':
#                 if computer=='keo':
#                     print('You win')
#                     print('-------------------------------------------')
#                 else:
#                     print('Computer win')
#                     print('-------------------------------------------')
#             elif player=='bao':
#                 if computer=='bua':
#                     print('You win')
#                     print('-------------------------------------------')
#                 else:
#                     print('Computer win')
#                     print('-------------------------------------------')

# if __name__=='__main__':
#     RockPaperScissors()
# max(map(int, map(lambda x: "".join(x), __import__("itertools").permutations(["1","3","04"]))))
# print(max(map(int, map(lambda x: ''.join(x), permutations(['1', '3', '04'])))))

from itertools import permutations

l = (list(permutations(['1', '3', '04'])))
s=[]
for i in range(len(l)):
    x = int(('').join(l[i]))
    s.append(x)
print(max(s))
