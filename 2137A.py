t = int(input())
for _ in range(t):
    k, x = map(int, input().split())

    print(2**k * x) 
    
    #We can choose only the even operation and reverse it!
    #The answer is not unique.
