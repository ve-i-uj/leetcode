"""13. Roman to Integer

https://leetcode.com/problems/roman-to-integer/
"""

class Solution:

    def romanToInt(self, s: str) -> int:
        dct: dict[str, int] = {k: v for k, v in [
            ('I', 1),
            ('V', 5),
            ('X', 10),
            ('L', 50),
            ('C', 100),
            ('D', 500),
            ('M', 1000),
        ]}
        res = 0
        for i in range(len(s) - 1):
            if dct[s[i]] < dct[s[i + 1]]:
                res -= dct[s[i]]
            else:
                res += dct[s[i]]
        res += dct[s[-1]]

        return res
