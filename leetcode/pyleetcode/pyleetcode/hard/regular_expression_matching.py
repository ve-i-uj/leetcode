"""10. Regular Expression Matching

https://leetcode.com/problems/regular-expression-matching/
"""

import re


class Solution:

    def isMatch(self, s: str, p: str) -> bool:
        m = re.match('^' + p + '$', s)
        if m is None:
            return False
        return True
