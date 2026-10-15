k2, k3, k5, k6 = map(int, input().split())

x = min(k2, k5, k6) 
y = min(k3, k2-x)

print(x * 256 + y * 32)
