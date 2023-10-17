# https://leetcode.com/problems/length-of-last-word/

class Solution(object):
    def lengthOfLastWord(self, s):
        word_list = s.strip().split(' ')
        return word_list[-1].strip().__len__()
        
    
        """
        :type s: str
        :rtype: int
        """


test1 = Solution().lengthOfLastWord("Hello World")
test2 = Solution().lengthOfLastWord("   fly me   to   the moon  ")
test3 = Solution().lengthOfLastWord("luffy is still joyboy")

print(test1)
print(test2)
print(test3)
