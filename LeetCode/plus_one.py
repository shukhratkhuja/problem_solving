# https://leetcode.com/problems/plus-one/

class Solution(object):
    def plusOne(self, digits):
        number = 0
        len_digit = len(digits)
        for i in range(len_digit):
            number += digits[len_digit-1-i]*10**i
        
        number += 1
        
        new_digits = []

        for d in str(number):
            new_digits.append(int(d))

        return new_digits


        
        
        """
        :type digits: List[int]
        :rtype: List[int]
        """

test1 = Solution().plusOne(digits = [1,2,3])
test2 = Solution().plusOne(digits = [4,3,2,1])
test3 = Solution().plusOne(digits = [9])
test4 = Solution().plusOne(digits = [1,0,0,0,0])


print(test1)
print(test2)
print(test3)
print(test4)

