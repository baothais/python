for i in range(1,11):
    print(i)
    if i == 2:
       break
if True: 
    print("Hello world")
    q = 10

#biến toàn cục
a = "awesome"
def myfunc_1():
    a = "wonderful"
    print("Python is " +a)

myfunc_1()
print("Python is " +a)

#tạo biến toàn cục trong hàm
def myfunc():
    global x 
    x = "fantastic"

myfunc()
print("Python is " +x)

#xem kiểu dữ liệu của bất kì đối tượng nào bằng cách sử dụng hàm type()
c = 5
print(type(c))

#biến chỉ định
a = int(1)
b = float(2)
c = str(5)
d = str("A Bảo đẹp trai")
print(a)
print(b)
print(c)
print(d)

                                                    #STRING (CHUỖI)
#chuỗi là mảng
a = "Thái Bảo"
print(a[4])
print(a[5:8])
print(a[-3:])

#tính độ dài chuỗi sử dụng hàm len()
a = "Hello world!"
print(len(a))

#phương thức strip() loại bỏ khoảng trắng đầu hoặc cuối chuỗi
a = " Thái Bảo đẹp trai "
print(a.strip())

#trả về chữ thường dùng lower()
a = "HELLO WORLD"
print(a.lower())

#trả về chữ in hoa dùng upper()
a = "hello world"
print(a.upper())

#thay thế chuỗi/ký tự này thành chuỗi/ký tự khác dùng replace()
a = "Thái Bảo đẹp trai"
print(a.replace("Thái Bảo đẹp trai", "Như Ý đẹp gái"))
print(a.replace("B", "b"))

#phương thức chia chuỗi thành các chuỗi con nếu nó tìm thấy các dấu phân tách
a = "Hello , World"
print(a.split(","))

#kiểm tra cụm từ trong chuỗi
a = "Never give up"
x = "never" not in a
print(x)
y = "Never" in a
print(y)
z = "never give up" in a
print(z)

#ghép 2 or nhiều chuỗi sử dụng "+"
a = "Hello"
b = "World"
c = a + " " + b
print(c)

#kết hợp chuỗi và số bằng format()
age_1 = 24
age_2 = 19
txt_1 = "Hello World, My name's Bảo. I'm {} years old."
print(txt_1.format(age_1))
txt_2 = "Hello World, My name's Bảo. I'm {} years old and my girlfriend is {} years old."
print(txt_2.format(age_1, age_2))
#sử dụng index numbers để các đối số được đặt vào đúng chỗ
age_3 = 19          #index = 0
age_4 = 24          #index = 1
txt_3 = "Hello World, My name's Bảo. I'm {1} years old and my girlfriend is {0} years old."
print(txt_3.format(age_3, age_4))               #không cần viết đúng thứ tự

#ký tự \
age = 24
txt = "Hello World. My name's \"Bảo\". I'm \'{}\' years old"
print(txt.format(age))












