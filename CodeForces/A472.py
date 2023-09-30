n = int(input())


def isPrime(number):
    for i in range(2, int(number**(1/2))+1):
        if number % i == 0 and number // i > 1:
            return True
    return False

def main(n):
    for i in range(4, n):
        if isPrime(i) and isPrime(n-i):
            return i, n-i

print(*main(n))


