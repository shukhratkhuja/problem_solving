import threading
from datetime import datetime

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def prime_list(n, m, results, i):
    p_list = []
    for number in range(n, m+1):
        if is_prime(number):
            p_list.append(number)
    results[i] = p_list


def main(number_of_threds, number_limit=3_000_000):
    if number_limit % number_of_threds == 0:
        threads = [None] * number_of_threds
        results = [None] * number_of_threds

        nums = int(number_limit / number_of_threds)
        print(nums)
        for i in range(number_of_threds):
            threads[i] = threading.Thread(
                target=prime_list, args=(i*nums, (i+1)*nums, results, i))
            threads[i].start()

        for i in range(number_of_threds):
            threads[i].join()

        return results
    else:
        print('Input correct number of threads')


if __name__ == '__main__':

    number_limit = int(input("Number limit: "))
    number_of_threds = int(input("Number of threads: "))

    results = main(number_of_threds, number_limit)

    for index, th_result in enumerate(results):
        print(f"Thread {index}: ", len(th_result))

