"""168. Excel Sheet Column Title

https://leetcode.com/problems/excel-sheet-column-title/
"""

import string


class Solution:

    def process(self, *args, **kwargs):
        return self.convertToTitle(*args)

    def convertToTitle(self, columnNumber: int) -> str:
        res = ""
        title_map = {i: s for i, s in zip(range(0, 26), string.ascii_uppercase)}

        while columnNumber > 0:
            columnNumber -= 1
            columnNumber, remainder = divmod(columnNumber, 26)

            res = title_map[remainder] + res

        return res
