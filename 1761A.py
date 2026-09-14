t = int(input())
for _ in range(t):
    n, a, b = map(int, input().split())

    if n == a == b or n - (a+b) >= 2:
        print("YES")
    else:
        print("NO")
