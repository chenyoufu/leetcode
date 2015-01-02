__author__ = 'wuyuan'
"""
Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.
For example,
"A man, a plan, a canal: Panama" is a palindrome.
"race a car" is not a palindrome.

Note:
Have you consider that the string might be empty? This is a good question to ask during an interview.
For the purpose of this problem, we define empty string as valid palindrome.
"""

class Solution:
    # @param s, a string
    # @return a boolean
    def isPalindrome(self, s):
        if len(s) == 0:
            return True
        else:
            j = len(s) - 1
        i = 0
        while i < j:
            if s[i].lower() != s[j].lower():
                if s[i].isalnum() and s[j].isalnum():
                    return False
                if not s[i].isalnum():
                    i += 1
                if not s[j].isalnum():
                    j -= 1
            else:
                i += 1
                j -= 1
        if s[i].lower() == s[j].lower() or not s[i].isalnum() or not s[j].isalnum():
            return True
        else:
            return False

s = Solution()
s1 = "A man, a plan, a canal: Panama"
s2 = "race a car"
s3 = "aa"
s4 = ""
s5 = "ab           ba"
s6 = "ab         ca"
s7 = "ab a"
s8 = "aA"
s9 = ".,"
print(s.isPalindrome(s1))
print(s.isPalindrome(s2))
print(s.isPalindrome(s3))
print(s.isPalindrome(s4))
print(s.isPalindrome(s5))
print(s.isPalindrome(s6))
print(s.isPalindrome(s7))
print(s.isPalindrome(s8))
print(s.isPalindrome(s9))