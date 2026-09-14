t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    occupied = {a[0]}
    for i in range(1, n):
        if a[i]-1 not in occupied and a[i]+1 not in occupied:
            print("NO")
            break
        occupied.add(a[i])
    else:
        print("YES")
