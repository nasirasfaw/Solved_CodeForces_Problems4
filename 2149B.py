t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    
    a.sort()

    maxd = max(a[i]-a[i-1] for i in range(1, n, 2))

    print(maxd)
