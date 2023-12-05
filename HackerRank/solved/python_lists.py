if __name__ == '__main__':
    N = int(input())
    
    numbers = []
    for i in range(N):
        command, *number = input().split()
        number = list(map(int, number))
        if command == 'insert':
            numbers.insert(number[0],number[1])
        elif command == 'print':
            print(numbers)
        elif command == 'remove':
            numbers.remove(number[0])
        elif command == 'append':
            numbers.append(number[0])
        elif command == 'sort':
            numbers.sort()
        elif command == 'pop':
            numbers.pop()
        elif command == 'reverse':
            numbers.reverse()


"""
12
insert 0 5
insert 1 10
insert 0 6
print
remove 6
append 9
append 1
sort
print
pop
reverse
print

"""