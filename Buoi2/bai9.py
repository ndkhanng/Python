# Nhập dữ liệu
dai = float(input("Nhập chiều dài đáy hình khối chữ nhật (cm): "))
rong = float(input("Nhập chiều rộng đáy hình khối chữ nhật (cm): "))
cao = float(input("Nhập chiều cao hình khối chữ nhật (cm): "))
soLe = int(input("Số lượng số lẻ cần hiển thị: "))

# Tính toán
dienTichDay = dai * rong
theTich = dai * rong * cao

# In kết quả

# Cách 1
print("Cách 1: Diện tích đáy hình chữ nhật =",
      round(dienTichDay, soLe), "cm\u00b2")

# Cách 2
print(f"Cách 2: Diện tích đáy hình chữ nhật = "
      f"{dienTichDay:.{soLe}f}cm\u00b2")

# Cách 1
print("Cách 1: Thể tích hình khối=",
      round(theTich, soLe), "cm\u00b3")

# Cách 2
print(f"Cách 2: Thể tích hình khối= "
      f"{theTich:.{soLe}f}cm\u00b3")
