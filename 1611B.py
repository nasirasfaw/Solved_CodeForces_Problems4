t = int(input())
for _ in range(t):
    a, b = map(int, input().split())

    teams = min((a+b)//4, a, b)
    
    print(teams)
