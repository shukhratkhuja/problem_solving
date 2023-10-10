t = int(input())

for _ in range(t):
    n = int(input())
    
    x = (int(str(n)[0])-1) * 10
    x += len(str(n))*(len(str(n))+1)/2
    
    print(int(x))
