"""20. Valid Parentheses.

https://leetcode.com/problems/valid-parentheses/
"""


class Solution:

    def isValid(self, s: str) -> bool:  # noqa
        length = len(s)
        if length % 2 != 0:
            return False
        round_cntr = 0
        square_cntr = 0
        curly_cntr = 0
        for i, ch in enumerate(s):
            if ch == '(':
                round_cntr += 1
            elif ch == ')':
                round_cntr -= 1
            elif ch == '[':
                square_cntr += 1
            elif ch == ']':
                square_cntr -= 1
            elif ch == '{':
                curly_cntr += 1
            elif ch == '}':
                curly_cntr -= 1

            if round_cntr < 0 or square_cntr < 0 or curly_cntr < 0:
                return False

            if (length - i) < (round_cntr + square_cntr + curly_cntr):
                return False

        if sum([round_cntr, square_cntr, curly_cntr]) != 0:
            return False

        return True


def test():
    assert not Solution().isValid('(')
    assert not Solution().isValid('(()[][]')
    assert not Solution().isValid('(){[[[{}()'), \
        'Need stop on the 4th element by the end'
    assert not Solution().isValid('()}[]'), 'The third bracket is a closing bracket'

    assert Solution().isValid('()')
    assert Solution().isValid('()[]{}')
    assert not Solution().isValid('(]')
