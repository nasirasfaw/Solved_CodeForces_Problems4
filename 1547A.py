def read_pair():
    while True:
        line = input().strip()
        if line:
            return map(int, line.split())
        
t = int(input())
for _ in range(t):
    xa, ya = read_pair()
    xb, yb = read_pair()
    xf, yf = read_pair()

    d = abs(xa - xb) + abs(ya - yb)

    if (ya == yb == yf and min(xa, xb) < xf < max(xa, xb) or
        xa == xb == xf and min(ya, yb) < yf < max(ya, yb)):
        print(d + 2)
    else:
        print(d)
