# https://leetcode.com/problems/add-binary

class Solution(object):
    def addBinary(self, a: str, b: str) -> str:
    
        s = []
        carry = 0
        i = len(a) - 1
        j = len(b) - 1

        while i >= 0 or j >= 0 or carry:
            if i >= 0:
                carry += int(a[i])
                i -= 1
            if j >= 0:
                carry += int(b[j])
                j -= 1
            print(s)
            s.append(str(carry % 2))
            carry //= 2
            print(s)
            print("#"*100)

        return ''.join(reversed(s))

    # my solution
    # def decToBin(self, dec_number):
    #     bin_number = ''
    #     q = 0
    #     while dec_number != 0:
    #         q = dec_number % 2
    #         dec_number = dec_number // 2
    #         bin_number = str(q) + bin_number

    #     return bin_number

    # def binToDec(self, bin_number_str):
        
    #     dec_number = 0
    #     for i, v in enumerate(bin_number_str):
    #         dec_number += int(v) * 2 ** (len(bin_number_str)-i-1)
    #     return dec_number
    
    # def addBinary(self, a, b):
    #     ad = self.binToDec(a)
    #     bd = self.binToDec(b)
    #     result = self.decToBin(ad+bd)
    #     return  result if result else "0" 
        


        return

        """
        :type a: str
        :type b: str
        :rtype: str
        """
    
x = Solution().addBinary(a = "11", b = "1")
# x = Solution().addBinary(a = "1010", b = "1011")
print(x)