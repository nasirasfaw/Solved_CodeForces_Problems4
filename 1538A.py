t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    
    m1, m2 = min(a), max(a)
    i1, i2 = a.index(m1), a.index(m2)
    mi12 = abs(i1 - i2)

    m = min(i1, i2, n-i1-1, n-i2-1)
    if m == i1 or m == n-i1-1:
        mx = min(i2, n-i2-1)+1
    else:
        mx = min(i1, n-i1-1)+1

    m12 = min(mi12, mx)
    
    print(m + m12 + 1)
