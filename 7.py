#Python Lambda (có thể nhận bất kì đối số nào nhưng chỉ có 1 biểu thức)
#syntax:
#lambda arguments : expression

x = lambda i : i + 1
print(x(5))

x = lambda i, j : i * j
print(x(3, 4))

x = lambda i, j, k : i + j + k
print(x(1, 2, 20))

# Python Array 
# create a array
arr = [1, 2, 4]
arr.pop()
print(arr)

#access arr
arr = [1, 2, 5, 3, 5]
print(arr[4])

#length array
arr = [1, 2, 4, 3, 5]
print(len(arr))

# looping array element
arr = [1, 4, 5, 2, 6]
for i in arr:
    print(i)

# add array element
arr = [1, 2, 5, 3, 7]
arr.append("Bảo")
print(arr)

#remove array
arr = [1, "Bảo", 3, 5, 6]
arr.pop()               #remove vị trí
print(arr)
arr.remove("Bảo")           #remove giá trị
print(arr)
