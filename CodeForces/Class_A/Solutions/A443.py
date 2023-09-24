x = input()

x = x.replace('{', '')
x = x.replace('}', '')
if x == '':
    print(0)
else:
    x = set(x.split(', '))
    print(len(x))
