t = int(input())
for _ in range(t):
    a, b = map(int, input().split())

    if b == 0:
        answer = a+1
    elif a == 0:
        answer = 1
    else:
        answer = a + 2*b + 1

    print(answer)
