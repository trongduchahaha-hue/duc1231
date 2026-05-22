tong_tien = int(input("Nhập tổng số tiền hóa đơn (VND): "))

if tong_tien >= 500000:
    tien_giam = tong_tien * 0.1
    phan_tram = "10%"
    
else:
    tien_giam = 0
    phan_tram = "0%"

so_tien_phai_tra = tong_tien - tien_giam

tien_giam = int(tien_giam)
so_tien_phai_tra = int(so_tien_phai_tra)

print("----------------------------------------")
print(f"Tổng tiền ban đầu: {tong_tien} VND")
print(f"Mức chiết khấu: {phan_tram}")
print(f"Số tiền được giảm: {tien_giam} VND")
print("----------------------------------------")
print(f"SỐ TIỀN KHÁCH PHẢI TRẢ: {so_tien_phai_tra} VND")