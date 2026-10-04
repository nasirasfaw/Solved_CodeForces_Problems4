t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    
    m = max(a.count(a[i]) for i in range(n))

    print(n-m)
