#Python set(không có thứ tự, không có chỉ định, không cho phép chứa dữ liệu trùng lặp và chứa trong dấu {})

#tạo 1 set
thisset = {"apple", "banana", "cherry", 24}
print(thisset)
#===================================================================

#truy cập items
thisset = {"apple", "banana", "cherry", 24, "Bảo"}
for i in thisset:
    print(i)
#===================================================================

#kiểm tra item có tồn tại trong set hay ko
thisset = {"apple", "banana", "cherry"}
if "apple" in thisset:
    print("Yes, it's in thisset")
else: print("No, it's not in thisset")
#===================================================================

#có thể thêm mới items nhưng không thể thay đổi

#thêm items
#dùng add() để thêm 1 item
thisset = {"apple", "banana", "cherry"}
thisset.add(24)         #add giá trị
print(thisset)

#dùng update() để thêm nhiều items
thisset = {"apple", "banana", "cherry"}
thisset.update(["orange", 24, "Bảo"])           
print(thisset)
#===================================================================

#chiều dài set
thisset = {"apple", "banana", "cherry"}
print(len(thisset))
#===================================================================

#remove items
#dùng remove() - Nếu item khôg tồn tại sẽ gây lỗi
thisset = {"apple", "banana", "cherry"}
thisset.remove("banana")        #remove giá trị
print(thisset)

#dùng discard() - Nếu item không tồn tại sẽ Không gây lỗi
thisset = {"apple", "banana", "cherry"}
thisset.discard("Bảo")          #remove giá trị
print(thisset)

#dùng pop() nhưng không biết item nào bị remove
thisset = {"apple", "banana", "cherry"}
x = thisset.pop()           #remove phần tử ngẫu nhiên
print(x)                    #item remove
print(thisset)              #set sau khi remove

#dùng clear() để xoá all item return none
thisset = {"apple", 24, 36}
print(thisset.clear())

#từ khoá del để xoá all item nhưng print sẽ lỗi
thisset = {"apple", 24, 36}
del thisset
#===================================================================

#kết hợp 2 or nhiều set
#dùng union()
thisset = {"apple", 24, 36}
myset = {1, 4, 2, 5}
print(myset.union(thisset))

#dùng update()
thisset = {"apple", 24, 36}
myset = {1, 4, 2, 5}
print(myset.update(thisset))
#===================================================================

#hàm set()
thisset = set((1, 2, 4, 5, 6))
print(thisset)
#===================================================================

#Python dictionary(không có thứ tự, có thể thay đổi, có chỉ định, không cho phép chứa dữ liệu trùng lặp và chứa trong dấu {} gồm key và value)
#tạo dict
thisdict = { 
            "name" : "Bảo",
            "age"  : 24,
            "relationship" : "had girlfriend"
}
print(thisdict)
#===================================================================

#truy cập dict
thisdict = {
    "car" : "BMW",
    "color" : "black",
    "cost" : 1000
}
print("Car's name is",thisdict["car"])
print("Cost's car is",thisdict["cost"])
#dùng get()
thisdict = {
    "car" : "BMW",
    "color" : "black",
    "cost" : 1000
}
print(thisdict.get("car"))
#===================================================================

#thay đổi dict
thisdict = {
    "car" : "BMW",
    "color" : "black",
    "cost" : 1000
}
thisdict["car"] = "Audi"
print(thisdict)
#===================================================================

#loop trong dict
#xuất all key
thisdict = {
    "car" : "BMW",
    "color" : "black",
    "cost" : 1000
}
for i in thisdict:
    print(i)
#xuất all value()
thisdict = {
    "car" : "BMW",
    "color" : "black",
    "cost" : 1000
}
for i in thisdict:
    print(thisdict[i])
#dùng values() để xuất value
thisdict = {
    "car" : "BMW",
    "color" : "black",
    "cost" : 1000
}
for i in thisdict.values():
    print(i)
#xuất both keys and values using by items()
thisdict = {
    "car" : "BMW",
    "color" : "black",
    "cost" : 1000
}
for i, j in thisdict.items():
    print(i,":",j)
#===================================================================

#check in dict
thisdict = {
    "car" : "BMW",
    "color" : "black",
    "cost" : 1000
}
if "car name" in thisdict:
    print("Yes")
else: print("No")
#===================================================================

#length dict
thisdict = {
    "car" : "BMW",
    "color" : "black",
    "cost" : 1000
}
print(len(thisdict))
#===================================================================

#add dict
thisdict = {
    "car" : "BMW",
    "color" : "black",
    "cost" : 1000
}
thisdict["year"] = 2025
print(thisdict)
#===================================================================

#remove item
#dùng pop() để remove item chỉ định bằng key
thisdict = {
    "car" : "BMW",
    "color" : "black",
    "cost" : 1000
}
x = thisdict.pop("car")
print(x)
print(thisdict)
#dùng popitem() để remove item cuối cùng
thisdict = {
    "car" : "BMW",
    "color" : "black",
    "cost" : 1000
}
x = thisdict.popitem()
print(x)
print(thisdict)
#dùng từ khoá del để remove item chỉ định = key
thisdict = {
    "car" : "BMW",
    "color" : "black",
    "cost" : 1000
}
del thisdict["car"]
print(thisdict)
#or dùng del để xoá all dict. Nếu print sẽ lỗi vì dict k còn tồn tại
thisdict = {
    "car" : "BMW",
    "color" : "black",
    "cost" : 1000
}
del thisdict
#dùng clear() để làm rỗng dict
thisdict = {
    "car" : "BMW",
    "color" : "black",
    "cost" : 1000
}
thisdict.clear()
print(thisdict)
#===================================================================

#copy dict
#dùng copy()
thisdict = {
    "car" : "BMW",
    "color" : "black",
    "cost" : 1000
}
mydict = thisdict.copy()
print(mydict)
#dùng dict()
thisdict = {
    "car" : "BMW",
    "color" : "black",
    "cost" : 1000
}
mydict = dict(thisdict)
print(mydict)
#===================================================================

#dict lồng nhau
#C1
myfamily = {
    "child1" : {
        "name" : "Susan",
        "age" : 10
    },
    "child2" : {
        "name" : "Billy",
        "age" : 15
    },
    "child3" : {
        "name" : "Mark",
        "age" : 14
    }
}
print(myfamily)
#C2
child1 = {
    "name" : "Susan",
    "age" : 10
}
child2 = {
    "name" : "Billy",
    "age" : 15
}
child3 = {
    "name" : "Mark",
    "age" : 14
}
myfamily = {
    "child1" : child1,
    "child2" : child2,
    "child3" : child3
} 
print(myfamily)
#===================================================================

#dict()
thisdict = dict(name = "Susan", age = 14, sex = "female")
print(thisdict)

thisdict = {
    1 : "hi",
    "2" : 2
}
for key in thisdict.keys():
    print(key)