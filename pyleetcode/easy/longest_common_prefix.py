"""14. Longest Common Prefix.

https://leetcode.com/problems/longest-common-prefix/
"""

import collections
from typing import List


class Solution:

    def longestCommonPrefix(self, strs: List[str]) -> str:  # noqa
        vocabulary: dict = collections.defaultdict(int)
        for word in strs:
            for i in range(len(word)):
                prefix = word[0:i+1]
                vocabulary[prefix] += 1

        prefs = sorted(vocabulary.items(), key=lambda p: (p[1], len(p[0])))
        last_prefix, cntr = prefs[-1]
        if cntr == 1:
            return ''

        return last_prefix

    def process(self, *args, **kwargs):
        return self.longestCommonPrefix(*args, **kwargs)
