"""144. Binary Tree Preorder Traversal

https://leetcode.com/problems/binary-tree-preorder-traversal/
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

        root = TreeNode(val)
        nodes = [root]
        for i, v in enumerate(lst[1:]):
            if v is None:
                continue

            parent_i = i // 2
            is_left = (i % 2 == 0)

            parent = nodes[parent_i]
            node = TreeNode(v)
            if is_left:
                parent.left = node
            else:
                parent.right = node
            nodes.append(node)

        return root

    def __str__(self) -> str:
        return f'{self.__class__.__name__}(val={self.val})'

    __repr__ = __str__


class Solution:

    def process(self, *args, **kwargs):
        return self.preorderTraversal(*args, **kwargs)

    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []

        res = []
        stack = [root]
        while stack:
            node = stack.pop()
            res.append(node.val)
            if node.right is not None:
                stack.append(node.right)
            if node.left is not None:
                stack.append(node.left)

        return res
