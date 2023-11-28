def print_formatted(number):
    # your code goes here
    for i in range(1, number+1):
        l = len(str(bin(number)))-1
        print("{:{n}d}{:{l}o}{:{l}X}{:{l}b}".format(i, i, i, i, l=l, n=l-1))

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)