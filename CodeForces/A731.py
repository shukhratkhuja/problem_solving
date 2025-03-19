import sys

result = 0
word = sys.stdin.readline().strip()

a = 0
alphabet = 'abcdefghijklmnopqrstuvwxyz'

for c in word:
    b = alphabet.index(c)
    if a < b:
        result += min(abs(b-a), a + abs(26-b))
    else:
        result += min(abs(b-a), b + abs(26-a))
    a = b

sys.stdout.write(str(result) + "\n")
