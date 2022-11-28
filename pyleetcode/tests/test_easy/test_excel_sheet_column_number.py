"""Unit tests of "171. Excel Sheet Column Number".

https://leetcode.com/problems/excel-sheet-column-number/
"""

import pytest

from pyleetcode.easy.excel_sheet_column_number import Solution


TEST_CASES = [
    ("A", 1),
    ("AB", 28),
    ("ZY", 701),
    ("FXSHRXW", 2147483647),
]


@pytest.mark.parametrize('title, output', TEST_CASES)
def test(title: str, output: int):
    res = Solution().process(title)
    assert res == output
