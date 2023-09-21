#Test cases
from math import ceil

t = int(input())

for test_case in range(t):
    # the number of Petya's apartment and the number of apartments on each floor of the house except the first one (there are two apartments on the first floor).
    n, x = map(int, input().split())
    if n == 1 or n == 2:
        print(1)
    else:
        f = ceil((n-2)/x)+1
        print(f)

