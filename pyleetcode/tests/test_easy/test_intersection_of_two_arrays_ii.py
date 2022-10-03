"""Unit tests of "350. Intersection of Two Arrays II".

https://leetcode.com/problems/intersection-of-two-arrays-ii/
"""

import pytest

from easy.intersection_of_two_arrays_ii import Solution


TEST_CASES = [
    ([1, 2, 2, 1],  [2, 2],  [2, 2]),
    ([4, 9, 5],  [9, 4, 9, 8, 4],  [4, 9]),
    ([1, 2], [1, 1],  [1]),
]


@pytest.mark.parametrize('nums1, nums2, output', TEST_CASES)
def test(nums1, nums2, output):
    res = Solution().process(nums1, nums2)
    assert set(res) == set(output)
