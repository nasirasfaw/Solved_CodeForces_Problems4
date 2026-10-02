t = int(input())
for _ in range(t):
    n = int(input())
    s = input()

    for x in s[1:n-1]:
        if s.count(x) > 1:
            print("YES")
            break
    else:
        print("NO")
