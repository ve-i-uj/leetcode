"""36. Valid Sudoku

https://leetcode.com/problems/valid-sudoku/
"""

import collections
import itertools
from typing import Iterable, Optional, List, Any  # noqa: F401


class Solution:

    def process(self, *args, **kwargs):  # noqa: N802
        return self.isValidSudoku(*args, **kwargs)

    def check(self, ivalues) -> bool:
        filter_ = set()
        for v in ivalues:
            if v == '.':
                continue
            if v in filter_:
                return False
            filter_.add(v)
        return True

    def isValidSudoku(self, board: List[List[str]]) -> bool:
        values = list(itertools.chain.from_iterable(board))

        for row in board:
            if not self.check(row):
                return False

        for i in range(9):
            column = itertools.islice(values, i, None, 9)
            if not self.check(column):
                return False

        for i in range(3):
            for j in range(3):
                box_conner = i * 27 + 3 * j
                box = []
                for k in range(3):
                    start = box_conner + k * 9
                    end = start + 3
                    box.extend(values[start:end])

                if not self.check(box):
                    return False

        return True


        return False