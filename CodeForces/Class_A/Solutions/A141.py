word1 = input()
word2 = input()
word3 = input()

l1 = [l for l in word1+word2]
l2 = [l for l in word3]

if sorted(l1) == sorted(l2):
    print('YES')
else:
    print('NO')