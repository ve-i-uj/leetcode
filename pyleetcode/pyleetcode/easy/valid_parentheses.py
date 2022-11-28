"""20. Valid Parentheses.

https://leetcode.com/problems/valid-parentheses/
"""

import enum


class PEnum(enum.Enum):
    ROUND_O = '('
    ROUND_C = ')'
    SQUARE_O = '['
    SQUARE_C = ']'
    CURLY_O = '{'
    CURLY_C = '}'


PARENTHESES_O_BY_C = {
    PEnum.ROUND_C: PEnum.ROUND_O,
    PEnum.SQUARE_C: PEnum.SQUARE_O,
    PEnum.CURLY_C: PEnum.CURLY_O,
}
OPEN_PARENTHESES = set(PARENTHESES_O_BY_C.values())
CLOSE_PARENTHESES = set(PARENTHESES_O_BY_C.keys())


class Stack:

    def __init__(self) -> None:
        self._stack: list = []

    @property
    def is_empty(self) -> bool:
        return bool(self._stack)

    @property
    def length(self) -> int:
        return len(self._stack)

    def consume(self, paren: PEnum) -> bool:
        if paren in OPEN_PARENTHESES:
            self._stack.append(paren)
            return True

        if paren in CLOSE_PARENTHESES:
            if not self._stack:
                return False
            last_open_p = self._stack.pop()
            if PARENTHESES_O_BY_C[paren] == last_open_p:
                return True
            return False

        return False


class Solution:

    def isValid(self, s: str) -> bool:  # noqa
        length = len(s)
        if length % 2 != 0:
            return False

        stack = Stack()

        for i, ch in enumerate(s):
            paren = PEnum(ch)
            if not stack.consume(paren) or stack.length > (length - i):
                return False
        return True


TEST_CASES = {
    '(': False,
    '(()[][]': False,
    '(){[[[{}()': False,
    '()}[]': False,
    '()': True,
    '()[]{}': True,
    '(]': False,
    '([)]': False,
    '{[]}': True,
    '){': False,
}


def test():
    for case in TEST_CASES:
        Solution().isValid(case)
