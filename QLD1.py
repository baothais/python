class SV:
    masv : int
    hoten : str
    ngaysinh : str
    dtb : float
    ghichu : str
    DSSV = []
    def showMenu(self):
        print('=====================Chuong Trinh=====================')
        print('1. Nhap danh sach SV.')
        print('2. In danh sach SV.')
        print('3. Dem SV co dtb < 4.0.')
        print('4. Tim SV theo masv.')
        print('======================================================')
    
    def nhapDSSV(self):
        for i in range(int(input('Ban muon nhap bao nhieu SV: '))):
            self.masv = int(input('Nhap masv thu {}: '.format(i+1)))
            if len(self.DSSV)!=0:
                for j in range(len(self.DSSV)):
                    while self.masv==self.DSSV[j][0]:
                        self.masv = int(input('Masv bi trung! Moi ban nhap lai masv thu {}: '.format(i+1)))
            self.hoten = input('Nhap ho ten SV thu {}: '.format(i+1))
            self.ngaysinh = input('Nhap ngay sinh SV thu {} (dd/mm/yy): '.format(i+1))
            self.dtb = float(input('Nhap dtb SV thu {} (0 <= dtb <= 10.0): '.format(i+1)))
            if self.dtb < 4.0:
                self.ghichu = 'KHONG DAT'
            else:
                self.ghichu = 'DAT'
            self.DSSV.append([self.masv, self.hoten, self.ngaysinh, self.dtb, self.ghichu])
            print()
    
    def inDSSV(self):
        print('Masv          Ho ten             Ngay sinh              DTB          Ghi Chu')
        for i in range(len(self.DSSV)):
            # print('{}'.format(self.DSSV[i][0]) + '{}'.center(23).format(self.DSSV[i][1]) + '{}'.center(15).format(self.DSSV[i][2]) + '{}'.center(18).format(self.DSSV[i][3]) + '{}'.center(23).format(self.DSSV[i][4]))
            print('000{}          {}           {}             {}          {}'.format(str(self.DSSV[i][0]), self.DSSV[i][1], self.DSSV[i][2], self.DSSV[i][3], self.DSSV[i][4]))
            print()
    def demSVtheoDTB(self):
        dem=0
        for i in range(len(self.DSSV)):
            if self.DSSV[i][3] < 4:
                dem+=1
        if dem==0:
            print('Khong co SV nao co dtb < {}')
        else:
            print('Co {} SV co dtb < 4'.format(dem))

    def timkiemSVtheoMasv(self):
        masv = int(input('Nhap ma SV can tim: '))
        dem=0
        for i in range(len(self.DSSV)):
            if masv==self.DSSV[i][0]:
                dem=1
                print('Masv          Ho ten             Ngay sinh              DTB          Ghi Chu')
                print('000{}          {}           {}             {}          {}'.format(str(self.DSSV[i][0]), self.DSSV[i][1], self.DSSV[i][2], self.DSSV[i][3], self.DSSV[i][4]))
                break
        if dem==0:
            print('Khong ton tai ma SV nay! Moi ban nhap lai ma SV')
            self.timkiemSVtheoMasv()

if __name__=='__main__':
    sv = SV()
    sv.showMenu()
    chon = int(input('Moi ban chon cong viec: '))
    while chon!=0:
        if chon==1:
            print('======================================================')
            print('1. Nhap danh sach SV.')
            sv.nhapDSSV()
            print('======================================================')
        elif chon==2:
            print('======================================================')
            print('2. In danh sach SV.')
            sv.inDSSV()
            print('======================================================')
        elif chon==3:
            print('======================================================')
            print('3. Dem SV co dtb < 4.0.')
            sv.demSVtheoDTB()
            print('======================================================')
        elif chon==4:
            print('======================================================')
            print('4. Tim SV theo masv.')
            sv.timkiemSVtheoMasv()
            print('======================================================')
        else:
            print('Khong co lua chon nay! Moi ban chon lai cong viec')
        chon = int(input('Moi ban chon cong viec: '))
    print('===========================Hen gap lai===========================')