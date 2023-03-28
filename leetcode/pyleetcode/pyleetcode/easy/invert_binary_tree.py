"""226. Invert Binary Tree

https://leetcode.com/problems/invert-binary-tree/
"""

from __future__ import annotations
import collections
from typing import Optional, List, Any  # noqa: F401


class TreeNode:

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    @staticmethod
    def to_tree(lst: list[int]) -> TreeNode | None:
        if not lst:
            return None

        def to_tree_rec(n) -> TreeNode | None:
            if n > len(lst) - 1:
                return None
            node = TreeNode(lst[n])
            node.left = to_tree_rec(2* n + 1)
            node.right = to_tree_rec(2* n + 2)
            return node

        return to_tree_rec(0)

    @staticmethod
    def from_tree(root: TreeNode | None) -> list[int]:
        if root is None:
            return []

        res = []
        stack = collections.deque([root])
        while stack:
            node: TreeNode = stack.popleft()
            res.append(node.val)
            if node.left is not None:
                stack.append(node.left)
            if node.right is not None:
                stack.append(node.right)

        return res

    def __str__(self) -> str:
        return f'{self.__class__.__name__}(val={self.val})'

    __repr__ = __str__


class Solution:

    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None:
            return None

        stack = collections.deque([root])
        while stack:
            node: TreeNode = stack.popleft()
            if node.left is not None:
                stack.append(node.left)
            if node.right is not None:
                stack.append(node.right)
            node.left, node.right = node.right, node.left

        return root

    def process(self, *args, **kwargs):
        return self.invertTree(*args, **kwargs)
