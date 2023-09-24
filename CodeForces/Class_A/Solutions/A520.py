n = int(input())
s = input()

if n < 26:
    print('NO')
else:
    s = s.lower()
    x = [l for l in s]
    if len(set(x)) < 26:
        print('NO')
    else:
        print('YES')