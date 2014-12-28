__author__ = 'wuyuan'

"""
Given a positive integer, return its corresponding column title as appear in an Excel sheet.
    1 -> A
    2 -> B
    3 -> C
    ...
    26 -> Z
    27 -> AA
    28 -> AB
"""
class Solution:
    # @return a string
    def convertToTitle(self, num):
        title = []
        if num > 0:
            while True:
                x = num % 26
                num //= 26
                if x == 0:
                    x = 26
                    num -= 1
                title.append(chr(x+64))
                if num == 0:
                    title.reverse()
                    return ''.join(title)
        else:
            return None

s = Solution()
print(s.convertToTitle(28))
