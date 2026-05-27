import math

# Hàm kiểm tra số nguyên tố
def laSoNguyenTo(n):
    if n < 2:
        return False

    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False

    return True


# =========================================
# Bài 1
# =========================================
def bangCuuChuong(a, b):

    if a < b:
        start = a
        end = b
    else:
        start = b
        end = a

    for i in range(start, end + 1):
        print(f"\nBảng cửu chương {i}")

        for j in range(1, 11):
            print(f"{i} x {j} = {i*j}")


# =========================================
# Bài 2
# =========================================
def kiemTraSoNguyenTo():
    n = int(input("Nhập n: "))

    if laSoNguyenTo(n):
        print(n, "là số nguyên tố")
    else:
        print(n, "không phải là số nguyên tố")


# =========================================
# Bài 3
# =========================================
def lietKeSoNguyenTo():
    n = int(input("Nhập n: "))

    print("Các số nguyên tố <", n, "là:")

    for i in range(2, n):
        if laSoNguyenTo(i):
            print(i, end=" ")


# =========================================
# Bài 4
# =========================================
def demSoNguyenTo():
    n = int(input("Nhập n: "))

    dem = 0

    for i in range(2, n):
        if laSoNguyenTo(i):
            dem += 1

    print("Số lượng số nguyên tố <", n, "là:", dem)


# =========================================
# Bài 5
# =========================================
def uocSoNguyenTo():
    n = int(input("Nhập n: "))

    print("Các ước số nguyên tố của", n, "là:")

    for i in range(1, n + 1):
        if n % i == 0 and laSoNguyenTo(i):
            print(i, end=" ")

# Chương trình chính

#1
a, b = map(int, input("Nhập a,b: ").split(","))

bangCuuChuong(a, b)

print("\n----------------")

#2
kiemTraSoNguyenTo()

print("\n----------------")

#3
lietKeSoNguyenTo()

print("\n----------------")

#4
demSoNguyenTo()

print("\n----------------")

#5
uocSoNguyenTo()
