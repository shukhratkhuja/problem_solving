n, m = map(int, input().split())

def is_prime(n):
    for i in range(2,int(n**(1/2)+1)):
        if n % i == 0:
            return False
    else: return True

result = -1
for i in range(n+1, m+1):
    if i % 2 ==1 and is_prime(i):
        result = i
        break

if result == m:
    print("YES")
else:
    print("NO")

        
