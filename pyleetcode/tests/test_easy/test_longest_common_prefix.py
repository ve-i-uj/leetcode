"""Unit tests of 14. Longest Common Prefix.

https://leetcode.com/problems/longest-common-prefix/
"""

import pytest

from easy.longest_common_prefix import Solution


TEST_CASES = [
    (['flower', 'flow', 'flight'], 'fl'),
    (['dog', 'disk', 'doom'], 'd'),
    (['dog', '', 'doom'], 'do'),
    (['dog', 'racecar', 'car'], ''),
]


@pytest.mark.parametrize("strs,res", TEST_CASES)
def test_1(strs: list[str], res: bool):
    assert Solution().process(strs) == res


def test_benchmark_longest_common_prefix(benchmark):
    solution = Solution()

    def process():
        for strs, _res in TEST_CASES:
            solution.process(strs)

    benchmark(process)
