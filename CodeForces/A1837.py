t = int(input())

valid = {'abc', 'cba', 'bac', 'acb'}
for _ in range(t):
    cards = input()
    if cards in valid:
        print("YES")
    else:
        print("NO")
