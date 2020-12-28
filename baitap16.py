"""class phan so"""
class PhanSo:
    """khai bao bien tu so, mau so va danh sach chua tu so, mau so"""
    tuSo : int
    mauSo : int
    listPhanSo=[]
    
    """ham khoi tao"""
    def __init__(self):
        pass

    """ham nhap phan so"""
    def nhapPhanSo(self):
        for i in range(n):
            self.tuSo = int(input(f'Nhap tu so thu {i+1}: '))
            self.mauSo = int(input(f'Nhap mau so thu {i+1} # 0: '))
            while self.mauSo==0:
                self.mauSo = int(input(f'Nhap lai mau so thu {i+1} # 0: '))
            self.listPhanSo.append([self.tuSo, self.mauSo])
    
    """ham xuat phan so"""
    def xuatPhanSo(self):
        for i in range(n):
            print(f'Phan so thu {i+1} la: {self.listPhanSo[i][0]}/{self.listPhanSo[i][1]}')
    
    """ham cong phan so"""
    def congPhanSo(self):
        for i in range(n):
            tuso = self.listPhanSo[i][0]*self.listPhanSo[i+1][1]+self.listPhanSo[i+1][0]*self.listPhanSo[i][1]
            mauso = self.listPhanSo[i][1]*self.listPhanSo[i+1][1]
            return (f'{tuso}/{mauso}')

if __name__=='__main__':
    n = int(input('Moi ban nhap so 2 tu ban phim: '))
    ps = PhanSo()
    ps.nhapPhanSo()
    ps.xuatPhanSo()
    print('Tong 2 phan so la:')
    print(ps.congPhanSo())


    

