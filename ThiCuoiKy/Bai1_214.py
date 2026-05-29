dai = float(input("Nhập chiều dài đáy hình khối chữ nhật (cm): "))
rong = float(input("Nhập chiều rộng đáy hình khối chữ nhật (cm): "))
cao = float(input("Nhập chiều cao hình khối chữ nhật (cm): "))

phan_nguyen = int(dai)
dem_le = 0

for so in str(abs(phan_nguyen)):
    if int(so) % 2 != 0:
        dem_le += 1

dien_tich_day = dai * rong
the_tich = dai * rong * cao

print("Số lượng số lẻ của phần nguyên chiều dài:", dem_le)
print(f"Diện tích đáy hình chữ nhật = {dien_tich_day:.2f} cm\u00b2")
print(f"Thể tích hình khối = {the_tich:.2f} cm\u00b3")