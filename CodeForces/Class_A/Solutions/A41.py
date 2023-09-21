word = input()
translation = input()

if word[-1::-1] == translation:
    print('YES')
else:
    print('NO')