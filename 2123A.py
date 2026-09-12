t = int(input())
for _ in range(t):
    n = int(input())

    if (n-1) % 4 == 3:
        print("Bob")
    else:
        print("Alice")
