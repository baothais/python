class Mang2Chieu:
    values : int
    list_2_chieu = []
    def showMenu(self):
        print('==================CHUONG TRINH==================')
        print('1. Nhap mang 2 chieu')
        print('2. In mang 2 chieu vua nhap')
        print('3. Đếm số lần xuất hiện của x trong A và vị trí của chúng.')
        print('4. Tính tổng các phần tử lớn nhất của mỗi dòng.')
        print('0. Thoat chuong trinh')
        print('================================================')
    def nhapMang2Chieu(self):
        m = int(input('Nhap so hang: '))
        n = int(input('Nhap so cot: '))
        for i in range(m):
            l=[]
            for j in range(n):
                self.values = int(input('Nhap gia tri A[{}][{}]: '.format(i+1, j+1)))
                l.append(self.values)
            self.list_2_chieu.append(l)
    def inMang2Chieu(self):
        for i in range(len(self.list_2_chieu)):
            for j in range(len(self.list_2_chieu[i])):
                print('Gia tri A[{}][{}]: {}'.format(i+1, j+1, self.list_2_chieu[i][j]))
    def demXuatHien(self):
        x = int(input('Nhap gia tri can dem: '))
        dem=0
        for i in range(len(self.list_2_chieu)):
            for j in range(len(self.list_2_chieu[i])):
                if self.list_2_chieu[i][j]==x:
                    dem+=1
                    print('Gia x={} xuat hien o hang {} cot {}:'.format(x, i+1, j+1))
        print('Co {} lan xuat hien voi gia tri x={} trong mang A'.format(dem, x))
    def maxMang2Chieu(self):
        l=[]
        s=0
        for i in range(len(self.list_2_chieu)):
            m=max(self.list_2_chieu[i])
            s+=m
        print('Tong cac phan tu lon nhat cua moi dong la: {}'.format(s))     

if __name__=='__main__':
    m = Mang2Chieu()
    m.showMenu()
    chon = int(input('Moi ban chon cong viec: '))
    while chon!=0:
        if chon==1:
            print('1. Nhap mang 2 chieu')
            m.nhapMang2Chieu()
        elif chon==2:
            print('2. In mang 2 chieu vua nhap')
            m.inMang2Chieu()
        elif chon==3:
            print('3. Đếm số lần xuất hiện của x trong A và vị trí của chúng.')
            m.demXuatHien()
        elif chon==4:
            print('4. Tính tổng các phần tử lớn nhất của mỗi dòng.')
            m.maxMang2Chieu()
        else:
            print('Khong co lua chon nay! Moi ban chon lai cong viec')
        print('================================================')
        chon = int(input('Moi ban chon cong viec: '))
    print('==================Hen gap lai===================')
