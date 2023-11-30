
def print_rangoli(n):

    ll = []
    for row in range(n):
        central_char_index = 97+n-row-1
        chrlist = [chr(central_char_index)]
        for i in range(1,row+1):
            chrlist.append(chr(central_char_index+i))
            chrlist.insert(0, chr(central_char_index+i))
            
        if row == n-1:
            ll.extend(reversed(ll))
            ll.insert(len(ll)//2, f"{'-'.join(chrlist)}".center(4*n-3, '-'))    
        else:
            ll.append(f"{'-'.join(chrlist)}".center(4*n-3, '-'))    
    print('\n'.join(ll))


# if __name__ == '__main__':
#     n = int(input())
#     print_rangoli(n)