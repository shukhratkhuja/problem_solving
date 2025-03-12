t = int(input())

def even_array(n, array):
    array_copy = array.copy()
    for i in range(n):
        for j in range(n):
            if i % 2 == 0 and array_copy[i] % 2 == 0 or i % 2 == 0 and array_copy[i] % 2 == 0:
                pass
            else:
                if i != n:
                    array_copy[i], array_copy[i+1] = array_copy[i+1], array_copy[i]


for _ in range(t):
    ...