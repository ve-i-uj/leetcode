"""412. Fizz Buzz

https://leetcode.com/problems/fizz-buzz/
"""

from typing import Optional, List, Any  # noqa: F401


class Solution:

    def process(self, *args, **kwargs):  # noqa: N802
        return self.fizzBuzz(*args, **kwargs)

    def fizzBuzz(self, n: int) -> List[str]:
        res = []
        for i in range(n):
            i += 1
            if i % 3 == 0 and i % 5 == 0:
                res.append('FizzBuzz')
            elif i % 3 == 0:
                res.append('Fizz')
            elif i % 5 == 0:
                res.append('Buzz')
            else:
                res.append(str(i))

        return res
