"""111. Minimum Depth of Binary Tree

https://leetcode.com/problems/minimum-depth-of-binary-tree/
"""

from __future__ import annotations

import sys
from typing import Optional

OptionalInts = list[Optional[int]]

NO_RES = sys.maxsize

class TreeNode:

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    @classmethod
    def create(cls, lst: OptionalInts) -> Optional[TreeNode]:
        if not lst:
            return None

        i = 0
        mult = 2

        val = lst[i]
        if val is None:
            return None

        root = TreeNode(val)
        stack: list[tuple[int, int, TreeNode]] = [(i, mult, root)]
        while stack:
            i, mult, node = stack.pop()

            l_i = i * mult + 1
            r_i = i * mult + 2

            l_val = None if l_i >= len(lst) else lst[l_i]
            r_val = None if r_i >= len(lst) else lst[r_i]

            if l_val is None and r_val is None:
                # It's a leaf
                continue

            if l_val is None or r_val is None:
                mult = 1
            else:
                mult = 2

            if l_val is not None:
                node.left = TreeNode(l_val)
                stack.append((l_i, mult, node.left))
            if r_val is not None:
                node.right = TreeNode(r_val)
                stack.append((r_i, mult, node.right))

        return root


    def __str__(self) -> str:
        return f'{self.__class__.__name__}(val={self.val})'

    __repr__ = __str__


class Solution:

    def process(self, *args, **kwargs):  # noqa: N802
        return self.minDepth(*args, **kwargs)

    def minDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0

        res = NO_RES
        stack: list[tuple[int, TreeNode]] = [(1, root)]
        while stack:
            depth, node = stack.pop()
            if depth > res:
                continue

            if node.left is None and node.right is None:
                # It's a leaf
                res = min(res, depth)
                continue

            if node.left is not None:
                stack.append((depth + 1, node.left))
            if node.right is not None:
                stack.append((depth + 1, node.right))

        return res
