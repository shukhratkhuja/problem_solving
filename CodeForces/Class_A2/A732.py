k, r = map(int, input().split())

result = 0

while True:
    if  ((result + 1) * k) % 10 == 0 or ((result + 1) * k) % 10 == r:
        result += 1
        break
    result += 1

print(result)