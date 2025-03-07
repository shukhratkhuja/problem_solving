k, n, w = map(int, input().split())

sum = 0

for i in range(1, w+1):
    sum += i * k

print(sum - n if sum - n > 0 else 0)