class Menu:
    food : str
    a=[]
    def showMenu(self):
        print('==================MENU=================')
        print('1. Nhap thuc don vao a tu ban phim')
        print('2. In thuc don vua nhap len man hinh')
        print('3. Xoa cac ky tu trang trong ten moi thuc don')
        print('4. Dem xem trong ten moi loai thuoc thuc don co bao nhieu tu')   
        print('5. Dem xem moi ky tu trong moi loai thuoc thuc don xuat hien bao nhieu lan')
        print('6. In dao nguoc thuc don ra man hinh')
        print('0. De thoat chuong trinh')
        print('=======================================')

    def nhapMenu(self):
        n = int(input('Ban muon nhap bao nhieu mon an: '))
        for i in range(n):
            self.food = input('Moi ban nhap mon an thu {}: '.format(i+1))
            self.a.append(self.food)
    def inMenu(self):
        for i in range(len(self.a)):
            print('Mon an thu {}: {}'.format(i+1, self.a[i]))
    def xoaKyTuSpace(self):
        list_s=[]
        for i in range(len(self.a)):
            old_list_s = [self.a[i][j] for j in range(len(self.a[i])) if not self.a[i][j].isspace()]
            list_s.append(old_list_s)
            print('Mon an thu {} sau khi xoa ky tu space: {}'.format(i+1, ('').join(list_s[i])))
    def demKyTu(self):
        list_dem=[len(self.a[i]) for i in range(len(self.a))]
        for i in range(len(list_dem)):
            print('So ky tu cua mon an thu {}: {}'.format(i+1, list_dem[i]))
    def demAllKyTu(self):
        d1 = {}
        for i in range(len(self.a)):
            d2 = {self.a[i][j] : f'{self.a[i].count(self.a[i][j])} ky tu' for j in range(len(self.a[i]))}
            d1[i] = d2
            print('So ky tu trong ten mon an thu {}: {}'.format(i+1, d1[i]))
    def inDaoNguoc(self):
        for i in range(len(self.a)):
            print('Mon an thu {}: {}'.format(i+1, self.a[i][::-1]))
if __name__=='__main__':
    menu = Menu()
    menu.showMenu()
    chon = int(input('Moi ban chon cong viec: '))
    while chon!=0:
        if chon==1:
            print('Nhap thuc don vao a:')
            menu.nhapMenu()
        elif chon==2:
            print('Menu ban vua nhap:')
            menu.inMenu()
        elif chon==3:
            print('Xoa khoang trang trong thuc don')
            menu.xoaKyTuSpace()
        elif chon==4:
            print('Dem so ky tu mon an trong thuc don')
            menu.demKyTu()
        elif chon==5:
            print('So ky tu trong moi mon an cua thuc don')
            menu.demAllKyTu()
        elif chon==6:
            print('Mon an sau khi bi dao nguoc')
            menu.inDaoNguoc()
        else:
            print('Khong co lua chon nay!')
        chon = int(input('Moi ban chon cong viec: '))
    print('============Hen gap lai===============')


