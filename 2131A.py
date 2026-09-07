t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    decrease_a = 0
    for i in range(n):
        if a[i]-b[i] > 0:
            decrease_a += a[i]-b[i]

    print(decrease_a + 1)
