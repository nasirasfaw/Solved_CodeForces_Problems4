t = int(input())
for _ in range(t):
    s = input()

    s1 = set()
    s2 = ""
    for i in range(len(s)):
        if s.count(s[i]) == 2:
            s1.add(s[i])
        else:
            s2 += s[i]
            
    s1 = "".join(list(s1))

    print(s1+s1+s2)
