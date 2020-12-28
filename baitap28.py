# bai 1: chia het cho 7, khong chia het cho 5
def division7():
    l = [str(x) for x in range(10, 201) if (x%7==0 and x%5!=0)]
    return ((', '.join(l)))

#bai 2: giai thua so n
def giaiThua(n):
    while n<0:
        n = int(input('n: '))
    else:
        if n==0: 
            return 1
        else:
            return n*giaiThua(n-1)

# bai 3: tao dict chua i: i*i
def mapSonguyen(n):
    d = {i: i*i for i in range(1, n+1)}
    return d

# bai 4: giai ptb2
from math import sqrt
def ptBac2(a, b, c):
    if a==0:
        if b==0:
            if c==0:
                return 'Vo so nghiem'
            else:
                return 'Vo nghiem'
        else:
            return float(-c/b)
    else:
        delta = b**b-4*a*c
        if delta<0:
            return 'Vo nghiem'
        elif delta==0:
            return float(-b/(2*a))
        else:
            return '{:.2f}, {:.2f}'.format(float(sqrt(delta)/(2*a)), float(-sqrt(delta)/(2*a)))

# bai 5: doi co so 10 sang co so B bat ky (1<=B<=32)
def convertToCs2(n):
    cs2 = []
    while n!=0:
        a = int(n%2)
        n = int(n/2)
        cs2.insert(0, str(a))
    if len(cs2)==3:
        return ('0{}'.format(('').join(cs2)))
    elif (len(cs2))==2:
        return ('00{}'.format(('').join(cs2)))
    elif (len(cs2))==1:
        return ('000{}'.format(('').join(cs2)))
    return (('').join(cs2))

def convertToCs16(n):
    cs16 = []
    while n!=0:
        a = int(n%16)
        n = int(n/16)
        if a==10:
            cs16.append('A')
        elif a==11:
            cs16.append('B')
        elif a==12:
            cs16.append('C')
        elif a==13:
            cs16.append('D')
        elif a==14:
            cs16.append('E')
        elif a==15:
            cs16.append('F')
        else:
            cs16.insert(0, str(a))
    return ('').join(cs16)

if __name__=='__main__':
    print('result lession 1: {}'.format(division7()))
    print('result lession 2: {}'.format(giaiThua(n=5)))
    print('result lession 3: {}'.format(mapSonguyen(n=8)))
    print('result lession 4: {}'.format(ptBac2(a=1, b=3, c=4)))
    print('result lession 5: nhi phan: {}, thap luc phan: {}'.format(convertToCs2(n=90), convertToCs16(n=126)))
