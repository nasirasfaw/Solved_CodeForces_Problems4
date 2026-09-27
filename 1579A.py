t = int(input())
for _ in range(t):
    s = input()

    na = s.count("A")
    nb = s.count("B")
    nc = s.count("C")

    print("YES" if nb == na + nc else "NO")
