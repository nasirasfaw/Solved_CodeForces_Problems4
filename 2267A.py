t = int(input())
for _ in range(t):
    n, c = input().split()
    s = input()
    n = int(n)
    k = n//2
    if n % 2 == 0:
        s1, s2 = s[:k], s[k:]
    else:
        s1, s2 = s[:k], s[k+1:]
    s2 = s2[::-1]
    cs12 = s1.count(c) + s2.count(c)
    count = 0
    for i in range(k):
        if s1[i] != s2[i]:
            count += 2
        if s1[i] == c and s2[i] == c:
            cs12 -= 2
    print(count - cs12)
