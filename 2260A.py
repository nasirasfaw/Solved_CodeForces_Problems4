t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    
    if a.count(0) < 2:
        print(-1)
    else:
        if a[0] == 0 and a[n-1] == 0:
            print(0)
        elif a[0] == 0 or a[n-1] == 0:
            print(1)
        else:
            print(2)
