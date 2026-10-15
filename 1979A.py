t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    m1 = [max(a[i],a[i+1]) for i in range(n-1)]

    print(min(m1)-1)
