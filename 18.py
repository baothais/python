# f = open('/Users/macbook/Desktop/python/demo9.txt','x')
# f.write('Name: Bao  ID: 1  Marks: 10.0\n')
# f.write('Name: Y  ID: 2  Marks: 9.0')
# f.close()
f = open('/Users/macbook/Desktop/python/demo9.txt')
list_ds = f.read().split('\n')
new_list_ds=[]

for i in range(len(list_ds)):
    l=[]
    for j in list_ds[i].split('  '):
        l.append(j)
    new_list_ds.append(l)

search_id = input('Nhap id can tim: ')
for i in range(len(new_list_ds)):
    if new_list_ds[i][1].split(':')[-1].strip()==search_id:
        print(new_list_ds[i][1].split(':')[-1].strip())

search_name = input('Nhap name can tim: ')
for i in range(len(new_list_ds)):
    if new_list_ds[i][0].split(':')[-1].strip()==search_name:
        print(('\n').join(new_list_ds[i]))
