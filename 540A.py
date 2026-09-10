n = int(input())
s1 = input()
s2 = input()

count = 0
for i in range(n):
    count += min(abs(int(s1[i])-int(s2[i])), (10-max(int(s2[i]), int(s1[i])) + min(int(s2[i]), int(s1[i]))))

print(count)
