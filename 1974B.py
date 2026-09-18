t = int(input())
for _ in range(t):
    n = int(input())
    s = input()

    r = list(set(s))
    r.sort()
    r2 = [r[len(r)-i-1] for i in range(len(r))]
    
    s1 = ""
    for x in s:
        s1 += r2[len(r2) - r2.index(x) - 1]

    print(s1)
