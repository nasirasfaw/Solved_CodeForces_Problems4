t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    ab = [[a[i], b[i]] for i in range(n)]
    ab.sort()
    for i in range(n):
        if ab[i][0] <= k:
            k += ab[i][1]

    print(k)
