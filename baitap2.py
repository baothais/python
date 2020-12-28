# Bai 7: tính tổng tiền chơi tuỳ vào khung giờ từ 0h-24h:
def tongTien(h, so_gio_choi):
    # số tiền chơi trong 1 giờ
    h_choi = 5000

    # tạo biến tổng tiền chơi net
    sum_tien_choi = 0

    # thời gian chơi từ 0h - 7h
    if h >= 0 and h <= 7:     
        if so_gio_choi < 7:
            sum_tien_choi = so_gio_choi * h_choi * 300
        else:
            sum_tien_choi = (so_gio_choi * h_choi * 300 * 60)/0.15

    # thời gian chơi từ 8h - 17h
    elif h > 7 and h <=17:
        if so_gio_choi >= 6:
            sum_tien_choi = (so_gio_choi * h_choi * 400 * 60)/0.1
        else:
            sum_tien_choi = so_gio_choi * h_choi * 400
            
    # thời gian chơi từ 18h - 24h
    else:
        if so_gio_choi >= 4:
            sum_tien_choi = (so_gio_choi * h_choi * 350 * 60)/0.1
        else:
            sum_tien_choi = so_gio_choi * h_choi * 350

    # trả về tổng tiền chơi
    return sum_tien_choi

def main():
    # nhập thời gian bắt đầu chơi net
    h = int(input("Nhập giờ bắt đầu chơi: "))
    while h < 0 or h > 24:
        h = int(input("Nhập sai, nhập lại giờ bắt đầu chơi: "))

    # nhập số giờ chơi net
    so_gio_choi = int(input("Nhập số giờ chơi: "))
    while so_gio_choi <= 0:
        so_gio_choi = int(input("Nhập sai, nhập lại số giờ chơi > 0: "))

    # in tổng tiền chơi net
    print(f"Tổng tiền chơi là: {tongTien(h, so_gio_choi)}")

    # DANG HOC DEO CHOI!

if __name__=="__main__":
    # gọi hàm main()
    main()




            
            
