# Enter your code here. Read input from STDIN. Print output to STDOUT

from collections import deque

def solve(dq: deque):
    
    top = float('inf')  
    
    while dq:
        lm = dq[0]
        rm = dq[-1]
        if rm >= lm and rm <= top:
            top = dq.pop()
        elif lm >= rm and lm <= top:
            top = dq.popleft()
        else:
            break

    if not dq:
        return "Yes"
    return "No"

t = int(input())

for _ in range(t):
    n = int(input())
    dq = deque(map(int, input().split()))

    print(solve(dq))












"""def can_stack_cubes(test_cases):
    results = []
    
    for cubes in test_cases:
        n = cubes[0]
        side_lengths = cubes[1]
        
        left_index = 0
        right_index = n - 1
        top_cube = float('inf')  # Set an initial value for the top cube
        
        while left_index <= right_index:
            left_cube = side_lengths[left_index]
            right_cube = side_lengths[right_index]
            
            # Choose the larger cube from the left or right
            if left_cube >= right_cube and left_cube <= top_cube:
                top_cube = left_cube
                left_index += 1
            elif right_cube >= left_cube and right_cube <= top_cube:
                top_cube = right_cube
                right_index -= 1
            else:
                # If neither cube can be placed on top, break the loop
                break
        
        # Check if all cubes are placed on the pile
        if left_index > right_index:
            results.append("Yes")
        else:
            results.append("No")
    
    return results

# Input parsing
def parse_input():
    T = int(input())  # Number of test cases
    test_cases = []

    for _ in range(T):
        n = int(input())  # Number of cubes
        side_lengths = list(map(int, input().split()))
        test_cases.append((n, side_lengths))

    return test_cases

# Main function
if __name__ == "__main__":
    test_cases = parse_input()
    results = can_stack_cubes(test_cases)

    # Output the results
    for result in results:
        print(result)
"""


    


"""
STDIN        
-----        
2            
6            
4 3 2 1 3 4  
3            
1 3 2   

Function
--------
T = 2
blocks[] size n = 6
blocks = [4, 3, 2, 1, 3, 4]
blocks[] size n = 3
blocks = [1, 3, 2]    
"""