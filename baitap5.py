# Bai 21
def print_Tong(a):
    A = list(a.split("+"))
    Q = []
    for i in range(len(A)):
        B = A[i]
        s = 0
        if i == 0:
            Q.append(A[0])

        else:
            for j in range(len(B)):
                s += int(B[j])
            Q.append(str(s))

    return Q
    
a = input("Enter a: ")

print("".join(print_Tong(a)))

# Bai 22
def print_so_le(s):
    A = list(s.split(","))
    Q = []
    
    for i in range(len(A)):
        # x = int(A[i])
        if int(A[i]) % 2 != 0:
            Q.append(A[i])
        
        else:
            pass

    return Q

if __name__=="__main__":
    s = input("Enter string: ")
    print(", ".join(print_so_le(s)))

# Bai 23
def print_Money(my_str):
    A = list(my_str.split(" "))
    D = 0
    W = 0
    tong = 0

    for i in range(len(A)):
        if str(A[i]) == "D":
            D += int(A[i+1])
        
        elif str(A[i]) == "W":
            W += int(A[i+1])
        
        else:
            pass
    tong = D - W
    print(f"sum: {tong}, D: {D}, W: {W}")

my_str = input("Enter your str: ")

print_Money(my_str)

