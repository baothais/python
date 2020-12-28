
from datetime import datetime, time
class Vemaybay:
    tenchuyen : str
    ngaybay : str
    giobay : str
    giave : int
    def nhapVMB(self):
        print('=============Nhap thong tin chuyen bay=============')
        self.tenchuyen = input('Nhap ten chuyen bay: ')
        self.ngaybay = input('Nhap ngay bay (dd/mm/yy): ')
        self.giobay = input('Nhap gio bay: ')
        self.giave = int(input('Nhap gia ve: '))
        print()
    def inVMB(self):
        print('===============Thong tin chuyen bay===============')
        print('Ten chuyen bay: {}'.format(self.tenchuyen))
        print('Ngay bay: {}'.format(self.ngaybay))
        print('Gio bay: {}'.format(self.giobay))
        print('Gia ve: {}'.format(self.giave))
        print()
    def getgiave(self):
        return self.giave

class Nguoi:
    hoten : str
    ngaysinh : str
    gioitinh : str
    CMND : int
    def nhapHanhkhach(self):
        print('=============Nhap thong tin hanh khach=============')
        self.hoten = input('Nhap ho ten hanh khach: ')
        self.ngaysinh = input('Nhap ngay sinh hanh khach (dd/mm/yy): ')
        self.gioitinh = input('Nhap gioi tinh hanh khach: ')
        self.CMND = int(input('Nhap CMND hanh khach: '))
        print()
    def inHanhkhach(self):
        print('===============Thong tin hanh khach================')
        print('Ho ten hanh khach: {}'.format(self.hoten))
        print('Ngay sinh hanh khach: {}'.format(self.ngaysinh))
        print('Gioi tinh hanh khach: {}'.format(self.gioitinh))
        print('CMND hanh khach: {}'.format(self.CMND))
        print()

class Hanhkhach(Nguoi, Vemaybay):
    soluong : int
    def tongtien(self):
        print('=================Thong tin gia ve==================')
        self.soluong = int(input('Nhap so luong ve: '))
        return ('Gia tien hanh khach da mua {} ve la: {}'.format(self.soluong, self.getgiave()*self.soluong))

if __name__=='__main__':
    hk = Hanhkhach()
    hk.nhapVMB()
    hk.inVMB()
    hk.nhapHanhkhach()
    hk.inHanhkhach()
    print(hk.tongtien())
