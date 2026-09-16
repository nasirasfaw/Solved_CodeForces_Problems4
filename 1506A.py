t = int(input())
for _ in range(t):
    n, m, x = map(int, input().split())

    column = (x-1)//n      
    row = (x-1) % n       

    answer = row * m + column + 1

    print(answer)
