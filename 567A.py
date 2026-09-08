n = int(input())
x = list(map(int, input().split()))

min0, max0 = x[1]-x[0], x[n-1]-x[0]
minn, maxn = x[n-1]-x[n-2], x[n-1]-x[0]
answer1 = [min0]
answer2 = [max0]
for i in range(1, n-1):
    mini = min(x[i]-x[i-1], x[i+1]-x[i])
    maxi = max(x[i]-x[0], x[n-1]-x[i])
    answer1.append(mini)
    answer2.append(maxi)
answer1.append(minn)
answer2.append(maxn)

for i in range(n):
    print(answer1[i], answer2[i])
