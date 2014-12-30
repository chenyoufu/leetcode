__author__ = 'wuyuan'

"""
Given an integer n, return the number of trailing zeroes in n!
Note: Your solution should be in logarithmic time complexity.
"""

class Solution1:
    # @return an integer
    def trailingZeroes(self, n):
        ret = 1
        zero = 0
        for i in range(1, n+1):
            ret *= i
        while ret > 0 and ret % 10 == 0:
            ret //= 10
            zero += 1
        return zero


class Solution2:
    # @return an integer
    def trailingZeroes(self, n):
        zero = 0
        for i in range(5, n+1, 5):
            while i % 5 == 0:
                i //= 5
                zero += 1
        return zero


class Solution3:
    # @return an integer
    def trailingZeroes(self, n):
        zero = 0
        k = 0
        while (5 ** k) <= n:
            k += 1
        for i in range(1, k):
            zero += n // (5 ** i)
        return zero

num = 100
s1 = Solution1()
print(s1.trailingZeroes(num))

s2 = Solution2()
print(s2.trailingZeroes(num))

s3 = Solution3()
print(s3.trailingZeroes(num))