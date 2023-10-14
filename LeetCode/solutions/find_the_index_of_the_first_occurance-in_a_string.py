class Solution(object):
    def strStr(self, haystack:str, needle):

        if needle in haystack:
            return haystack.find(needle)
        else:
            return -1


        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """


x = Solution().strStr(haystack='leetcode', needle='leeto')
# x = Solution().strStr(haystack='sadbutsad', needle='sad')
print(x)