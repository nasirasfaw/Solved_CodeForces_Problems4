from math import ceil
t = int(input())
for _ in range(t):
    n, x = map(int, input().split())
    a = list(map(int, input().split()))

    sum1 = ceil(sum(a)/x)
    sum2 = sum(ceil(a[i]/x) for i in range(n))

    print(sum1, sum2)
