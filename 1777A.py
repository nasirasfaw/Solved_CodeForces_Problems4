t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    count = 0
    for i in range(1, n):
        if a[i-1]%2 == a[i]%2:
            count += 1

    print(count)
