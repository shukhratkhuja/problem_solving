a = input()
b = input()
c = ''
for i in range(len(a)):
    c += str(int(a[i])^int(b[i]))

print(c)