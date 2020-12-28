class SV:
    masv : int
    hoten : str
    ngaysinh : str
    dtb : float
    ghichu : str
    DSSV = []

    def showMenu(self):
        print('====================Chuong Trinh====================')
        print('1. Nhập vào một danh sách sinh viên lưu thông tin vào trong mảng.')
        print('2. In danh sách sinh viên.')
        print('3. Hãy cho biết trong danh sách có bao nhiêu sinh viên có DTB <4.0.')
        print("""4. Nhập vào một mã sinh viên bất kỳ, tìm xem trong danh sách có sinh viên đó hay
không? Nếu có in thông tin sinh viên đó lên màn hình.""")
        print("""5. Nhập vào một tên sinh viên bất kỳ, tìm xem có sinh viên đó hay không? Nếu có in
tất cả các sinh viên có tên đã nhập ra màn hình.""")
        print("""6. Nhập vào mã của một sinh viên, xóa thông tin sinh viên theo mã đã nhập ra khỏi
danh sách. In danh sách sau khi xóa ra màn hình.""")
        print('7. Đếm xem có bao nhiêu sinh viên sinh năm 1993 có trong danh sách đã nhập.')
        print('8. Sắp xếp danh sách theo thứ tự giảm dần của điểm trung bình.')
        print("""9. Giả sử danh sách đã sx giảm dần theo điểm trung bình. Nhập thông tin của sinh
mới bất kỳ từ bàn phím, chèn thông tin sinh viên đã nhập vào danh sách sao cho
sau khi chèn danh sách vẫn giảm dần theo điểm trung bình.""")
        print('=====================================================')

    def nhapDSSV(self):
        for i in range(int(input('Ban muon nhap bao nhieu SV: '))):
            self.masv = int(input('Nhap ma SV thu {}: '.format(i+1)))
            if len(self.DSSV)!=0:
                for j in range(len(self.DSSV)):
                    while self.masv == self.DSSV[j][0]:
                        self.masv = int(input('Ma so SV bi trung! Moi ban nhap lai ma SV thu {}: '.format(i+1)))
            self.hoten = input('Nhap ho ten SV thu {}: '.format(i+1))
            self.ngaysinh = input('Nhap ngay sinh SV thu {} (dd/mm/yy): '.format(i+1))
            self.dtb = float(input('Nhap dtb SV thu {} (0.0 =< dtb <= 10.0): '.format(i+1)))
            if self.dtb >= 4:
                self.ghichu = "DAT"
            else:
                self.ghichu = "KHONG DAT"
            self.DSSV.append([self.masv, self.hoten, self.ngaysinh, self.dtb, self.ghichu])
            print()

    def inDSSV(self):
        # string = 'Masv\Ho ten\Ngay sinh\DTB\Ghi chu'
        # print(string.expandtabs())
        for i in range(len(self.DSSV)):
            print('Ma SV thu {}: {}'.format(i+1, self.DSSV[i][0]))
            print('Ho ten SV thu {}: {}'.format(i+1, self.DSSV[i][1]))
            print('Ngay sinh SV thu {}: {}'.format(i+1, self.DSSV[i][2]))
            print('Diem trung binh SV thu {}: {}'.format(i+1, self.DSSV[i][3]))
            print('Ket qua SV thu {}: {}'.format(i+1, self.DSSV[i][4]))
            print()
            # print(('            ').join(self.DSSV[i]))

    def demSVtheoDTB(self):
        dem=0
        print('Thong tin SV co dtb < 4:')
        for i in range(len(self.DSSV)):
            if self.DSSV[i][3] < 4.0:
                dem+=1
                # print('Ma SV thu {}: {}'.format(i+1, self.DSSV[i][0]))
                # print('Ho ten SV thu {}: {}'.format(i+1, self.DSSV[i][1]))
                # print('Ngay sinh SV thu {}: {}'.format(i+1, self.DSSV[i][2]))
                # print('Diem trung binh SV thu {}: {}'.format(i+1, self.DSSV[i][3]))
                # print('Ket qua SV thu {}: {}'.format(i+1, self.DSSV[i][4]))
                # print()
        print('Co {} sinh vien co dtb < 4'.format(dem))

    def timkiemSVtheoMaso(self):
        masv = int(input('Nhap ma SV can tim: '))
        for i in range(len(self.DSSV)):
            if masv==self.DSSV[i][0]:
                print('Ma SV thu {}: {}'.format(i+1, self.DSSV[i][0]))
                print('Ho ten SV thu {}: {}'.format(i+1, self.DSSV[i][1]))
                print('Ngay sinh SV thu {}: {}'.format(i+1, self.DSSV[i][2]))
                print('Diem trung binh SV thu {}: {}'.format(i+1, self.DSSV[i][3]))
                print('Ket qua SV thu {}: {}'.format(i+1, self.DSSV[i][4]))
                break
    
    def timkiemSVtheoTen(self):
        ten = input('Nhap ten SV can tim: ')
        dem=0
        for i in range(len(self.DSSV)):
            if ten==self.DSSV[i][1].split(' ')[-1]:
                print('=====================================================')
                print('Thong tin SV can tim la:')
                dem+=1
                print('Ma SV thu {}: {}'.format(i+1, self.DSSV[i][0]))
                print('Ho ten SV thu {}: {}'.format(i+1, self.DSSV[i][1]))
                print('Ngay sinh SV thu {}: {}'.format(i+1, self.DSSV[i][2]))
                print('Diem trung binh SV thu {}: {}'.format(i+1, self.DSSV[i][3]))
                print('Ket qua SV thu {}: {}'.format(i+1, self.DSSV[i][4]))
                print('=====================================================')
                break
        if dem==0:
            print('Khong ton tai SV co ten la {}. Moi ban nhap lai ten SV can tim'.format(ten))
            self.timkiemSVtheoTen()  

    def xoaSV(self):
        masv = int(input('Nhap ma SV can xoa: '))
        dem=0
        for i in range(len(self.DSSV)):
            if masv==self.DSSV[i][0]:
                dem=1
                self.DSSV.remove(self.DSSV[i])
                break
        if dem==0:
            print('Khong ton tai SV co masv = {}. Moi ban nhap lai ma SV can xoa: '.format(masv))
            self.xoaSV()
        else:
            print('=====================================================')
            print('Danh sach SV sau khi xoa: ')
            self.inDSSV()
            print('=====================================================')
        
    def demSVtheoNamsinh(self):
        namsinh = '1993'
        dem=0
        for i in range(len(self.DSSV)):
            if namsinh==self.DSSV[i][2].split('/')[-1]:
                dem+=1
        if dem==0:
            print('=====================================================')
            print('Khong ton tai SV nao co nam sinh la {}.'.format(namsinh))
            print('=====================================================')
        else:
            print('=====================================================')
            print('Co {} SV co nam sinh la {}'.format(dem, namsinh))
            print('=====================================================')

    def sapxepDTB(self):
        self.DSSV.sort(key=lambda x: x[3], reverse=True)
        self.inDSSV()

    def chenSV(self):
        masv = int(input('Nhap ma so SV can them: '))
        for i in range(len(self.DSSV)):
            while masv==self.DSSV[i][0]:
                masv = int(input('Nhap ma so SV can them: '))
        self.hoten = input('Nhap ho ten SV: ')
        self.ngaysinh = input('Nhap ngay sinh SV (dd/mm/yy): ')
        self.dtb = float(input('Nhap dtb SV (0.0 =< dtb <= 10.0): '))
        if self.dtb >= 4:
            self.ghichu = "DAT"
        else:
            self.ghichu = "KHONG DAT"
        self.DSSV.append([masv, self.hoten, self.ngaysinh, self.dtb, self.ghichu])

