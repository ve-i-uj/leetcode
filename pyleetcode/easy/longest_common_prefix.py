"""14. Longest Common Prefix.

https://leetcode.com/problems/longest-common-prefix/
"""

from typing import List


class Solution:

    def longestCommonPrefix(self, strs: List[str]) -> str:  # noqa
        if len(strs) == 1:
            return strs[0]

        last_index = 0
        for i, chars in enumerate(zip(*strs)):
            if len(set(chars)) == 1:
                # Letters are the same.
                continue

            last_index = i
            break

        return strs[0][:last_index]

    def process(self, *args, **kwargs):
        return self.longestCommonPrefix(*args, **kwargs)
