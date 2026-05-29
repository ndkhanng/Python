import math

scp = lambda n: int(math.sqrt(n))**2 == n
sht = lambda n: n > 1 and sum(i for i in range(1, n) if n % i == 0) == n

print("SO CHINH PHUONG:")
for i in range(1, 10001):
    if scp(i):
        print(i, end=" ")

print("\n\nSO HOAN THIEN:")
for i in range(1, 10001):
    if sht(i):
        print(i, end=" ")