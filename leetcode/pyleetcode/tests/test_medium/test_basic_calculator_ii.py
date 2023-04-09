'''Unit tests of '227. Basic Calculator II'.

https://leetcode.com/problems/basic-calculator-ii/
'''

import pytest

from pyleetcode.medium.basic_calculator_ii import Solution


TEST_CASES = [
    ('1 + 2 + 3 - 4', 2),
    ('1 * 2 * 3 / 2', 3),
    ('1 * 2 * 3', 6),
    ('1 + 2 * 3', 7),
    ('1 + 2 * 3 / 4 + 5', 7),
    ('3+2*2', 7),
    (' 3/2 ', 1),
    (' 3+5 / 2 ', 5),
    ('5   ', 5),
    ('    99  ', 99),
    ('0-2147483647', -2147483647),
]


@pytest.mark.parametrize('s, output', TEST_CASES)
def test(s: str, output: int):
    res = Solution().process(s)
    assert res == output
