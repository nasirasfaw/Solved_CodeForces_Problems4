t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    if all(abs(a[i] - a[i-1]) == 5 or abs(a[i] - a[i-1]) == 7 for i in range(1, n)):
        print("YES")
    else:
        print("NO")
