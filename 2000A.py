t = int(input())
for _ in range(t):
    a = int(input())

    a = str(a)
    a1 = a[:2]
    a2 = a[2:]
 
    if len(a) >= 3 and a1 == "10" and a[2] != "0" and int(a2) >= 2:
        print("YES")
    else:
        print("NO")
