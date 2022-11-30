"""22. Generate Parentheses

https://leetcode.com/problems/generate-parentheses/
"""

from typing import Optional, List, Any  # noqa: F401


class Solution:

    def process(self, *args, **kwargs):
        return self.generateParenthesis(*args, **kwargs)

    def generateParenthesis(self, n: int) -> List[str]:  # noqa: N802

        def _generate(ps: str, new_p: str, cntr: int, i: int) -> list[str]:
            if new_p == '(':
                cntr += 1
            else:
                cntr -= 1

            if cntr < 0 or (cntr >= 0 and cntr > (2 * n - i)):
                return []

            if i + 1 == 2 * n:
                return [ps + new_p]

            return _generate(ps + new_p, '(', cntr, i+1) \
                + _generate(ps + new_p, ')', cntr, i+1)

        return _generate('', '(', 0, 0)
