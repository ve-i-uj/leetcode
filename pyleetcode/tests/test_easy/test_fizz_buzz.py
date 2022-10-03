"""Unit tests of "412. Fizz Buzz".

https://leetcode.com/problems/fizz-buzz/
"""

import pytest

from easy.fizz_buzz import Solution


TEST_CASES = [
    (3, ["1", "2", "Fizz"]),
    (5,  ["1", "2", "Fizz", "4", "Buzz"]),
    (15,  ["1", "2", "Fizz", "4", "Buzz", "Fizz", "7", "8", "Fizz", "Buzz", "11", "Fizz", "13", "14", "FizzBuzz"]),
]


@pytest.mark.parametrize('n, output', TEST_CASES)
def test(n, output):
    res = Solution().process(n)
    assert res == output
