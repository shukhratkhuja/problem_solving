if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    arr_set = set(arr)
    arr = sorted(list(arr_set))
    print(arr[-2])
    