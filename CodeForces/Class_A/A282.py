n = int(input())

result = 0
for _ in range(n):
    result += 1 if '+' in input() else -1

print(result)