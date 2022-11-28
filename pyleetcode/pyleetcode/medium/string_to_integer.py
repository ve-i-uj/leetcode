"""8. String to Integer

https://leetcode.com/problems/string-to-integer/
"""

from typing import Optional, List, Any  # noqa: F401

MAX = 2 ** 31 - 1
MIN = -2 ** 31

INT_CHARS = set([str(i) for i in range(10)])
SING_CHARS = set(['+', '-'])


class Solution:

    def process(self, *args, **kwargs) -> int:
        return self.myAtoi(*args, **kwargs)

    def myAtoi(self, s: str) -> int:
        is_negative = False
        s = s.lstrip()
        if not s:
            return 0
        if s[0] in SING_CHARS:
            if s[0] == '+':
                is_negative = False
            else:
                is_negative = True
            s = s[1:]

        res = 0
        i = 0
        for i, ch_i in enumerate(s):
            if ch_i not in INT_CHARS:
                break

            i = int(ch_i)
            if not is_negative:
                if res > MAX // 10 or (res == MAX // 10 and i > MAX % 10):
                    return MAX
            else:
                if res > abs(MIN) // 10 or (res == abs(MIN) // 10
                                            and i > (abs(MIN) % 10)):
                    return MIN
            res = res * 10 + i

        return res * -1 if is_negative else res
