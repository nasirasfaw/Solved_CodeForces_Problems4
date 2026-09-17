t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))

    a.sort()

    m = n - a[k-1]
    op1 = m - (k-1)
    op2 = m
    print(op1 + op2)
