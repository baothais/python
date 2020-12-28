class Mang2Chieu:
    value : int
    list_value=[]
    def showMenu(self):
        print('=====================MENU=====================') 
        print('1. Nhap mang 2 chieu')
        print('2. In mang 2 chieu')
        print('3. Các phần tử trên mỗi dòng được sắp xếp theo thứ tự giảm dần.')
        print('4. Các dòng được sắp xếp lại theo thứ tự tăng dần của tổng các phần tử trên mỗi dòng')
        print('0. Thoat chuong trinh')
        print('==============================================')
    def nhapMang2Chieu(self):
        m=int(input('Nhap so hang: '))
        n=int(input('Nhap so cot: '))
        for i in range(m):
            l=[]
            for j in range(n):
                self.value = int(input('Nhap gia tri A[{}][{}]: '.format(i+1, j+1)))
                l.append(self.value)
            self.list_value.append(l)
    def inMang2Chieu(self):
        for i in range(len(self.list_value)):
            for j in range(len(self.list_value[i])):
                print('Gia tri A[{}][{}]: {}'.format(i+1, j+1, self.list_value[i][j]))
    def sxGiamDan(self):
        for i in range(len(self.list_value)):
            self.list_value[i].sort(reverse=True)
            print('Thu tu giam dan cac phan tu cua dong thu {} la: {}'.format(i+1, ('->').join(list(map(str, self.list_value[i])))))      
    def sxTangDan(self):
        l=[]
        for i in range(len(self.list_value)):
            s=sum(self.list_value[i])
            l.append(s)
        l.sort()
        for i in range(len(l)):
            print('Tong cac phan tu cua dong thu {} la: {}'.format(i+1, l[i]))

if __name__=='__main__':
    m = Mang2Chieu()
    m.showMenu()
    chon = int(input('Moi ban chon cong viec: '))
    while chon!=0:
        if chon==1:
            print('1. Nhap mang 2 chieu')
            m.nhapMang2Chieu()
        elif chon==2:
            print('2. In mang 2 chieu')
            m.inMang2Chieu()
        elif chon==3:
            print('3. Các phần tử trên mỗi dòng được sắp xếp theo thứ tự giảm dần.')
            m.sxGiamDan()
        elif chon==4:
            print('4. Các dòng được sắp xếp lại theo thứ tự tăng dần của tổng các phần tử trên mỗi dòng')
            m.sxTangDan()
        else:
            print('Khong co lua chon nay! Moi ban chon lai cong viec')
        print('==============================================')
        chon = int(input('Moi ban chon cong viec: '))
    print('=================Hen gap lai==================')
