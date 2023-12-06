
def digital_root(n):
	
    return n % 9 or n and 9 

    # new_n = sum(list(map(int, list(str(n)))))
    # if n > 9:
    #     return digital_root(new_n)
    # return n

n = int(input())
print(digital_root(n))