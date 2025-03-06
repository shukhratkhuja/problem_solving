n = int(input())

result = 0
for _ in range(n):

    answers = map(int, input().split())
    result += 1 if sum(answers) > 1 else 0

print(result)