"""9. Palindrome Number.

https://leetcode.com/problems/palindrome-number/
"""


class Solution:

    def isPalindrome(self, x: int) -> bool:  # noqa
        str_x = str(x)
        return str_x == str_x[::-1]


def test():
    assert Solution().isPalindrome(121)
    assert not Solution().isPalindrome(-121)
    assert not Solution().isPalindrome(10)
