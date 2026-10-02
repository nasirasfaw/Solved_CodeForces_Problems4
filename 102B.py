n = int(input())

count = 0
while n >= 0:
    if n >= 10:
        n1 = [int(d) for d in str(n)]
        n = sum(n1)
        count += 1
    else:
        break

print(count)
