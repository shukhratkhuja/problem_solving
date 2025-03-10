screens = list(map(int, input().split()))
touches = input()
result = 0
for touch in touches:
    result += screens[int(touch)-1]
print(result)