t = int(input())
for _ in range(t):
    n = int(input())

    x = 0
    i = 1
    while abs(x) < n:
        if i % 2 == 1:
            x -= 2*i - 1
        else:
            x += 2*i -1
        i += 1
    if x < 0:
        print("Kosuke")
    else:
        print("Sakurako")
