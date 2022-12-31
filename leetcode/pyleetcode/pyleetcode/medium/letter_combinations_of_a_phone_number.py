"""17. Letter Combinations of a Phone Number

https://leetcode.com/problems/letter-combinations-of-a-phone-number/
"""

import itertools
from typing import Optional, List, Any  # noqa: F401


_letters_by_digit = {
    2: 'abc',
    3: 'def',
    4: 'ghi',
    5: 'jkl',
    6: 'mno',
    7: 'pqrs',
    8: 'tuv',
    9: 'wxyz',
}
LETTERS_BY_DIGIT = {k: list(v) for k, v in _letters_by_digit.items()}


class Solution:

    def process(self, *args, **kwargs):
        return self.letterCombinations(*args, **kwargs)

    def letterCombinations(self, digits: str) -> List[str]:   # noqa: N802
        if not digits:
            return []
        letters = [LETTERS_BY_DIGIT[int(d)] for d in digits]
        return [''.join(combo) for combo in itertools.product(*letters)]
