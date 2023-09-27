
def ddfunc(number):
    l = []
    while True:
        b = number // 10**(len(str(number))-1)
        l.append(b * 10 ** (len(str(number))-1))
        number %= 10**(len(str(number))-1)
        if number < 10:
            if number == 0:
                break 
            l.append(number)
            break
    
    print(len(l), end='\n')
    print(*l)


n = int(input())
for _ in range(n):
    d = int(input())
    ddfunc(d)