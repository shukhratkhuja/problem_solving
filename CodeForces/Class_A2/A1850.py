t = int(input())

for _ in range(t):
    ns = list(map(int, input().split()))
    ns.sort()
    if ns[1] + ns[2] >= 10:
        print("YES")
    else:
        print("NO")

