t = int(input())
for _ in range(t):
    n = int(input())
    x = list(map(int, input().split()))

    if len(x) == 2 and abs(x[0]-x[1]) > 1:
        print("YES")
    else:
        print("NO")
