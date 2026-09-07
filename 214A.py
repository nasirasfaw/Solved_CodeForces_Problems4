from math import sqrt
n, m = map(int, input().split())

count = 0
for a in range(int(sqrt(n))+1):
    b = n - a**2
    if a + b**2 == m:
        count += 1

print(count)
