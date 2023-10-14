# https://leetcode.com/problems/search-insert-position/

class Solution(object):
    def searchInsert(self, nums, target):

        l = 0
        r = len(nums) - 1

        while l <= r:
            mid = (l+r) // 2
            if nums[mid] > target:
                r = mid - 1
            elif nums[mid] < target:
                l = mid + 1
            else:
                return mid
        return l
        
        # my own solution
        # if target in nums:
        #     return nums.index(target)
        # else:
        #     for i in range(len(nums)):
        #         if nums[i] > target:
        #             return i
        #     else:
        #         return len(nums)
        
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        


# x = Solution().searchInsert(nums = [1,3,5,6], target = 5)
# x = Solution().searchInsert(nums = [1,3,5,6], target = 2)
x = Solution().searchInsert(nums = [1,3,5,6], target = 7)
print(x)
