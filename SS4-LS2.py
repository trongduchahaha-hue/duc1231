tong_doanh_thu = 0

so_ngay_dat_muc_tieu = 0

print("=== HỆ THỐNG THỐNG KÊ DOANH THU TUẦN - RIKKEI STORE ===")
print("Vui lòng nhập doanh thu cho từng ngày:\n")

for ngay in range(1, 8):

    doanh_thu_ngay = int(input(f"Nhập doanh thu Ngày {ngay} (VND): "))
    
    tong_doanh_thu = tong_doanh_thu + doanh_thu_ngay
    if doanh_thu_ngay >= 5000000:
        so_ngay_dat_muc_tieu = so_ngay_dat_muc_tieu + 1

doanh_thu_trung_binh = tong_doanh_thu / 7

doanh_thu_trung_binh = int(doanh_thu_trung_binh)

print("\n" + "="*45)
print("       BÁO CÁO DOANH THU KINH DOANH TUẦN")
print("="*45)
print(f"- Tổng doanh thu cả tuần   : {tong_doanh_thu} VND")
print(f"- Doanh thu trung bình/ngày: {doanh_thu_trung_binh} VND")
print(f"- Số ngày đạt mục tiêu lớn : {so_ngay_dat_muc_tieu} / 7 ngày")
print("="*45)