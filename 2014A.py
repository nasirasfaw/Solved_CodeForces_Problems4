t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))

    gold = 0
    give = 0
    for i in range(n):
        if a[i] >= k:
            gold += a[i]
        if a[i] == 0 and gold >= 1:
            gold -= 1
            give += 1

    print(give)
