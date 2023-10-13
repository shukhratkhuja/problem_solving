# https://leetcode.com/problems/remove-duplicates-from-sorted-array/

class Solution(object):
    def removeDuplicates(self, nums):
        l = list(set(nums))
        llen = len(nums)
        nums[:] = []
        nums.extend(l)
        nums.sort()
        nums.extend('_' for _ in range(len(l), llen))
        return len(l)
        

        """
        :type nums: List[int]
        :rtype: int
        """
    
# x = Solution().removeDuplicates([0,0,1,1,1,2,2,2,3,3,4])
x = Solution().removeDuplicates([1,1,2])
print(x)