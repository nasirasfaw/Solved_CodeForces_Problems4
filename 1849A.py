t = int(input())
for _ in range(t):
    b, c, h = map(int, input().split())
    
    print(2*min(b-1, c+h) + 1)
