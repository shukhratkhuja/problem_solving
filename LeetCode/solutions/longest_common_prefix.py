# https://leetcode.com/problems/longest-common-prefix/

class Solution(object):
    def longestCommonPrefix(self, strs):
        min_lenw = strs[0]
        for w in strs:
            if len(w) < len(min_lenw):
                min_lenw = w
        x = 0
        while True:
            x+=1
            if x == 10:
                break
            for w in strs:
                if min_lenw != w[:len(min_lenw)]:
                    min_lenw = min_lenw[:-1:1  ]
                    break
            else:
                return min_lenw
            
x = Solution().longestCommonPrefix(strs=["flower","flow","flight", "car"])
print(x)