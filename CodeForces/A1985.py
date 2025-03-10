t = int(input())

for _ in range(t):
    a, b = input().split()
    print(f"{b[0]}{a[1:]} {a[0]}{b[1:]}")