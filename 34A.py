n = int(input())
a = list(map(int, input().split()))

a1 = []
a2 = []
for i in range(n):
    a1.append(abs(a[i]-a[i-1]))
    a2.append([i, i+1])
a2[0] = [n, 1]

m = min(a1)

print(*a2[a1.index(m)])
