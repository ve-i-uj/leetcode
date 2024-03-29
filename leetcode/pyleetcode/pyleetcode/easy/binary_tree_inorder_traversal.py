"""94. Binary Tree Inorder Traversal

https://leetcode.com/problems/binary-tree-inorder-traversal/
"""

from __future__ import annotations

from typing import Optional, List, Union  # noqa: F401


class TreeNode:

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    @classmethod
    def new(cls, vals: list[Union[int, None]]) -> Optional[TreeNode]:
        if len(vals) == 0:
            return None

        def new(i: int) -> Optional[TreeNode]:
            if i >= len(vals) or vals[i] is None:
                return None
            node = TreeNode(vals[i])
            node.left = new(i * 2 + 1)
            node.right = new(i * 2 + 2)
            return node

        return new(0)

    @staticmethod
    def normalize_data(vals: list[Optional[int]]):
        i = 0
        while i < len(vals):
            if vals[i] is None:
                l_i = i * 2 + 1
                r_i = i * 2 + 2
                if l_i < len(vals) and vals[l_i] is not None:
                    vals.insert(l_i, None)
                if r_i < len(vals) and vals[r_i] is not None:
                    vals.insert(r_i, None)
            i += 1

    def __str__(self) -> str:
        return str(self.val)

    def __repr__(self) -> str:
        return str(self)


class Solution:

    def process(self, *args, **kwargs):  # noqa: N802
        return self.inorderTraversal(*args, **kwargs)

    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        stack = []
        res = []
        while root is not None or stack:
            while root is not None:
                stack.append(root)
                root = root.left
            root = stack.pop()
            res.append(root.val)
            root = root.right

        return res
