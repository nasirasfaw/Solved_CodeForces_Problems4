n = int(input())
s1 = []
for i in range(n):
    s = input()
    s1.append(s)
for i in range(n):
    if s1[i][:2] == "OO" or s1[i][3:] == "OO":
        print("YES")
        if s1[i][:2] == "OO":
            s1[i] = "++" + s1[i][2:]
        else:
            s1[i] = s1[i][:3] + "++"
        for j in range(n):
            print(s1[j])
        break
else:
    print("NO")
