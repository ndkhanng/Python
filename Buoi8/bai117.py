n = input("Nhap n: ")

S = 0

for i in range(len(n)):
    for j in range(i + 1, len(n) + 1):
        so_con = int(n[i:j])
        S += so_con ** 2

print("Tong S =", S)
