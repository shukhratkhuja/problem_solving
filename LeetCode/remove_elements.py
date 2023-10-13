# https://leetcode.com/problems/remove-element/

class Solution(object):
    def removeElement(self, nums, val):
        k = 0
        for i in range(len(nums)):
            if nums[i-k] == val:
                del nums[i-k]
                k += 1
                nums.append('_')
        return len(nums) - k
    
x = Solution().removeElement(nums=[0,1,2,2,3,0,4,2], val=2)
print(x)