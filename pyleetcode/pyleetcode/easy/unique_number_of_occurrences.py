"""1207. Unique Number of Occurrences

https://leetcode.com/problems/unique-number-of-occurrences/
"""

import collections
from typing import Optional, List, Any  # noqa: F401


class Solution:

    def process(self, *args, **kwargs):  # noqa: N802
        return self.uniqueOccurrences(*args, **kwargs)

    def uniqueOccurrences(self, arr: List[int]) -> bool:
        cntr = collections.Counter(arr)
        values = list(cntr.values())
        return len(values) == len(set(values))
