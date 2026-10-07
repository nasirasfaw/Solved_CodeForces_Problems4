t = int(input())
for _ in range(t):
    s = int(input())

    s1 = []
    for i in range(10):
        s1.append(9-i)
        if sum(s1) > s:
            s1[len(s1)-1] = s - sum(s1[:len(s1)-1])
            break
    s1 = s1[::-1]
    s1 = [str(x) for x in s1]
    s1 = "".join(s1)
    print(int(s1))
