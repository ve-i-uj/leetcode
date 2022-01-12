"""Unit tests of `20. Valid Parentheses`.

https://leetcode.com/problems/valid-parentheses/
"""

import pytest

from easy.longest_common_prefix import Solution


TEST_CASES = [
    (['flower', 'flow', 'flight'], 'fl'),
    (['dog', 'racecar', 'car'], ''),
]


@pytest.mark.parametrize("strs,res", TEST_CASES)
def test_1(strs: list[str], res: bool):
    assert Solution().process(strs) is res


def test_benchmark(benchmark):
    solution = Solution()

    def process():
        for strs, _res in TEST_CASES:
            solution.process(strs)

    benchmark(process)
