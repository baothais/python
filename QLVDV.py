class Vandongvien:

    maVDV : str
    hoTen : str
    tuoi : int
    canNang : float
    chieuCao : float
    monThidau : str
    list_VDV=[]

    def showMenu(self):
        print('=====================MENU=====================') 
        print('1. Nhap thong tin VDV.')
        print('2. In thong tin VDV.')
        print('3. Cap nhat thong tin VDV.')
        print('4. Them VDV vao danh sach')
        print('5. Xoa VDV khoi danh sach')
        print('6. Tim kiem VDV trong danh sach')
        print('0. Thoat chuong trinh')
        print('==============================================')

    def nhapDSVDV(self):
        for i in range(int(input('Ban muon nhap bao nhieu van dong vien: '))):
            print()
            self.maVDV = input('Nhap ma so cua VDV thu {}: '.format(i+1))
            self.hoten = input('Nhap ho ten cua VDV thu {}: '.format(i+1))
            self.tuoi = int(input('Nhap tuoi cua VDV thu {}: '.format(i+1)))
            self.canNang = float(input('Nhap can nag cua VDV thu {} (kg): '.format(i+1)))
            self.chieuCao = float(input('Nhap chieu cao cua VDV thu {} (cm): '.format(i+1)))
            self.monThidau = input('Nhap mon thi dau cua VDV thu {}: '.format(i+1))
            self.list_VDV.append([self.maVDV, self.hoten, self.tuoi, self.canNang, self.chieuCao, self.monThidau])

    def inDSVDV(self):
        for i in range(len(self.list_VDV)):
            print('Ma so cua VDV thu {} la: {}'.format(i+1, self.list_VDV[i][0]))
            print('Ho ten cua VDV thu {} la: {}'.format(i+1, self.list_VDV[i][1]))
            print('Tuoi cua VDV thu {} la: {}'.format(i+1, self.list_VDV[i][2]))
            print('Can nang cua VDV thu {} la: {}'.format(i+1, self.list_VDV[i][3]))
            print('Chieu cao cua VDV thu {} la: {}'.format(i+1, self.list_VDV[i][4]))
            print('Mon thi dau cua VDV thu {} la: {}'.format(i+1, self.list_VDV[i][5]))
            print()
        if self.list_VDV==[]:
            print('Danh sach VDV trong! Ban hay them VDV vao danh sach.')

    def capNhatVDV(self):
        maVDV = input('Nhap ma so cua VDV can cap nhat thong tin: ')
        dem=0
        for i in range(len(self.list_VDV)):
            if self.list_VDV[i][0]==maVDV:
                dem=1
                self.list_VDV.remove(self.list_VDV[i])
                self.list_VDV
                self.hoten = input('Nhap lai ho ten cua VDV thu {}: '.format(i+1))
                self.tuoi = int(input('Nhap lai tuoi cua VDV thu {}: '.format(i+1)))
                self.canNang = float(input('Nhap lai can nag cua VDV thu {} (kg): '.format(i+1)))
                self.chieuCao = float(input('Nhap lai chieu cao cua VDV thu {} (cm): '.format(i+1)))
                self.monThidau = input('Nhap lai mon thi dau cua VDV thu {}: '.format(i+1))
                self.list_VDV.append([self.maVDV, self.hoten, self.tuoi, self.canNang, self.chieuCao, self.monThidau])
                break
        if dem==0:
            print()
            print('Khong co ma so cua VDV nao trung khop! Moi ban nhap lai ma so cua VDV')
            print('----------------------------------------------')
            self.capNhatVDV()

    # def themVDV(self):
    #     print()
    #     maVDV = input('Nhap ma so cua VDV can them moi: ')
    #     for i in range(len(self.list_VDV)):
    #         while maVDV==self.list_VDV[i][0]:
    #             maVDV = input('maVDV bi trung! Moi ban nhap lai ma so VDV can them moi: ')
    #         self.hoten = input('Nhap ho ten cua VDV can them moi: ')
    #         self.tuoi = int(input('Nhap tuoi cua VDV can them moi: '))
    #         self.canNang = float(input('Nhap can nag cua VDV can them moi (kg): '))
    #         self.chieuCao = float(input('Nhap chieu cao cua VDV can them moi (cm): '))
    #         self.monThidau = input('Nhap mon thi dau cua VDV can them moi: ')
    #         self.list_VDV.append([maVDV, self.hoten, self.tuoi, self.canNang, self.chieuCao, self.monThidau])

    def xoaVDV(self):
        print()
        dem=0
        maVDV = input('Nhap ma so cua VDV ma ban muon xoa: ')
        for i in range(len(self.list_VDV)):
            if self.list_VDV[i][0]==maVDV:
                dem=1
                self.list_VDV.remove(self.list_VDV[i])
                break
        if dem==0:
            print('Khong ton tai ma so VDV can xoa! Moi ban nhap lai ma so VDV can xoa')
            print('----------------------------------------------')
            self.xoaVDV()
    
    def timkiemVDV(self):
        maVDV = input('Nhap ma so cua VDV can tim kiem: ')
        dem=0
        for i in range(len(self.list_VDV)):
            if maVDV==self.list_VDV[i][0]:
                dem=1
                print('Thong tin VDV can tim kiem: ')
                print('Ma so cua VDV thu {} la: {}'.format(i+1, self.list_VDV[i][0]))
                print('Ho ten cua VDV thu {} la: {}'.format(i+1, self.list_VDV[i][1]))
                print('Tuoi cua VDV thu {} la: {}'.format(i+1, self.list_VDV[i][2]))
                print('Can nang cua VDV thu {} la: {}'.format(i+1, self.list_VDV[i][3]))
                print('Chieu cao cua VDV thu {} la: {}'.format(i+1, self.list_VDV[i][4]))
                print('Mon thi dau cua VDV thu {} la: {}'.format(i+1, self.list_VDV[i][5]))
                break
        if dem==0:
            print('Khong ton tai ma so cua VDV! Moi ban nhap lai ma so cua VDV')
            print('----------------------------------------------')
            self.timkiemVDV()

