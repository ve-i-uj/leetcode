"""Unit tests of "168. Excel Sheet Column Title".

https://leetcode.com/problems/excel-sheet-column-title/
"""

import pytest

from pyleetcode.easy.excel_sheet_column_title import Solution


TEST_CASES = [
    (1, 'A'),
    (28, 'AB'),
    (701, 'ZY'),
    (2147483647, 'FXSHRXW'),
    (52, 'AZ'),
]


@pytest.mark.parametrize('columnNumber, expected', TEST_CASES)
def test_excel_sheet_column_title(columnNumber: int, expected: str):
    res = Solution().process(columnNumber)
    assert res == expected
