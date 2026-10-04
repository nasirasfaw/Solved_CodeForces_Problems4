import math 
t = int(input())
for _ in range(t):
    n = int(input())

    sr = int(math.sqrt(n))
    cr = int(math.cbrt(n))
    scr = int(math.sqrt(math.cbrt(n)))

    print(sr + cr - scr)
