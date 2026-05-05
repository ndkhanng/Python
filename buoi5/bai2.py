from collections import Counter

s1 = input("Nhập S1: ")
s2 = input("Nhập S2: ")

# chuyển thành Counter (dict đếm ký tự)
c1 = Counter(s1)
c2 = Counter(s2)

# a) ký tự chung
common = c1 & c2
print("Ký tự chung:", list(common.keys()))

# b) đếm ký tự riêng
only_s1 = set(c1.keys()) - set(c2.keys())
only_s2 = set(c2.keys()) - set(c1.keys())

print("Số ký tự chỉ có trong S1:", len(only_s1))
print("Số ký tự chỉ có trong S2:", len(only_s2))

# c) in ký tự riêng
print("Ký tự chỉ có trong S1:", list(only_s1))
print("Ký tự chỉ có trong S2:", list(only_s2))