"""36. Valid Sudoku

https://leetcode.com/problems/valid-sudoku/
"""

from typing import List


class Solution:

    def process(self, *args, **kwargs):  # noqa: N802
        return self.isValidSudoku(*args, **kwargs)

    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = set()
        columns = set()
        boxes = set()
        for r_i, row in enumerate(board):
            for c_i, value in enumerate(row):
                if value == '.':
                    continue

                r_v = ('r', r_i, value)
                if r_v in rows:
                    return False
                rows.add(r_v)

                c_v = ('c', c_i, value)
                if c_v in columns:
                    return False
                columns.add(c_v)

                b_v = ('b', r_i // 3, c_i // 3, value)
                if b_v in boxes:
                    return False
                boxes.add(b_v)

        return True
