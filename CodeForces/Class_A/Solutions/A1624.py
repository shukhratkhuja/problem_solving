t = int(input())

for _ in range(t):
    n = int(input())
    l = list(map(int, input().split()))
    print(max(l)-min(l))
