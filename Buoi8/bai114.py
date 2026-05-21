import math

def dao_nguoc(n):
    return int(str(n)[::-1])

def ucln(a, b):
    while b != 0:
        a, b = b, a % b
    return a

a = int(input("Nhap a: "))
b = int(input("Nhap b: "))

dem = 0

for i in range(a, b + 1):
    rev = dao_nguoc(i)

    if ucln(i, rev) == 1:
        print(i, end=" ")
        dem += 1

print("\nSo luong:", dem)
