import textwrap

def wrap(string, max_width):
    strlist = list(string)
    c = 0
    for i in range(1,len(strlist)):
        if i % max_width == 0:
            strlist.insert(i+c, '\n') 
            c+=1
    return ''.join(strlist)


if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)