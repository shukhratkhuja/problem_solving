stations = int(input())
m = 0
p = 0
for i in range(stations):
    c ,t = map(int, input().split())
    p = p - c + t
    if p > m:
        m = p
print(m)