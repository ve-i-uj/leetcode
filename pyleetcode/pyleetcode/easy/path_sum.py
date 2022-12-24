"""112. Path Sum

https://leetcode.com/problems/path-sum/
"""
from __future__ import annotations

from typing import Optional, List, Any  # noqa: F401


class TreeNode:

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    @classmethod
    def create(cls, lst: list[Optional[int]]) -> Optional[TreeNode]:
        if not lst:
            return None

        val = lst[0]
        if val is None:
            return None

        i = 0
        root = TreeNode(val)
        stack: list[tuple[int, TreeNode]] = [(i, root)]

        while stack:
            i, node = stack.pop()
            li = i * 2 + 1
            ri = i * 2 + 2

            if li < len(lst) and lst[li] is not None:
                node.left = TreeNode(lst[li])
            if ri < len(lst) and lst[ri] is not None:
                node.right = TreeNode(lst[ri])

            if node.left is not None:
                stack.append((li, node.left))
            if node.right is not None:
                stack.append((ri, node.right))

        return root

    def __repr__(self) -> str:
        return f'{self.__class__.__name__}(val={self.val})'


class Solution:

    def process(self, *args, **kwargs):
        return self.hasPathSum(*args, **kwargs)

    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if root is None:
            return False

        stack: list[tuple[int, TreeNode]] = [(root.val, root)]
        while stack:
            sum_, node = stack.pop()
            if node.left is None and node.right is None and sum_ == targetSum:
                return True

            if node.left is not None:
                stack.append((sum_ + node.left.val, node.left))
            if node.right is not None:
                stack.append((sum_ + node.right.val, node.right))

        return False
