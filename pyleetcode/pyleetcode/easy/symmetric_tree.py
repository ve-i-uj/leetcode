"""101. Symmetric Tree

https://leetcode.com/problems/symmetric-tree/
"""
from __future__ import annotations
from typing import Optional, Union, Any  # noqa: F401


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

    def __str__(self) -> str:
        return str(self.val)

    def __repr__(self) -> str:
        return str(self)


class Solution:

    def isSymmetric(self, root: Optional[TreeNode]) -> bool:  # noqa: N802
        l_stack: list[TreeNode] = [root.left]
        r_stack: list[TreeNode] = [root.right]
        while l_stack and r_stack:
            l_node = l_stack.pop()
            r_node = r_stack.pop()
            if l_node is None and r_node is None:
                continue

            if l_node is None and r_node is not None:
                return False
            if l_node is not None and r_node is None:
                return False

            if l_node.val != r_node.val:
                return False
            l_stack.append(l_node.right)
            l_stack.append(l_node.left)
            r_stack.append(r_node.left)
            r_stack.append(r_node.right)

        return True

    def process(self, *args, **kwargs) -> bool:  # noqa: N802
        return self.isSymmetric(*args, **kwargs)
