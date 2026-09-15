import string
t = int(input())
for _ in range(t):
    n = int(input())

    s = list(string.ascii_lowercase)

    if n <= 26:
        s1, s2, s3 = 1, 1, n-2
    elif n == 27:
        s1, s2, s3 = 1, 1, 25
    elif n <= 53:
        s1, s2, s3 = 1, (n-27), 26
    elif n <= 77:
        s1, s2, s3 = n%26, (n - (n%26))//2, (n - (n%26))//2
    else:
        s1 = s2 = s3 = 26
    w = [s[s1-1], s[s2-1], s[s3-1]]
    print("".join(w))
