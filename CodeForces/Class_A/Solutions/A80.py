n = int(input())
m = int(input())
def is_prime(n):
    for i in range(2,n//2+1):
        if n % i == 0:
            return False
    else: return True
print(is_prime(n))

for i in range(n, m+1):
    if is_prime(i):
        pass
