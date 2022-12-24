"""114. Flatten Binary Tree to Linked List

https://leetcode.com/problems/flatten-binary-tree-to-linked-list/
"""
from __future__ import annotations

from typing import Optional


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
            parent = nodes[i // 2]
            assert parent is not None
            is_left = (i % 2 == 0)
            if is_left:
                parent.left = TreeNode(v)
                nodes.append(parent.left)
            else:
                parent.right = TreeNode(v)
                nodes.append(parent.right)

        return root

    def __str__(self) -> str:
        return f'{self.__class__.__name__}(val={self.val})'

    __repr__ = __str__


class Solution:

    def process(self, *args, **kwargs):
        return self.flatten(*args, **kwargs)

    def flatten(self, root: Optional[TreeNode]):
        if not root:
            return

        stack = [root]
        while stack:
            node = stack.pop()
            if node.left is not None:
                curr: TreeNode = node.left
                while curr.right is not None:
                    curr = curr.right
                curr.right = node.right
                node.right = node.left
                node.left = None
            if node.right is not None:
                stack.append(node.right)
