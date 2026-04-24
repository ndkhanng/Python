import math

# a) |n|
abs_val = lambda n: abs(n)

# b) n + 15
add_15 = lambda n: n + 15

# c) x * y
mul = lambda x, y: x * y

# d) kiểm tra bội 13 hoặc 19
is_multiple_13_19 = lambda n: n % 13 == 0 or n % 19 == 0

# e) diện tích hình tròn
circle_area = lambda r: math.pi * r * r

# f) chu vi hình chữ nhật
rectangle_perimeter = lambda d, r: 2 * (d + r)

# g) số chính phương
is_perfect_square = lambda n: int(math.sqrt(n))**2 == n

# h) số nguyên tố
is_prime = lambda n: n > 1 and all(n % i != 0 for i in range(2, int(math.sqrt(n)) + 1))

# i) kiểm tra tam giác
triangle_type = lambda a, b, c: (
    "Không phải tam giác" if a + b <= c or a + c <= b or b + c <= a else
    "Tam giác đều" if a == b == c else
    "Tam giác cân" if a == b or b == c or a == c else
    "Tam giác vuông" if a*a + b*b == c*c or a*a + c*c == b*b or b*b + c*c == a*a else
    "Tam giác thường"
)

# TEST thử cho đỡ ngu
print(abs_val(-5))                 # 5
print(add_15(10))                 # 25
print(mul(3, 4))                  # 12
print(is_multiple_13_19(26))      # True
print(circle_area(3))             # ~28.27
print(rectangle_perimeter(5, 3))  # 16
print(is_perfect_square(16))      # True
print(is_prime(17))               # True
print(triangle_type(3, 4, 5))     # Tam giác vuông