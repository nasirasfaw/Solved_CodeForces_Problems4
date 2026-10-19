from math import comb
t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    
    a0, a1 = a.count(0), a.count(1)

    s10 = 0
    
    for i in range(a0 + 1):
        s10 += comb(a0, i) * a1

    print(s10)
