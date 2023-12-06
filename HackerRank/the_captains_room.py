# Enter your code here. Read input from STDIN. Print output to STDOUT
"""
from collections import Counter
k = int(input())
people = list(map(int, input().split()))
ddict = dict(Counter(people))
result = next((key for key, value in ddict.items() if value == 1), None)

print(result)
"""

"""
k = int(input())
list_k = list(map(int, input().split()))

#Finding room of Captian
set_k = set(list_k)
captiansRoom = ((sum(set_k) * k ) - sum(list_k)) // (k - 1)
print(captiansRoom)

"""