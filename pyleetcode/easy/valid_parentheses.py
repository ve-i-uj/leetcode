"""20. Valid Parentheses.

https://leetcode.com/problems/valid-parentheses/
"""

from dataclasses import dataclass, fields


@dataclass
class Counter:
    round: int
    square: int
    curly: int

    def is_valid(self):
        return sum(getattr(self, f.name) for f in fields(self)) <= 1

    def is_valid_after_stop(self):
        return not any(getattr(self, f.name) != 0 for f in fields(self))


class Solution:

    def isValid(self, s: str) -> bool:  # noqa
        length = len(s)
        if length % 2 != 0:
            return False
        counter = Counter(0, 0, 0)
        for ch in s:
            if ch == '(':
                counter.round += 1
            elif ch == ')':
                counter.round -= 1
            elif ch == '[':
                counter.square += 1
            elif ch == ']':
                counter.square -= 1
            elif ch == '{':
                counter.curly += 1
            elif ch == '}':
                counter.curly -= 1

            if not counter.is_valid():
                return False

        if not counter.is_valid_after_stop():
            return False

        return True


def test():
    # my tests
    assert not Solution().isValid('(')
    assert not Solution().isValid('(()[][]')
    assert not Solution().isValid('(){[[[{}()'), \
        'Need stop on the 4th element by the end'
    assert not Solution().isValid('()}[]'), 'The third bracket is a closing bracket'
    # task tests
    assert Solution().isValid('()')
    assert Solution().isValid('()[]{}')
    assert not Solution().isValid('(]')
    # check task test
    assert not Solution().isValid('([)]')
