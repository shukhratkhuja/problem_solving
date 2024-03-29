# https://leetcode.com/problems/valid-parentheses/

class Solution(object):
    def isValid(self, s):
        d = {
            "}": "{", 
            "]": "[", 
            ")": "(", 
        }

        left = []

        for p in s:
            try:
                if p in "({[":
                    left.append(p)
                elif left[-1] == d[p]:
                        del left[-1]
                else: return False
            except: return False

        if left:
            return False
        return True


        # second solution
        # l = []
        # for p in s:
        #     try:
        #         if p in d.values():
        #             l.append(p)
        #         elif l[-1] == d[p]:
        #                 del l[-1]
        #         else:
        #             return False
        #     except: return False

        # if not l:
        #     return True
        # return False


x = Solution().isValid("([)]")
print(x)