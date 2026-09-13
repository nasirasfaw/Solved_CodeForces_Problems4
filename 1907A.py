t = int(input())
for _ in range(t):
    p = input()

    x = "abcdefgh"
    y = "87654321"
    k, h = x.index(p[0]), y.index(p[1])
    
    xd = [x[k]+y[j] for j in range(8) if j != h]

    yd = [x[i]+y[h] for i in range(8) if i != k]

    xyd = xd + yd 
    
    for r in xyd:
        print(r)
