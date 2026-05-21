pairs = [
    ('0', '0'),
    ('1', '1'),
    ('6', '9'),
    ('8', '8'),
    ('9', '6')
]


# a. Sinh strobogrammatic


def generate_strobo(n, total):

    if n == 0:
        return [""]

    if n == 1:
        return ["0", "1", "8"]

    result = []

    middle = generate_strobo(n - 2, total)

    for s in middle:

        for left, right in pairs:

            # không cho số bắt đầu bằng 0
            if n == total and left == '0':
                continue

            result.append(left + s + right)

    return result



# b. Sinh strobogrammatic mở rộng


def generate_extended(n, current):

    if len(current) == n:
        print(current)
        return

    digits = ['0', '1', '6', '8', '9']

    for d in digits:

        # số đầu không được là 0
        if len(current) == 0 and d == '0':
            continue

        generate_extended(n, current + d)



# Main


n = int(input("Nhap n (2-10): "))

# a
print("\n=== Strobogrammatic ===")

strobo = generate_strobo(n, n)

for s in strobo:
    print(s)

# b
print("\n=== Strobogrammatic mo rong ===")

generate_extended(n, "")
