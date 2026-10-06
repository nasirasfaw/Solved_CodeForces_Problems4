t = int(input())
for _ in range(t):
    s = input()

    k = len(s)
    s1 = "Yes"+"Yes"*(k//3 + 1)

    if s in s1:
        print("YES")
    else:
        print("NO")
