t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    w = [input() for _ in range(n)]
    if len(w[0]) > m:
        print(0)
    else:
        count = 1
        total = len(w[0])
        for i in range(1, n):
            if total + len(w[i]) <= m:
                total += len(w[i])
                count += 1
            else:
                break
        print(count)