if __name__=='__main__':
    sv = SV()
    sv.showMenu()
    chon = int(input('Moi ban chon cong viec: '))
    while chon!=0:
        if chon==1:
            print('1. Nhập vào một danh sách sinh viên lưu thông tin vào trong mảng.')
            sv.nhapDSSV()
        elif chon==2:
            print('2. In danh sách sinh viên.')
            sv.inDSSV()
        elif chon==3:
            print('3. Hãy cho biết trong danh sách có bao nhiêu sinh viên có DTB <4.0.')
            sv.demSVtheoDTB()
        elif chon==4:
            print("""4. Nhập vào một mã sinh viên bất kỳ, tìm xem trong danh sách có sinh viên đó hay
không? Nếu có in thông tin sinh viên đó lên màn hình.""")
            sv.timkiemSVtheoMaso()
        elif chon==5:
            print("""5. Nhập vào một tên sinh viên bất kỳ, tìm xem có sinh viên đó hay không? Nếu có in
tất cả các sinh viên có tên đã nhập ra màn hình.""")
            sv.timkiemSVtheoTen()
        elif chon==6:
            print("""6. Nhập vào mã của một sinh viên, xóa thông tin sinh viên theo mã đã nhập ra khỏi
danh sách. In danh sách sau khi xóa ra màn hình.""")
            sv.xoaSV()
        elif chon==7:
            print('7. Đếm xem có bao nhiêu sinh viên sinh năm 1993 có trong danh sách đã nhập.')
            sv.demSVtheoNamsinh()
        elif chon==8:
            print('8. Sắp xếp danh sách theo thứ tự giảm dần của điểm trung bình.')
            sv.sapxepDTB()
        elif chon==9:
            print("""9. Giả sử danh sách đã sx giảm dần theo điểm trung bình. Nhập thông tin của sinh
mới bất kỳ từ bàn phím, chèn thông tin sinh viên đã nhập vào danh sách sao cho
sau khi chèn danh sách vẫn giảm dần theo điểm trung bình.""")
            sv.chenSV()
        else:
            print('Khong co lua chon nay! Moi ban chon lai cong viec')
        chon = int(input('Moi ban chon cong viec: ')) 
    print('====================Hen gap lai====================')