t = int(input())
for _ in range(t):
    n = int(input())
    s = input()

    position = {}

    for i in range(n):
        if s[i] not in position:
            position[s[i]] = i % 2
        elif position[s[i]] != i % 2:
            print("NO")
            break
    else:
        print("YES")
