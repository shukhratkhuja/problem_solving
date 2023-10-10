x,y = map(int, input().split())

if x > y:
    z = x
else:
    z = y

if z == 1:
    print('1/1')
elif z == 2:
    print('5/6')
elif z == 3:
    print('2/3')
elif z == 4:
    print('1/2')
elif z == 5:
    print('1/3')
elif z == 6:
    print('1/6')
