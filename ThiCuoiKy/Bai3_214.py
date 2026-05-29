import math


is_square = lambda n: int(math.sqrt(n)) ** 2 == n

n = int(input("Nhập n: "))

if is_square(n):
    print(n, "là số chính phương")
else:
    print(n, "không phải là số chính phương")



a = int(input("Nhập cạnh a: "))
b = int(input("Nhập cạnh b: "))
c = int(input("Nhập cạnh c: "))


is_triangle = lambda a, b, c: a + b > c and a + c > b and b + c > a

if not is_triangle(a, b, c):
    print("Không phải tam giác")
else:
    if a == b == c:
        print("Tam giác đều")

    elif a == b or b == c or a == c:
        if a*a + b*b == c*c or a*a + c*c == b*b or b*b + c*c == a*a:
            print("Tam giác vuông cân")
        else:
            print("Tam giác cân")

    elif a*a + b*b == c*c or a*a + c*c == b*b or b*b + c*c == a*a:
        print("Tam giác vuông")

    else:
        print("Tam giác thường")