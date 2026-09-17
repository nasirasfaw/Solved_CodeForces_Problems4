t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))

    a1 = []
    i = 0
    for j in range(1, n):
        if a[j] != a[j-1]:
            a1.append(a[i:j])
            i = j
    a1.append(a[i:])
    
    count = 0
    for i in range(len(a1)):
        if 0 in a1[i] and len(a1[i]) >= k:
            count += (len(a1[i]) + 1)//(k+1)

    print(count)
