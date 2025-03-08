n = int(input())

max_cap = -1
cap = 0

for i in range(n):
    m, p = map(int, input().split())
    cap += p - m
    if cap > max_cap:
        max_cap = cap

print(max_cap)