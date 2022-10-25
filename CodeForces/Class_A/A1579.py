# Number of test cases
t = int(input())

for i in range(t):
    letters = str(input())
    a = letters.count('A')
    b = letters.count('B')
    c = letters.count('C')

    if a + c == b:
        print("YES")
    else:
        print("NO")