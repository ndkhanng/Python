
# STROBOGRAMMATIC NUMBERS

mapping = {
    '0': '0',
    '1': '1',
    '6': '9',
    '8': '8',
    '9': '6'
}


# kiểm tra số nguyên tố
def is_prime(n):

    if n < 2:
        return False

    for i in range(2, int(n ** 0.5) + 1):

        if n % i == 0:
            return False

    return True


# kiểm tra strobogrammatic
def is_strobogrammatic(n):

    s = str(n)

    left = 0
    right = len(s) - 1

    while left <= right:

        c1 = s[left]
        c2 = s[right]

        if c1 not in mapping:
            return False

        if mapping[c1] != c2:
            return False

        left += 1
        right -= 1

    return True


# xoay số
def rotate_number(n):

    s = str(n)

    rotated = ""

    for c in reversed(s):

        if c not in mapping:
            return -1

        rotated += mapping[c]

    return int(rotated)


# strobogrammatic mở rộng
def is_extended_strobo(n):

    return rotate_number(n) != -1


LIMIT = 1000000

# a

print("a. So strobogrammatic:\n")

for i in range(LIMIT):

    if is_strobogrammatic(i):
        print(i, end=" ")

# b

print("\n\nb. So nguyen to strobogrammatic:\n")

for i in range(LIMIT):

    if is_strobogrammatic(i) and is_prime(i):
        print(i, end=" ")

# c

print("\n\nc. So strobogrammatic mo rong:\n")

for i in range(LIMIT):

    if is_extended_strobo(i):
        print(i, end=" ")

# d

print("\n\nd. So nguyen to strobogrammatic mo rong:\n")

for i in range(LIMIT):

    if is_extended_strobo(i) and is_prime(i):
        print(i, end=" ")

# e

print("\n\ne. Khong phai strobogrammatic")
print("   khong phai so nguyen to")
print("   nhung so xoay cua no la so nguyen to:\n")

for i in range(LIMIT):

    if not is_strobogrammatic(i) and not is_prime(i):

        rotated = rotate_number(i)

        if rotated != -1 and is_prime(rotated):
            print(i, end=" ")
