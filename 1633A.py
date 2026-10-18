t = int(input())
for _ in range(t):
    n = int(input())

    n1 = [int(d) for d in str(n)]

    if n1[-1]+7-(n % 7) >= 10:
        n1[-1] -= n % 7
    else:
        n1[-1] += 7-(n % 7)

    if n % 7 == 0:
        print(n)
    else:
        n1 = "".join([str(k) for k in n1])

        print(int(n1))
