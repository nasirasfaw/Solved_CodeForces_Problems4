t = int(input())
for _ in range(t):
    l1, l2, l3 = map(int, input().split())

    ln = [l1, l2, l3]
    ln.sort()

    if ((ln[0] + ln[1] == ln[2]) or (ln[0] == ln[1] and ln[2] % 2 == 0) 
        or (ln[1] == ln[2] and ln[0] % 2 == 0)):
        print("YES")
    else:
        print("NO")
