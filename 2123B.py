t = int(input())
for _ in range(t):
    n, j, k = map(int, input().split())
    a = list(map(int, input().split()))
    
    if k > 1 or (k == 1 and a[j-1] == max(a)):
        print("YES") 
    else:
        print("NO")
