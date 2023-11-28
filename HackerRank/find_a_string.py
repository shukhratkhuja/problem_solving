def count_substring(string, sub_string):
    counter = 0
    lss = len(sub_string)
    for i in range(len(string)-lss+1):
        print(string[i:i+lss])
        if sub_string == string[i:i+lss]:
            counter += 1
    return counter
    


if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)