"""36. Valid Sudoku

https://leetcode.com/problems/valid-sudoku/
"""

from typing import List


class Solution:

    def process(self, *args, **kwargs):  # noqa: N802
        return self.isValidSudoku(*args, **kwargs)

    def isValidSudoku(self, board: List[List[str]]) -> bool:
        entities = []
        for r_i, row in enumerate(board):
            for c_i, value in enumerate(row):
                if value == '.':
                    continue
                entities.append(('r', r_i, value))
                entities.append(('c', c_i, value))
                entities.append(('b', r_i // 3, c_i // 3, value))

        return len(entities) == len(set(entities))
