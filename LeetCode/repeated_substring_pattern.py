# https://leetcode.com/problems/repeated-substring-pattern/description/

class Solution(object):
    def repeatedSubstringPattern(self, s):
        r = ""
        
        for i in range(2, len(s)):
            r = s.replace(s[:i], "")
            if r == "":
                break
        else:
            return False
        
        return True

        
        
        """
        :type s: str
        :rtype: bool
        """
        