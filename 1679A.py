t = int(input())
for _ in range(t):
    n = int(input())

    if n == 2 or n % 2 != 0:
        print(-1)
    elif n % 6 == 0 and n % 4 == 0:
        print(n//6, n//4)
    elif n % 6 == 0:
        print(n//6, (n-6)//4 + 1)
    elif n % 4 == 0:
        if n % 6 == 2:
            print((n-8)//6 + 2, n//4)
        else:
            print((n-4)//6 + 1, n//4)
    elif n % 4 == 2:
        print((n-8)//6 + 2, (n-6)//4 + 1)
