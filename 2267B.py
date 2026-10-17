t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    m = max(a)
    freq = [0]*(m+1)

    for x in a:
        freq[x] += 1
    mf = max(freq)
    answer = []
    for i in range(1, mf+1):
        for x in range(m, 0, -1):
            if freq[x] >= i:
                answer.append(x)

    print(*answer)
