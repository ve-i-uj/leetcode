"""Unit tests of 21. Merge Two Sorted Lists

https://leetcode.com/problems/merge-two-sorted-lists/
"""

import pytest

from easy.merge_two_sorted_lists import Solution


TEST_CASES = [
    ([1, 2, 4], [1, 3, 4], [1, 1, 2, 3, 4, 4]),
    ([], [], []),
]


@pytest.mark.parametrize('list1, list2, res', TEST_CASES)
def test_1(list1: list, list2: list, res: list):
    assert Solution().process(list1, list2) == res


def test_merge_two_sorted_lists(benchmark):
    solution = Solution()

    def process():
        for list1, list2, _res in TEST_CASES:
            solution.process(list1, list2)

    benchmark(process)
