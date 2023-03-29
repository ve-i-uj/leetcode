"""543. Diameter of Binary Tree

https://leetcode.com/problems/diameter-of-binary-tree/
"""

from __future__ import annotations
import collections
from typing import Optional, Deque  # noqa: F401


class TreeNode:

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    @staticmethod
    def to_tree(lst: list[int]) -> TreeNode | None:
        if not lst:
            return None

        n = 0
        root = TreeNode(lst[n])
        stack: Deque[tuple[TreeNode, int]] = collections.deque([(root, n)])
        cntr = 1
        while stack:
            node, n = stack.popleft()
            l_n = 2 * n + 1
            r_n = 2 * n + 2
            if l_n < len(lst) and lst[l_n] is not None:
                node.left = TreeNode(lst[l_n])
                stack.append((node.left, l_n))
            if r_n < len(lst) and lst[r_n] is not None:
                node.right = TreeNode(lst[r_n])
                stack.append((node.right, r_n))

        return root

    @staticmethod
    def from_tree(root: TreeNode | None) -> list[int]:
        if root is None:
            return []

        res = []
        stack = collections.deque([root])
        while stack:
            node = stack.popleft()
            res.append(node.val)
            if node.left is not None:
                stack.append(node.left)
            if node.right is not None:
                stack.appendleft(node.right)

        return res

    def __str__(self) -> str:
        return f'{self.__class__.__name__}(val={self.val})'

    __repr__ = __str__


class Solution:

    def __init__(self) -> None:
        self._res: int = 0

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if root is None or (root.left is None and root.right is None):
            return 0

        def get_max_height(node: TreeNode | None) -> int:
            if node is None:
                return 0

            l_h = get_max_height(node.left)
            r_h = get_max_height(node.right)

            self._res = max(l_h + r_h, self._res)

            return 1 + max(l_h, r_h)

        get_max_height(root)

        return self._res

    def process(self, *args, **kwargs):  # noqa: N802
        return self.diameterOfBinaryTree(*args, **kwargs)
