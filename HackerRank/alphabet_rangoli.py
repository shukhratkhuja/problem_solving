
def print_rangoli(n):
    for row in range(0, 2*n-1):
        rs = ''
        for col in range(0, 4*n-3):
            if col % 2 ==  1:
                rs += "-"
            else:  
                if col == (2*n-1)+row*2 or col == (2*n-1)-row*2:
                    rs += chr(97+col)
                else:
                    rs += '-'
              
        print(rs)
    
if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)