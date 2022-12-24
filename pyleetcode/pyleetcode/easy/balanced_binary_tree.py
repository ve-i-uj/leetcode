"""110. Balanced Binary Tree

https://leetcode.com/problems/balanced-binary-tree/
"""

from __future__ import annotations

from typing import Optional


class TreeNode:

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    @classmethod
    def new(cls, lst: list[Optional[int]]) -> Optional[TreeNode]:

        def create_node(i, lst) -> Optional[TreeNode]:
            if i >= len(lst):
                return None
            if lst[i] is None:
                return None

            node = TreeNode(lst[i])
            node.left = create_node(i * 2 + 1, lst)
            node.right = create_node(i * 2 + 2, lst)

            return node

        return create_node(0, lst)


class NotBalancedError(Exception):
    pass


class Solution:

    def process(self, *args, **kwargs):
        return self.isBalanced(*args, **kwargs)

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True

        def get_height(node: Optional[TreeNode]) -> int:
            if node is None:
                return 0

            left = get_height(node.left)
            right = get_height(node.right)

            if abs(left - right) > 1:
                raise NotBalancedError

            return 1 + max(left, right)

        try:
            get_height(root)
        except NotBalancedError:
            return False

        return True
