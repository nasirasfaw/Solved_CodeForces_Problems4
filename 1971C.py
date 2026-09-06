t = int(input())
for _ in range(t):
    a, b, c, d = map(int, input().split())

    min1, max1 = min(a, b), max(a, b)
    min2, max2 = min(c, d), max(c, d)

    if (min1 < min2 and max1 > max2) or (min2 < min1 and max2 > max1):
        print("NO")
    elif min2 > max1 or min1 > max2:
        print("NO")
    else:
        print("YES")
