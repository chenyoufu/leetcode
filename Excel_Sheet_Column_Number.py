__author__ = 'wuyuan'
"""
Related to question Excel Sheet Column Title.
Given a column title as appear in an Excel sheet, return its corresponding column number.
For example:
    A -> 1
    B -> 2
    C -> 3
    ...
    Z -> 26
    AA -> 27
    AB -> 28
"""
class Solution:
    # @param s, a string
    # @return an integer
    def titleToNumber(self, s):
        length = len(s)
        num = 0
        j = 0
        for i in range(length-1, -1, -1):
            num += (ord(s[i])-64) * (26 ** j)
            j += 1
        return num

s = Solution()
print(s.titleToNumber('AB'))