n = int(input())
result = 0
for _ in range(n):
    p, q = map(int, input().split())
    if q - p > 1:
        result += 1

print(result)