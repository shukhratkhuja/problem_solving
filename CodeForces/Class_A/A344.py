n = int(input())

result = 0
lp = ''
for _ in range(n):
    s = input()
    if lp != s:
        result += 1
        lp = s

print(result)