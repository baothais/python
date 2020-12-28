Try & Exception
Basic Syntax:
try:
    # code
    pass
except exceptionName:
    code
    exceptionName là tên của các exception bạn nghĩ có khả năng xảy ra
    pass

Note: + exceptionName là tên của các exception bạn nghĩ có khả năng xảy ra
      + Một lệnh try có thể có nhiều mệnh đề except để xử lí chúng khác nhau
      + Nếu khối lệnh trong try có lỗi xảy ra thì chương trình sẽ thực hiện except phía dưới. except nào thoả
      mãn thì nó sẽ thực thi code trong khối except đó

# Example_1
try:
    # code
    pass

except ValueError:
    # code
    pass

except RuntimeError:
    # code
    pass

try:
    n = int(input("Enter n > 0: "))
    if n <= 0:
        raise ValueError

except:
    print("Nhập sai rồi cha nội")

else:
    print(n)

Example_2
print("\n============================WELCOME TO NASA============================\n")
n = input("Enter your username: ")
p = input("Enter your password: ")

try:
    if (n != "bao.thais"):
        raise ValueError("Wrong username, bro. Enter again!")
    
    elif (p != "thaibao96"):
        raise KeyError("Wrong password, bro. Enter again!")

    print("\nÔng nhập đúng rồi đấy :D\n")
    
except ValueError as vl_1:
    print(vl_1)
    n = input("Enter your username: ")

    while (n != "bao.thais"):
        print("Wrong username, bro. Enter again!")
        n = input("Enter your username: ")
    else:
        p = input("Enter your password: ")
        while (p != "thaibao96"):
            print("Wrong password, bro. Enter again!")
            p = input("Enter your password: ")
        else: 
            print("\nÔng nhập đúng rồi đấy :D\n")
            print("===========================Chúc mừng ông đã truy cập thành công vào NASA===========================")      

except KeyError as vl_2:
    print(vl_2)
    p = input("Enter your password: ")

    while (p != "thaibao96"):
        print("Wrong password, bro. Enter again!")
        p = input("Enter your password: ")

    else:
        print("\nÔng nhập đúng rồi đấy", end="\n")
        print("\n========================Chúc mừng ông đã truy cập thành công vào NASA=======================")

else:
    print("\n============================Chúc mừng ông đã truy cập thành công vào NASA==========================")

