t = int(input())
for _ in range(t):
    n = int(input())
    
    if n % 3 == 0:
        first = n//3 + 1
        second = n//3
        third = n//3 - 1
    elif n % 3 == 1:
        first = n//3 + 2
        second = n//3
        third = n//3 - 1
    else:
        first = n//3 + 2
        second = n//3 + 1
        third = n//3 - 1

    print(second, first, third)
