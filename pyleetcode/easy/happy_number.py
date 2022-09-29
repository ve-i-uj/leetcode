"""202. Happy Number

https://leetcode.com/problems/happy-number/
"""

import math
import sys
from typing import Optional, List, Any  # noqa: F401


class Solution:

    def process(self, *args, **kwargs):  # noqa: N802
        return self.isHappy(*args, **kwargs)

    def isHappy(self, n: int) -> bool:
        if n == 1:
            return True

        get_new_n = lambda v: sum(int(i) ** 2 for i in str(v))

        slow = get_new_n(n)
        fast = get_new_n(get_new_n(n))
        if slow == 1 or fast == 1:
            return True

        while slow != fast:
            slow = get_new_n(slow)
            fast = get_new_n(get_new_n(fast))

            if slow == 1 or fast == 1:
                return True

        # The cycle detected
        return False
