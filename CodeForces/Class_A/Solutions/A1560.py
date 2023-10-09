t = int(input())



for _ in range(t):
    limit = int(input())
    start_number = 1

    while limit != 1:
        start_number += 1
        if start_number % 3 != 0 and f'{start_number}'[-1] != '3':
            limit -= 1
    print(start_number)