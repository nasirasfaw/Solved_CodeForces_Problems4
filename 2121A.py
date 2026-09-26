t = int(input())
for _ in range(t):
    n, s = map(int, input().split())
    x = list(map(int, input().split()))

    md = min(abs(s-x[0]), abs(s-x[n-1]))
    total = md + max(x) - min(x)
    
    print(total)
