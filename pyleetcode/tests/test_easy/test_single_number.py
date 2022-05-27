"""Unit tests of "136. Single Number".

https://leetcode.com/problems/single-number/
"""

import pytest

from easy.single_number import Solution


TEST_CASES = [
    ([2, 2, 1], 1),
    ([4, 1, 2, 1, 2], 4),
    ([1], 1),
]


@pytest.mark.parametrize('nums, output', TEST_CASES)
def test(nums: list[int], output: int):
    assert output == Solution().process(nums)
