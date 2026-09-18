t = int(input())
for _ in range(t):
    a, b, c = map(int, input().split())

    if a > max(b, c):
        xa = 0
    else:
        xa = max(b, c) - a + 1
    if b > max(a, c):
        xb = 0
    else:
        xb = max(a, c) - b + 1
    if c > max(a, b):
        xc = 0
    else:
        xc = max(a, b) - c + 1

    print(xa, xb, xc)
