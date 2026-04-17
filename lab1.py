# Nhập dữ liệu
dai = input("Nhập chiều dài đáy hình chữ nhật (cm): ")
rong = input("Nhập chiều rộng đáy hình chữ nhật (cm): ")
cao = input("Nhập chiều cao hình khối chữ nhật (cm): ")

print("dai = ", dai)
print("rong = ", rong)
print("cao = ", cao)

# Định dạng số lẻ
sole = input("Số lượng số lẻ cần hiển thị: ")
dinhdang = "{:." + sole + "f}"

dai = dinhdang.format(eval(dai))
rong = dinhdang.format(eval(rong))
cao = dinhdang.format(eval(cao))

print("dai = ", dai)
print("rong = ", rong)
print("cao = ", cao)

# Tính toán
dientich = float(dai) * float(rong)
thetich = float(dai) * float(rong) * float(cao)

print("Diện tích đáy hình chữ nhật = ", dientich, "cm2")
print("Thể tích hình khối = ", thetich, "cm3")