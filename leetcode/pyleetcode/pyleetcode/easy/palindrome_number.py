"""9. Palindrome Number.

https://leetcode.com/problems/palindrome-number/
"""


class Solution:

    def isPalindrome(self, x: int) -> bool:  # noqa
        if x < 0 or (x != 0 and x % 10 == 0):
            return False
        invert = 0
        while x > invert:
            invert = invert * 10 + x % 10
            x //= 10

        return x == invert or x == invert // 10

