s = input()
result = 0

for c in s:
    if c.isupper():
        result += 1
    else:
        result -= 1

print(s.upper() if result > 0 else s.lower())