if __name__=='__main__':
    vdv = Vandongvien()
    vdv.showMenu()
    chon = int(input('Moi ban chon cong viec: '))
    while chon!=0:
        if chon==1:
            print('1. Nhap thong tin VDV')
            print('----------------------------------------------')
            vdv.nhapDSVDV()
        elif chon==2:
            print('2. In thong tin VDV')
            print('----------------------------------------------')
            vdv.inDSVDV()
        elif chon==3:
            print('3. Cap nhat thong tin VDV.')
            print('----------------------------------------------')
            vdv.capNhatVDV()
            print()
            print('Danh sach VDV sau khi cap nhat: ')
            print('----------------------------------------------')
            vdv.inDSVDV()
        # elif chon==4:
        #     print('4. Them VDV vao danh sach')
        #     print('----------------------------------------------')
        #     vdv.themVDV()
        #     print()
        #     print('Danh sach VDV sau khi them moi: ')
        #     print('----------------------------------------------')
        #     vdv.inDSVDV()
        elif chon==5:
            print('5. Xoa VDV khoi danh sach')
            print('----------------------------------------------')
            vdv.xoaVDV()
            print()
            print('Danh sach VDV sau khi xoa:')
            print('----------------------------------------------')
            vdv.inDSVDV()
        elif chon==6:
            print('6. Tim kiem VDV trong danh sach')
            print('----------------------------------------------')
            vdv.timkiemVDV()
        else:
            print('Khong co lua chon nay! Moi ban chon lai cong viec')
        print('==============================================')
        chon = int(input('Moi ban chon cong viec: '))
    print('=================Hen gap lai==================')