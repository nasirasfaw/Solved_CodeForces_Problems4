n = int(input())
a = list(map(int, input().split()))

a1 = []
for i in range(n):
    if a[i] not in a[i+1:]:
        a1.append(a[i])
        
print(len(a1))
print(*a1)
