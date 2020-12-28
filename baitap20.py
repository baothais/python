class PhanSo:
    tuso = mauso = 0
    list_phanso = []
    def showMenu(self):
        print('================MENU================')
        print('1. Nhap 2 phan so')
        print('2. In 2 phan so vua nhap')
        print('3. Thuc hien phep toan voi 2 phan so')
        print('0. De thoat chuong trinh')
        print('====================================')
    def nhapPhanSo(self):
        for i in range(2):
            self.tuso = int(input('Nhap tu so thu {}: '.format(i+1)))
            self.mauso = int(input('Nhap mau so thu {}: '.format(i+1)))
            while self.mauso==0:
                self.mauso = int(input('Nhap lai mau so thu {}: '.format(i+1)))
            self.list_phanso.append([self.tuso, self.mauso])
    def inPhanSo(self):
        for i in range(len(self.list_phanso)):
            print('Phan so thu {}: {}/{}'.format(i+1, self.list_phanso[i][0], self.list_phanso[i][1]))
    def USCLN(self, a, b):
        while a*b != 0:
            if a > b:
                a %= b
            else:
                b %= a
        return a + b
    def congPhanSo(self):
        for i in range(len(self.list_phanso)):
            tuso = self.list_phanso[i][0]*self.list_phanso[i+1][1] + self.list_phanso[i+1][0]*self.list_phanso[i][1]
            mauso = self.list_phanso[i][1]*self.list_phanso[i+1][1]
            print('Tong cua 2 phan so la: {}/{}'.format(int(tuso/self.USCLN(tuso, mauso)),int(mauso/self.USCLN(tuso, mauso))))
            break
    def truPhanSo(self):
        for i in range(len(self.list_phanso)):
            tuso = self.list_phanso[i][0]*self.list_phanso[i+1][1] - self.list_phanso[i+1][0]*self.list_phanso[i][1]
            mauso = self.list_phanso[i][1]*self.list_phanso[i+1][1]
            print('Hieu cua 2 phan so la: {}/{}'.format(int(tuso/self.USCLN(tuso, mauso)),int(mauso/self.USCLN(tuso, mauso))))
            break
    def nhanPhanSo(self):
        for i in range(len(self.list_phanso)):
            tuso = self.list_phanso[i][0]*self.list_phanso[i+1][0]
            mauso = self.list_phanso[i][1]*self.list_phanso[i+1][0]
            print('Tich cua 2 phan so la: {}/{}'.format(int(tuso/self.USCLN(tuso, mauso)),int(mauso/self.USCLN(tuso, mauso))))
            break
    def chiaPhanSo(self):
        for i in range(len(self.list_phanso)):
            tuso = self.list_phanso[i][0]*self.list_phanso[i+1][1]
            mauso = self.list_phanso[i][1]*self.list_phanso[i+1][0]
            print('Thuong cua 2 phan so la: {}/{}'.format(int(tuso/self.USCLN(tuso, mauso)),int(mauso/self.USCLN(tuso, mauso))))
            break
if __name__=='__main__':
    ps = PhanSo()
    ps.showMenu()
    chon = int(input('Moi ban chon cong viec: '))
    while chon!=0:
        if chon==1:
            print('Moi ban nhap phan so')
            ps.nhapPhanSo()
        elif chon==2:
            print('Phan so ban vua nhap')
            ps.inPhanSo()
        elif chon==3:
            pheptinh = input('Moi ban chon phep tinh (+, -, *, /): ')
            if pheptinh=='+':
                ps.congPhanSo()
            elif pheptinh=='-':
                ps.truPhanSo()
            elif pheptinh=='*':
                ps.nhanPhanSo()
            elif pheptinh=='/':
                ps.chiaPhanSo()
            else:
                print('Khong co phep tinh nay!')
        else:
            print('Khong co lua chon nay! Moi ban chon lai cong viec')
        chon = int(input('Moi ban chon cong viec: '))
    print('===================Hen gap lai!===================')
