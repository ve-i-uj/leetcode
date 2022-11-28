"""Unit tests of "108. Convert Sorted Array to Binary Search Tree".

https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/
"""

import pytest

from pyleetcode.easy.convert_sorted_array_to_binary_search_tree import Solution, TreeNode


TEST_CASES = [
    ([-10, -3, 0, 5, 9], TreeNode.from_list([0, -3, 9, -10, None, 5])),
    ([1, 3], TreeNode.from_list([3, 1])),
]


@pytest.mark.parametrize('nums, output', TEST_CASES)
def test(nums: list[int], output: TreeNode):
    res = Solution().process(nums)
    assert res == output
