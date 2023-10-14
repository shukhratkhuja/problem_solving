# https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/

class Solution(object):
    def searchRange(self, nums, target):
        if target not in nums:
            return [-1, -1]
        else:
            start = nums.index(target)
            nums.reverse()
            end = len(nums) - nums.index(target) - 1
            return [start, end]
           
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        