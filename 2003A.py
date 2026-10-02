t = int(input())
for _ in range(t):
    n = int(input())
    s = input()

    if n > 1 and s[0] != s[n-1]:
        print("YES")
    else:
        print("NO")
