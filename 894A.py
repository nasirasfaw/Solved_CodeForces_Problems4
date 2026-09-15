s = input()
count = 0
i = 1
while i < len(s):
    if s[i-1] == "A":
        count += s[:i-1].count("Q") * s[i:].count("Q")
    i += 1
    
print(count)
