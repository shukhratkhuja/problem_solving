n = int(input())
answer = 0
for i in range(n):
    operation = input()
    if '++' in operation:
        answer += 1
    else:
        answer -= 1
print(answer) 