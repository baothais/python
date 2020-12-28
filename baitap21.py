import math
class Diem:
    x : int
    y : int
    list_diem = []
    def showMenu(self):
        print('========================MENU========================')
        print('1. Viết thủ tục nhập vào một điểm bất kỳ')
        print('2. Viết thủ tục xuất ra một điểm')
        print('3. Viết hàm tính khoảng cách giữa hai điểm bất kỳ')
        print('4. Nhập vào ba điểm bất kỳ, xét xem ba điểm đó có thể thành lập thành một tam giác không. Nếu có hãy tính diện tích của tam giác đó.')
        print('====================================================')
    def nhapDiem(self):
        for i in range(int(input('So diem ban muon nhap: '))):
            self.x = int(input('Nhap hoang do diem thu {}: '.format(i+1)))
            self.y = int(input('Nhap tung do diem thu {}: '.format(i+1)))
            self.list_diem.append([self.x, self.y])
    def inDiem(self):
        for i in range(len(self.list_diem)):
            print('Toa do diem thu {}: (x={}, y={})'.format(i+1, self.list_diem[i][0], self.list_diem[i][1]))
    def distance(self):
        for i in range(len(self.list_diem)):
            print('Khoang cach giua 2 diem la: {}'.format(math.sqrt((self.list_diem[i+1][0]-self.list_diem[i][0])**2 + (self.list_diem[i+1][1]-self.list_diem[i][1])**2)))
            break
    def dienTich(self):
        for i in range(len(self.list_diem)):
            AB = math.sqrt((self.list_diem[i+1][0]-self.list_diem[i][0])**2 + (self.list_diem[i+1][1]-self.list_diem[i][1])**2)
            BC = math.sqrt((self.list_diem[i+2][0]-self.list_diem[i+1][0])**2 + (self.list_diem[i+2][1]-self.list_diem[i+1][1])**2)
            AC = math.sqrt((self.list_diem[i+2][0]-self.list_diem[i][0])**2 + (self.list_diem[i+2][1]-self.list_diem[i][1])**2)
            if AB+BC>AC and AB+AC>BC and AC+BC>AB:
                print('3 diem vua nhap co the tao thanh 1 tam giac')
                p = (AB+BC+AC)/2
                h = (2*math.sqrt(p*(p-AB)*(p-BC)*(p-AC)))/AB
                print('Dien tich tam giac tao thanh tu 3 diem tren la: {:.2f}'.format((AB*h)/2))
                break
            else:
                print('3 diem vua nhap khong the tao thanh 1 tam giac')
                break

if __name__=='__main__':
    d = Diem()
    d.showMenu()
    chon = int(input('Moi ban chon cong viec: '))
    while chon!=0:
        if chon==1:
            d.nhapDiem()
        elif chon==2:
            print('Ket qua toa do nhung diem vua nhap')
            d.inDiem()
        elif chon==3:
            d.distance()
        elif chon==4:
            d.dienTich()
        else:
            print('Khong co lua chon nay! Moi ban chon lai cong viec')
        chon = int(input('Moi ban chon cong viec: '))
    print('====================Hen gap lai=====================')