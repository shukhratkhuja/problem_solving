a, b = map(int, input().split())
years = 0
while True:
    years += 1
    a *= 3
    b *= 2
    if a > b:
        break

print(years)