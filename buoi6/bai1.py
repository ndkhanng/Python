# iii. Nhap so dien thoai va in ra cac so khong xuat hien

s = input("Nhap so dien thoai: ")

khong_co = []

for i in range(10):
    if str(i) not in s:
        khong_co.append(i)

print("Cac ky so khong xuat hien:", khong_co)


# iv. Tim tu dau tien lap lai trong chuoi

s = input("Nhap chuoi: ")

tu = s.split()

da_xuat_hien = []

ket_qua = None

for x in tu:
    if x in da_xuat_hien:
        ket_qua = x
        break
    da_xuat_hien.append(x)

print("Tu lap dau tien:", ket_qua)