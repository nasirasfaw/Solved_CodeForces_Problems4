n = int(input())
 
v = list(map(int, input().split()))
 
# Original order
prefix1 = [0] * (n + 1)
 
for i in range(n):
    prefix1[i + 1] = prefix1[i] + v[i]
 
# Sorted order
u = sorted(v)
 
prefix2 = [0] * (n + 1)
 
for i in range(n):
    prefix2[i + 1] = prefix2[i] + u[i]
 
m = int(input())
 
for _ in range(m):
    typ, l, r = map(int, input().split())
 
    if typ == 1:
        print(prefix1[r] - prefix1[l - 1])
    else:
        print(prefix2[r] - prefix2[l - 1])
