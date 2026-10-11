n = int(input())
s = input()

n1, o1, e1 = s.count("n"), s.count("o"), s.count("e")
z1, r1 = s.count("z"), s.count("r")
ones = min(n1, o1, e1)
zeros = min(z1, e1-ones, r1, o1-ones)

answer = ["1"]*ones + ["0"]*zeros

print(*answer)
