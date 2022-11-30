"""22. Generate Parentheses

https://leetcode.com/problems/generate-parentheses/
"""

import itertools
from typing import Optional, List, Any  # noqa: F401


class Solution:

    def process(self, *args, **kwargs):  # noqa: N802
        return self.generateParenthesis(*args, **kwargs)

    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        for ps in itertools.permutations('(' * n + ')' * n, n * 2):
            cntr = 0
            for i, p in enumerate(ps, 1):
                if cntr > len(ps) // 2:
                    break
                if p == '(':
                    cntr += 1
                else:
                    cntr -= 1

                if cntr < 0:
                    break
            else:
                res.append(''.join(ps))

        return list(set(res))

        return []
