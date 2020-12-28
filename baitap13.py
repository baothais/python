from math import sqrt
import datetime
# cau a  
l1 = list(filter(lambda x: x%2==0, [x for x in range(int(input()))]))
print(l1)

# cau b  
for i in range(2, int(input())+1):
    if all(i%j!=0 for j in range(2, int(sqrt(i)+1))):
        print(i)

# cau 2
newlist = []
for i in range(1, int(input('Nhap so luong sinh vien: '))+1):
    hoten, ngaysinh, lop = input(f'Nhap ten sv thu {i}: '), list(map(int, input('Nhap ngay sinh: ').split('/'))), input('Nhap lop: ')
    print('\n')
    tuoi = datetime.date.today().year - ngaysinh[2]
    newlist.append([hoten, ngaysinh, lop, tuoi])
 
for i in range(len(newlist)):
    print(f'Ten sv thu {i+1}: {newlist[i][0]}, ngay sinh sv: {newlist[i][1]}')

# cau 3
# ten = hoten.split(' ')[:-1]
# newlist.sort(key= lambda x: x[0].split(' ')[-1])
# for i in range(len(newlist)):
#     print(newlist[i])

for i in range(len(newlist)):
    print(sorted(newlist,key= lambda x: x[0].split(' ')[-1], reverse=False))
    



    

  






