# https://leetcode.com/problems/fibonacci-number/description/

class Solution:
    def fib(self, n: int) -> int:
        if n == 0: return 0
        elif n == 1 or n == 2: return 1
        return self.fib(n-1) + self.fib(n-2)
        

x = Solution().fib(6)
# x = Solution().fib(4)
print(x)