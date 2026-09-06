table = input()
hand = list(map(str, input().split()))

if any(table[0] in y or table[1] in y for y in hand):
    print("YES")
else:
    print("NO")
