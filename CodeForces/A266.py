n = int(input())
s = input()
result = 0
for i in range(1, n):
    if s[i-1] == s[i]:
        result += 1

print(result)