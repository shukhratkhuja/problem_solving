
def print_rangoli(n):
    for row in range(n):

        rs = ''
        counter = 0
        for col in range(2*n-2):
            if col == 2*n-1:
                rs += chr(97+row)
            
            # if col % 2 == 0:
            #     if col == 2*n-1:
            #         rs += chr(97+(n-row-1))
            # # print(f"[{row}, {col}]", end=' ')
            # if col == (2*n-1)+row*2-1 or col == (2*n-1)-row*2-1:
            #     rs += chr(97+(n-row-1))
            # else:  
            #     rs += '-'
              
        print(rs)
    
if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)