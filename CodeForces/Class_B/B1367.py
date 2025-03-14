def min_moves_to_good_array(n, arr):
    wrong_even = 0  # Even index has odd value
    wrong_odd = 0   # Odd index has even value

    for i in range(n):
        if i % 2 == 0 and arr[i] % 2 == 1:
            wrong_even += 1
        elif i % 2 == 1 and arr[i] % 2 == 0:
            wrong_odd += 1

    if wrong_even == wrong_odd:
        return wrong_even  # Minimum swaps needed
    else:
        return -1  # Impossible

# Reading input
t = int(input())  # Number of test cases
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    print(min_moves_to_good_array(n, arr))
