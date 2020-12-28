class SV:
    masv : int
    hoten : str
    dtb : float
    dssv=[]

    # ham kiem tra trung masv 
    def checkSVTrungId(self):
        for i in range(n+1):
            if self.dssv[i][0]==self.dssv[i+1][0]:
                return True
        return False
    # ham nhap sinh vien 
    def nhapSV(self):    
        for i in range(n):
            self.masv = int(input(f'Nhap ma so sv thu {i+1}: '))
            if self.checkSVTrungId():
                self.masv = int(input(f'Nhap ma so sv thu {i+1}: '))
            self.hoten = input(f'Nhap ho ten sv thu {i+1}: ')
            self.dtb = float(input(f'Nhap diem trung binh cua sv thu {i+1}: '))
            print('\n')
            self.dssv.append([self.masv, self.hoten, self.dtb])
            # self.checkSVTrungId()
        print(f'\nDanh sach sinh vien vua nhap:\n')
        self.printSV()
        
    # ham in sinh vien     
    def printSV(self):
        for i in range(len(self.dssv)):
            print(f'Sinh vien thu {i+1}:')
            print(f'    ma so sv thu {i+1}: {self.dssv[i][0]}')
            print(f'    ho ten sv thu {i+1}: {self.dssv[i][1]}')
            print(f'    diem trung binh sv thu {i+1}: {self.dssv[i][2]}\n')

    # ham cap nhat sinh vien 
    def capnhapThongTinSV(self):
        masv = int(input("Nhap ma sinh vien can cap nhat thong tin: "))
        dem=0
        print(f'Danh sach sinh vien sau khi cap nhat:\n')
        for i in range(len(self.dssv)):
            if self.dssv[i][0] == masv:
                dem=1
                self.dssv.remove(self.dssv[i])
                self.masv = int(input(f'Nhap lai ma so sv thu {i+1}: '))
                self.hoten = input(f'Nhap lai ho ten sv thu {i+1}: ')
                self.dtb = float(input(f'Nhap lai diem trung binh cua sv thu {i+1}: '))
                print('\n')
                self.dssv.insert(i, [self.masv, self.hoten, self.dtb])
                self.printSV()
                break
        if dem==0:
            print(f'Khong ton tai sinh vien co masv = {masv}')
    
    # ham xoa sinh vien theo masv 
    def xoaSV(self):
        masv = int(input('Nhap ma so sinh vien can xoa: '))
        dem=0
        print('Danh sach sinh vien sau khi xoa:\n')
        for i in range(len(self.dssv)):
            if self.dssv[i][0] == masv:
                dem=1
                self.dssv.remove(self.dssv[i])
                self.printSV()
                break
        if dem==0:
            print(f'Khong ton tai sinh vien co masv = {masv}')
    
    # ham tim kiem sinh vien theo ten 
    def searchSV(self):
        name = input('Nhap ten sinh vien can tim kiem: ')
        print('\n')
        dem=0
        print('Danh sach sinh vien sau khi tim kiem:\n')
        for i in range(len(self.dssv)):
            if self.dssv[i][1].split(' ')[-1] == name:
                dem=1
                print(f'Sinh vien thu {i+1}:')
                print(f'    ma so sv thu {i+1}: {self.dssv[i][0]}')
                print(f'    ho ten sv thu {i+1}: {self.dssv[i][1]}')
                print(f'    diem trung binh sv thu {i+1}: {self.dssv[i][2]}\n')
        if dem==0:
            print(f'Khong ton tai sinh vien co ten = {name}')

    # ham sap xep sinh vien theo diem trung binh
    def sapxepSVTheoDTB(self):
        self.dssv.sort(key=lambda item: item[2])
        print('Danh sach sinh vien sau khi sap xep: \n')
        self.printSV()
    
    # ham sap xep sinh vien theo ten 
    def sapxepSVTheoTen(self):
        self.dssv.sort(key=lambda item: item[1].split(' ')[-1])
        print('Danh sach sinh vien sau khi sap xep: \n')
        self.printSV()

if __name__=='__main__':
    n = int(input("Nhap so luong sinh vien: "))
    print('\n')
    sv = SV()
    sv.nhapSV()
    sv.capnhapThongTinSV()
    sv.xoaSV()
    sv.searchSV()
    sv.sapxepSV()
    sv.sapxepSVTheoTen()











