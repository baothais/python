from itertools import zip_longest
class A:
    value : int
    list_A=[]
    def showMenu(self):
        print('=====================MENU=====================') 
        print('1. Nhap mang 2 chieu')
        print('2. In mang 2 chieu')
        print('3. tìm ma trận chuyển vị của ma trận A.')
        print('0. Thoat chuong trinh')
        print('==============================================')
    def nhapMaTran(self):
        m = int(input('Nhap so hang: '))
        n = int(input('Nhap so cot: '))
        for i in range(m):
            l=[]
            for j in range(n):
                self.value = int(input('Nhap gia tri A[{}][{}]: '.format(i+1, j+1)))
                l.append(self.value)
            self.list_A.append(l)
    def inMaTran(self):
        for i in range(len(self.list_A)):
            for j in range(len(self.list_A[i])):
                print('Gia tri A[{}][{}] la: {}'.format(i+1, j+1, self.list_A[i][j]))
    def chuyenVi(self):
        list_B = list(zip_longest(*self.list_A))
        for i in range(len(list_B)):
            for j in range(len(list_B[i])):
                print('Gia tri B[{}][{}] la: {}'.format(i+1, j+1, list_B[i][j]))

if __name__=='__main__':
    a = A()
    a.showMenu()
    chon = int(input('Moi ban chon cong viec: '))
    while chon!=0:
        if chon==1:
            print('1. Nhap mang 2 chieu')  
            a.nhapMaTran()
        elif chon==2:
            print('2. In mang 2 chieu')
            a.inMaTran()
        elif chon==3:
            print('3. tìm ma trận chuyển vị của ma trận A.')
            a.chuyenVi()
        else:
            print('Khong co lua chon nay! Moi ban chon lai cong viec')
        print('==============================================')
        chon = int(input('Moi ban chon cong viec: '))
    print('=================Hen gap lai==================')
