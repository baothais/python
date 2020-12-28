                                                    #BOOLEAN
#giá trị
print(10 > 9)
print(10 == 9)
print(10 < 9)

#bool() function
x = "Hello World"
y = 10
print(bool(x))
print(bool(y))

                                                    #Operators (Toán tử)

                                                    #Python list(có thể thay đổi thứ tự, có thể trùng nhau và không phân biệt kiểu kiểu dữ liệu)
#khai báo list dùng dấu []

#tạo 1 list
thislist = ["apple", "banana", "orange"]
print(thislist)
#===================================================================

#truy cập phần tử list
thislist = ["apple", "banana", "orange"]
print(thislist[1])
print(thislist[0:2])
print(thislist[-2:])
#===================================================================

#thay đổi giá trị phần tử list
thislist = ["apple", "banana", "orange"]
thislist[2] = "cherry"
print(thislist)
#===================================================================

#in từng gía trị trong list dùng "for...in"
thislist = ["apple", "banana", "orange", 4]
for i in thislist:
    print(i)
#===================================================================

#kiểm tra phần tử có tồn tại trong list hay không dùng "in"
thislist = ["apple", "banana", "orange", 4]
if "cherry" in thislist:
    print("Yes, it's in thislist")
else: print("No, it's not in thislist")
#===================================================================

#độ dài list
thislist = ["apple", "banana", "orange"]
print(len(thislist))
#===================================================================

#thêm phần tử vào list 
# dùng append() để thêm vào cuối list
thislist = ["apple", "banana", "orange"]
thislist.append("cherry")
print(thislist)

#dùng insert() để thêm vào vị trí chỉ định
thislist = ["apple", "banana", "orange"]
thislist.insert(2, "cherry")
print(thislist)
#===================================================================
#xoá phần tử trong list
#xoá phần tử chỉ định dùng remove()
thislist = ["apple", "banana", "orange"]
thislist.remove("apple")
print(thislist)

#xoá phần tử có index chỉ định dùng pop(). Nếu không điền chỉ số, nó sẽ xoá phần tử cuối
thislist = ["apple", "banana", "orange"]
thislist.pop(1)
print(thislist)
thislist.pop()
print(thislist)

#dùng từ khoá del để xoá phần tử chỉ định or toàn bộ phần từ trong list
thislist = ["apple", "banana", "orange"]
del thislist[1]
print(thislist)
del thislist
#print(thislist) đã bị xoá toàn bộ nên không thể in được

#làm trống list dùng clear()
thislist = ["apple", "banana", "orange"]
thislist.clear()
print(thislist)
#===================================================================

#sao chép 1 list
#để sao chép dùng copy()
thislist = ["apple", "banana", "orange"]
mylist = thislist.copy()
print(mylist)

#cũng có thể dùng list()
thislist = ["apple", "banana", "orange"]
mylist = list(thislist)
print(mylist)
#===================================================================

#kết hớp 2 list với nhau
#dùng +
thislist = ["apple", "banana", "orange"]
mylist = ["0", "1", "2"]
sumlist = thislist + mylist
print(sumlist)

#dùng append()
thislist = ["apple", "banana", "orange"]
mylist = ["0", "1", "2"]
for i in thislist:
    mylist.append(i)

print(mylist)

#dùng extend()
thislist = ["apple", "banana", "orange"]
mylist = ["0", "1", "2"]
thislist.extend(mylist)
print(thislist)
#===================================================================

#tạo ds mới bằng list()
thislist = list(("apple", "banana", "orange"))
print(thislist)
# =============================================================================
                                    #Python Tuples(sắp xếp theo thứ tự và không thể thay đổi, cho phép trùng nhau và không phân biệt kiểu dữ liệu)
#khai báo tuple dùng dấu ()

#tạo 1 tuple()
#C1:
thistuple = ("apple", "orange", "banana")
print(thistuple)

#C2(dùng tuple()):
thistuple = tuple((1, 2, 3, 5, 6, "Bảo"))
print(thistuple)


#truy cập phần tử tuple
thistuple = ("apple", "orange", "banana")
print(thistuple[1])

#thay đổi giá trị phần tử tuple
x = ("apple", "orange", "banana")
y = list(x)
y.append("cherry")
x = tuple(y)
print(x)

#dùng vòng lặp để lặp qua phần tử tuple
thistuple = ("apple", "banana", "cherry")
for i in thistuple:
    print(i)

#kiểm tra phần tử có nằm trong tuple không
thistuple = ("apple", "banana", "cherry")
if "apple" in thistuple:
    print("Yes, it's in thistuple")
else: print("No, it's not in thistuple")

#độ dài tuple
thistuple = ("1", "2", "3")
print(len(thistuple))
x = (1, "2", 3, "4", 5, 5)
print(len(x))

#không thể xoá hoặc thêm items vào tuple

#cộng 2 tuple
x = ("1", "2", 3)
y = (1, 2, 3)
z = x + y
print(z)

