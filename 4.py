""" 1.Viết chương trình tìm tất cả các số chia hết cho 7 nhưng không phải bội số của 5, 
nằm trong đoạn 2000 và 3200 (tính cả 2000 và 3200). 
Các số thu được sẽ được in thành chuỗi trên một dòng, cách nhau bằng dấu phẩy."""
#sử dụng join() để nối chuỗi thành 1 chuỗi
j = list()
for i in range(2000, 3200):
    if (i % 7 == 0 and i % 5 != 0):
        j.append(str(i))

print(", ".join(j))
#---------------------------------------------------------------------------------

""" 2.Viết một chương trình có thể tính giai thừa của một số cho trước. 
Kết quả được in thành chuỗi trên một dòng, phân tách bởi dấu phẩy. 
Ví dụ, số cho trước là 8 thì kết quả đầu ra phải là 40320."""
#
x = int(8)
gt = int(1)
for i in range(1,x+1):
    gt *= i

print("x! =",gt)
#---------------------------------------------------------------------------------

""" 3.Với số nguyên n nhất định, hãy viết chương trình để tạo ra một dictionary chứa (i, i*i) 
như là số nguyên từ 1 đến n (bao gồm cả 1 và n) sau đó in ra dictionary này. 
Ví dụ: Giả sử số n là 8 thì đầu ra sẽ là: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64}."""
#
n = 8
thisdict = dict()
for i in range(1, n+1):
    thisdict[i] = i*i
print(thisdict)
#---------------------------------------------------------------------------------

""" 4.Viết chương trình chấp nhận một chuỗi số, phân tách bằng dấu phẩy từ giao diện điều khiển, 
tạo ra một danh sách và một tuple chứa mọi số.
Ví dụ: Đầu vào được cung cấp là 34,67,55,33,12,98 thì đầu ra là:
['34', '67', '55', '33', '12', '98']
('34', '67', '55', '33', '12', '98')"""
#
values = input("Enter your numbers: ")
thislist = list(values.split(" "))
thistuple = tuple(thislist)
print(thislist)
print(thistuple)
#---------------------------------------------------------------------------------

""" 5.Viết chương trình tính tổng của các chữ số của môt số nguyên n trong Python. 
Số nguyên dương n được nhập từ bàn phím."""
#
n = int(input("Enter number: "))
tong = int(0)
while n > 0:
    a = n%10
    n = int(n/10)
    tong += a
print("Tổng là :",tong)






