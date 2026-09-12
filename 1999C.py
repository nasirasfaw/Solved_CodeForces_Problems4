t = int(input())
for _ in range(t):
    n, s, m = map(int, input().split())
    n1 = []
    for _ in range(n):
        l, r = map(int, input().split())
        n1.append([l, r])
        
    if n1[0][0] >= s or m - n1[n-1][1] >= s:
        print("YES")
    else:
        for i in range(1, n):
            if n1[i][0] - n1[i-1][1] >= s:
                print("YES")
                break
        else:
            print("NO")
