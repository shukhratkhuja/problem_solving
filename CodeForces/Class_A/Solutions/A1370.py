import sys

def max_gcd(n):
    return n // 2

t = int(sys.stdin.readline().strip())  # Test holatlar sonini o‘qib olamiz
results = []
for _ in range(t):
    n = int(sys.stdin.readline().strip())  # Har bir test uchun n ni o‘qiymiz
    results.append(str(max_gcd(n)))

sys.stdout.write("\n".join(results) + "\n")  # Natijalarni chiqaramiz


# def max_gcd(n):
#     return n // 2

# t = int(input())  # Read number of test cases
# results = []
# for _ in range(t):
#     n = int(input())  # Read n for each test case
#     results.append(str(max_gcd(n)))
# print("\n".join(results) + "\n")  # Efficient output


# from itertools import combinations
# t = int(input())
# def find_gcd(a, b):
#     if a > b:
#         a -= b
#         return find_gcd(a, b)
#     elif b > a:
#         b -= a
#         return find_gcd(b, a)
#     else:
#         return a 

# def print_biggest_gcd(ll):
#     l = [i for i in range(1, x)]
#     ll = list(combinations(l, 2))
#     max_gcd = 0
#     for i in ll:
#         cur_gcd = find_gcd(*i)
#         if max_gcd < cur_gcd:
#             max_gcd = cur_gcd
#     return max_gcd


# for _ in range(t):
#     x = int(input())
#     print(print_biggest_gcd(x))
    