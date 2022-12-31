"""13. Roman to Integer.

https://leetcode.com/problems/roman-to-integer/
"""

INT_BY_ROME = {
    'I': 1,
    'IV': 4,
    'V': 5,
    'IX': 9,
    'X': 10,
    'XL': 40,
    'L': 50,
    'XC': 90,
    'C': 100,
    'CD': 400,
    'D': 500,
    'CM': 900,
    'M': 1000,
}


class Solution:

    def romanToInt(self, s: str) -> int:  # noqa
        ret = 0
        next_ = 0
        for i, ch in enumerate(s):
            if i < next_:
                continue
            pair = s[i:i+2]
            if (digit := INT_BY_ROME.get(pair)) is not None:
                next_ = i + 2
                ret += digit
                continue
            digit = INT_BY_ROME.get(ch)
            if digit is None:
                raise SystemExit
            ret += digit
        return ret


def test():
    assert Solution().romanToInt('III') == 3
    assert Solution().romanToInt('LVIII') == 58
    assert Solution().romanToInt('MCMXCIV') == 1994
