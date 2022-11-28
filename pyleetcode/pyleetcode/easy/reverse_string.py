"""344. Reverse String

https://leetcode.com/problems/reverse-string/
"""

from typing import Optional, List, Any  # noqa: F401


class Solution:

    def process(self, *args, **kwargs):  # noqa: N802
        return self.reverseString(*args, **kwargs)

    def reverseString(self, s: List[str]) -> None:
        l_pos = 1
        r_pos = len(s)
        while l_pos <= r_pos:
            l_val = s[l_pos - 1]
            r_val = s[r_pos - 1]
            s[l_pos - 1] = r_val
            s[r_pos - 1] = l_val

            l_pos += 1
            r_pos -= 1
