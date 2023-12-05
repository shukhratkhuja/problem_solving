def merge_the_tools(string, k):
    
    ll = []
    for i in range(len(string)//k):
        ll.append(string[i*k:i*k+k])
    
    for i, l in enumerate(ll):
        nl = []
        for c in l:
            if c not in nl:
                nl.append(c)
        print(''.join(nl))


    # your code goes here

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)