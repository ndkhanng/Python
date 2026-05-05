def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


nums = []

while True:
    x = int(input("Nhập số nguyên: "))
    nums.append(x)

    choice = input("Nhập tiếp? (Y/N): ").strip().lower()
    if choice == 'n':
        break


# a) Số nguyên tố
primes = [x for x in nums if is_prime(x)]
print("Số nguyên tố:", primes)


# b) Trung bình âm và dương
neg = [x for x in nums if x < 0]
pos = [x for x in nums if x > 0]

if neg:
    print("TBC số âm:", sum(neg) / len(neg))
else:
    print("Không có số âm")

if pos:
    print("TBC số dương:", sum(pos) / len(pos))
else:
    print("Không có số dương")


# c) Max / Min
print("Max:", max(nums))
print("Min:", min(nums))


# d) Check tăng dần
is_increasing = all(nums[i] <= nums[i+1] for i in range(len(nums)-1))

if is_increasing:
    print("Danh sách tăng dần")
else:
    print("Danh sách KHÔNG tăng dần")