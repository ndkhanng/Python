import math

def tongUoc(n):
    if n == 1:
        return 0

    tong = 1

    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            tong += i

            if i != n // i:
                tong += n // i

    return tong
# a) Số thân thiện
soThanThien = lambda n: n > 9 and math.gcd(n, int(str(n)[::-1])) == 1

print("=== Số thân thiện ===")
result = []

for i in range(1, 1000001):
    if soThanThien(i):
        result.append(i)

print("Số lượng:", len(result))
print("100 số đầu:")
print(*result[:100])

# b) Số chính phương
soChinhPhuong = lambda n: int(math.sqrt(n)) ** 2 == n

print("\n\n=== Số chính phương ===")
result = []

for i in range(1, 1000001):
    if soChinhPhuong(i):
        result.append(i)

print("Số lượng:", len(result))
print("100 số đầu:")
print(*result[:100])

# c) Số đồng nhất
# Cách 1: dùng all
soDongNhat1 = lambda n: (
    lambda s: all(ch == s[0] for ch in s)
)(str(n))

# Cách 2: dùng any
soDongNhat2 = lambda n: not any(ch != str(n)[0] for ch in str(n))

print("\n\n=== Số đồng nhất (all) ===")
result = []

for i in range(1, 1000001):
    if soDongNhat2(i):
        result.append(i)

print("Số lượng:", len(result))
print("100 số đầu:")
print(*result[:100])

print("\n\n=== Số đồng nhất (any) ===")
result = []

for i in range(1, 1000001):
    if soDongNhat2(i):
        result.append(i)

print("Số lượng:", len(result))
print("100 số đầu:")
print(*result[:100])

# d) Số hoàn thiện
soHoanThien = lambda n: tongUoc(n) == n

print("\n\n=== Số hoàn thiện ===")
result = []

for i in range(1, 1000001):
    if soHoanThien(i):
        result.append(i)

print("Số lượng:", len(result))
print("100 số đầu:")
print(*result[:100])

# e) Số phong phú
#soPhongPhu = lambda n: sum(i for i in range(1, n) if n % i == 0) > n
soPhongPhu = lambda n: tongUoc(n) > n

print("\n\n=== Số phong phú ===")
result = []

for i in range(1, 1000001):
    if soPhongPhu(i):
        result.append(i)

print("Số lượng:", len(result))
print("100 số đầu:")
print(*result[:100])

# f) Số tăng dần
soTangDan = lambda n: all(str(n)[i] <= str(n)[i+1] for i in range(len(str(n)) - 1))

print("\n\n=== Số tăng dần ===")
result = []

for i in range(1, 1000001):
    if soTangDan(i):
        result.append(i)

print("Số lượng:", len(result))
print("100 số đầu:")
print(*result[:100])

# g) Số Armstrong
soArmstrong = lambda n: sum(int(ch) ** len(str(n)) for ch in str(n)) == n

print("\n\n=== Số Armstrong ===")
result = []

for i in range(1, 1000001):
    if soArmstrong(i):
        result.append(i)

print("Số lượng:", len(result))
print("100 số đầu:")
print(*result[:100])

# h) Số nguyên tố
# Cách 1
soNguyenTo1 = lambda n: n > 1 and len([i for i in range(1, n + 1) if n % i == 0]) == 2

# Cách 2
soNguyenTo2 = lambda n: n > 1 and sum(i for i in range(1, n + 1) if n % i == 0) == n + 1

# Cách 3
soNguyenTo3 = lambda n: n > 1 and not any(n % i == 0 for i in range(2, int(math.sqrt(n)) + 1))

# Cách 4
def F(k):
    return k > 1 and len(list(filter(lambda x: k % x == 0, range(2, k)))) == 0

print("\n\n=== Số nguyên tố (Cách 3) ===")

result = []

for i in range(1, 1000001):
    if soNguyenTo3(i):
        result.append(i)

print("Số lượng:", len(result))
print(*result[:100])

# i) Số Palindrome
soPalindrome = lambda n: str(n) == str(n)[::-1]

print("\n\n=== Số Palindrome ===")
result = []

for i in range(1, 1000001):
    if soPalindrome(i):
        result.append(i)

print("Số lượng:", len(result))
print("100 số đầu:")
print(*result[:100])

# j) Số nguyên tố Palindrome
soNguyenToPalindrome = lambda n: soPalindrome(n) and soNguyenTo3(n)

print("\n\n=== Số nguyên tố Palindrome ===")
result = []

for i in range(1, 1000001):
    if soNguyenToPalindrome(i):
        result.append(i)

print("Số lượng:", len(result))
print("100 số đầu:")
print(*result[:100])

# k) Số lộc phát
# Cách 1: dùng all
soLocPhat1 = lambda n: all(ch in "68" for ch in str(n))

# Cách 2: đếm số 6 và 8
soLocPhat2 = lambda n: str(n).count('6') + str(n).count('8') == len(str(n))

print("\n\n=== Số lộc phát ===")
result = []

for i in range(1, 1000001):
    if soLocPhat1(i):
        result.append(i)

print("Số lượng:", len(result))
print("100 số đầu:")
print(*result[:100])

# l) Số lộc phát Palindrome
soLocPhatPalindrome = lambda n: soLocPhat1(n) and soPalindrome(n)

print("\n\n=== Số lộc phát Palindrome ===")
result = []

for i in range(1, 1000001):
    if soLocPhatPalindrome(i):
        result.append(i)

print("Số lượng:", len(result))
print("100 số đầu:")
print(*result[:100])
