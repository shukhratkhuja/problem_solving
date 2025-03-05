from itertools import combinations, permutations
t = int(input())
def find_gcd(a, b):
    if a > b:
        return find_gcd(a-b, b)
    elif b > a:
        return find_gcd(b-a, a)
    else:
        return a 

def print_biggest_gcd(ll):
    l = [i+1 for i in range(x)]
    ll = list(combinations(l, 2))
    max_gcd = 0
    for i in ll:
        cur_gcd = find_gcd(*i)
        if max_gcd < cur_gcd:
            max_gcd = cur_gcd
    return max_gcd



for _ in range(t):
    x = int(input())
    print(print_biggest_gcd(x))
    
