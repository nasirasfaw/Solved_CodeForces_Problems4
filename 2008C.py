from math import sqrt
t = int(input())
for _ in range(t):
    l, r = map(int, input().split())
    k = int((-1 + sqrt(1 + 8*(r-l)))/2)

    print(k+1)
