t = int(input())
for _ in range(t):
    p = int(input())

    if p == 5:
        print(2, 4)
    elif p == 7:
        print(3, 6)
    else:
        print((p-3)//2, p-3)
