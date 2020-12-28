# f1 = open('/Users/macbook/Desktop/python/demo4.txt','a')
# f1.write('001 : Thai Bao\n')
# f1.write('002 : Nguyen Van Tien\n')
# f1.write('003 : Duong Cong Hiep\n')
# f1.write('004 : Le Thi Thao')
# f1.close()
f1 = open('/Users/macbook/Desktop/python/demo4.txt')
list_dssv = f1.read().split('\n')
new_list_dssv=[]
for i in range(len(list_dssv)):
    l=[]
    for a in list_dssv[i].split(':'):
        l.append(a)
    new_list_dssv.append(l)

print(new_list_dssv)
# ten = input('Nhap ten can tim: ')
# for i in range(len(new_list_dssv)):
#     if new_list_dssv[i][1].split(' ')[-1].lower()==ten.lower():
#         print(new_list_dssv[i][1].strip())
f1.close()
# import os
# if os.path.exists("/Users/macbook/Desktop/python/demo3.txt"):
#     os.remove("/Users/macbook/Desktop/python/demo3.txt")
#     os.remove("/Users/macbook/Desktop/python/demo2.txt")
#     os.remove("/Users/macbook/Desktop/python/demo1.txt")
# else:
#     print("The file does not exist")

