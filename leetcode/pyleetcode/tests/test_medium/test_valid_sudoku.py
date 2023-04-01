'''Unit tests of '36. Valid Sudoku'.

https://leetcode.com/problems/valid-sudoku/
'''

import pytest

from pyleetcode.medium.valid_sudoku import Solution

TEST_CASES = [
    ([['5', '3', '.', '.', '7', '.', '.', '.', '.'],
      ['6', '.', '.', '1', '9', '5', '.', '.', '.'],
      ['.', '9', '8', '.', '.', '.', '.', '6', '.'],
      ['8', '.', '.', '.', '6', '.', '.', '.', '3'],
      ['4', '.', '.', '8', '.', '3', '.', '.', '1'],
      ['7', '.', '.', '.', '2', '.', '.', '.', '6'],
      ['.', '6', '.', '.', '.', '.', '2', '8', '.'],
      ['.', '.', '.', '4', '1', '9', '.', '.', '5'],
      ['.', '.', '.', '.', '8', '.', '.', '7', '9']], True),
    ([['8', '3', '.', '.', '7', '.', '.', '.', '.'],
      ['6', '.', '.', '1', '9', '5', '.', '.', '.'],
      ['.', '9', '8', '.', '.', '.', '.', '6', '.'],
      ['8', '.', '.', '.', '6', '.', '.', '.', '3'],
      ['4', '.', '.', '8', '.', '3', '.', '.', '1'],
      ['7', '.', '.', '.', '2', '.', '.', '.', '6'],
      ['.', '6', '.', '.', '.', '.', '2', '8', '.'],
      ['.', '.', '.', '4', '1', '9', '.', '.', '5'],
      ['.', '.', '.', '.', '8', '.', '.', '7', '9']], False),
    ([['.', '.', '4', '.', '.', '.', '6', '3', '.'],
      ['.', '.', '.', '.', '.', '.', '.', '.', '.'],
      ['5', '.', '.', '.', '.', '.', '.', '9', '.'],
      ['.', '.', '.', '5', '6', '.', '.', '.', '.'],
      ['4', '.', '3', '.', '.', '.', '.', '.', '1'],
      ['.', '.', '.', '7', '.', '.', '.', '.', '.'],
      ['.', '.', '.', '5', '.', '.', '.', '.', '.'],
      ['.', '.', '.', '.', '.', '.', '.', '.', '.'],
      ['.', '.', '.', '.', '.', '.', '.', '.', '.']], False),
]


@pytest.mark.parametrize('board, output', TEST_CASES)
def test(board: list[list[str]], output: bool):
    res = Solution().process(board)
    assert res == output
