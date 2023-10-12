# https://leetcode.com/problems/roman-to-integer/

class Solution(object):
    def romanToInt(self, s):
        dr = {"I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        nl = [dr[l] for l in s]
        if nl == sorted(nl):
            return sum(nl)
        else:
            dn = {}
            dn[s[0]] = 0
            for i in range(1, len(s)):
                if s[i] not in dn.keys():
                    dn[s[i]] = 0

                dn[s[i-1]] += 1

                if dr[s[i]] > dr[s[i-1]]:
                    dn[s[i-1]] *= (-1)
            else:
                dn[s[-1]] += 1

            result = 0
            for k, v in dn.items():
                result += dr[k] * v

            return result


x = Solution().romanToInt('MLCXXLVIII')
print(x)
"""
:type s: str
:rtype: int
"""