# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import permutations

word, n = input().split()

plist = permutations(word, int(n))
plist = list(map(''.join, plist))
plist.sort()
for l in plist:
    print(l)