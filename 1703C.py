t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    b = []
    for _ in range(n):
        m, s = input().split()
        b.append([int(m), s])
    a1 = []
    for i in range(n):
        u = b[i][1].count("U")
        d = b[i][1].count("D")
        if u >= d:
            a1.append(a[i]-(u-d))
        else:
            a1.append(a[i]+(d-u))  
    for i in range(n):
        if a1[i] < 0 or a1[i] >= 10:
            a1[i] = max(abs(a1[i])-10, 10-abs(a1[i])) 
    a2 = [str(x) for x in a1]
    print(*a2)
