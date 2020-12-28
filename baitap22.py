from collections import OrderedDict
class List:
    a = []
    b = []
    def showMenu(self):
        print('===================MENU===================')
        print('1. Nhập hai dãy số a, b từ bàn phím')
        print('2. In hai dãy vừa nhập lên màn hình')
        print('3. Thêm tất cả các phần tử của mảng b vào mảng a tại vị trí k')
        print('4. Tìm các phần tử vừa có trong a vừa có trong b.')
        print('5. Tìm các phần tử có ở a mà không có ở b')
        print('0. Thoat chuong trinh')
        print('==========================================')
    def nhapList(self):
        self.a = list(map(int, input('Nhap day so vao list a: ').split()))
        self.b = list(map(int, input('Nhap day so vao list b: ').split()))
    def inList(self):
        print('Day so a la: {}'.format(self.a))
        print('Day so b la: {}'.format(self.b))
    def chenPhanTu(self):
        a = self.a.copy()
        b = self.b.copy()
        k = int(input('Nhap vi tri k ban muon chen: '))
        for i in range(len(b)-1, -1, -1):
            a.insert(k, b[i])
        print('Mang a sau khi chen cac phan tu cua mang b tai vi tri k={} la: {}'.format(k, a))
    def timPhanTu1(self):
        l = [str(self.a[i]) for i in range(len(self.a)) if self.a[i] in self.b]
        # list(OrderedDict.fromkeys(l)): xoa cac phan tu trung nhau trong list l ma khong thay doi thu tu.
        print('Cac phan tu vua co trong a va b la: {}'.format((', ').join(list(OrderedDict.fromkeys(l)))))
    def timPhanTu2(self):
        l = [str(self.a[i]) for i in range(len(self.a)) if not self.a[i] in self.b]
        print('Cac phan tu co trong a nhung khong co trong b la: {}'.format((', ').join(list(OrderedDict.fromkeys(l)))))

if __name__=='__main__':
    l = List()
    l.showMenu()
    chon = int(input('Moi ban chon cong viec: '))
    while chon!=0:
        if chon==1:
            print('1. Nhập hai dãy số a, b từ bàn phím')
            l.nhapList()
        elif chon==2:
            print('2. In hai dãy vừa nhập lên màn hình')
            l.inList()
        elif chon==3:
            print('3. Thêm tất cả các phần tử của mảng b vào mảng a tại vị trí k')
            l.chenPhanTu()
        elif chon==4:
            print('4. Tìm các phần tử vừa có trong a vừa có trong b.')
            l.timPhanTu1()
        elif chon==5:
            print('5. Tìm các phần tử có ở a mà không có ở b')
            l.timPhanTu2()
        else:
            print('Khong co cong viec phu hop! Moi ban chon lai cong viec')
        print('==========================================')
        chon = int(input('Moi ban chon cong viec: '))
    print('==================Hen gap lai==================')