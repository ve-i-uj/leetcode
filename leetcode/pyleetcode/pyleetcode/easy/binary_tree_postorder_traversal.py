"""145. Binary Tree Postorder Traversal

https://leetcode.com/problems/binary-tree-postorder-traversal/
"""

from __future__ import annotations

from typing import Optional, List


class TreeNode:

    def __init__(self, val=0, left: Optional[TreeNode] = None,
                 right: Optional[TreeNode] = None):
        self.val = val
        self.left = left
        self.right = right

    @staticmethod
    def normalize_vals(vals: list[Optional[int]]) -> list[Optional[int]]:
        i = 0
        if not vals or vals[i] is None:
            return []

        res = vals[:]
        stack = []
        while i < len(vals):
            if vals[i] is None:
                i1 = 2 * i + 1
                i2 = 2 * i + 2
                if i1 < len(res):
                    res.insert(i1, None)
                if i2 < len(res):
                    res.insert(i2, None)
            i += 1

        return res

    @staticmethod
    def to_tree(vals: list[Optional[int]]) -> Optional[TreeNode]:
        vals[:] = TreeNode.normalize_vals(vals)
        i = 0
        if not vals or vals[i] is None:
            return None

        val = vals[i]
        assert val is not None
        root = TreeNode(val)
        stack: list[tuple[int, TreeNode]] = [(i, root)]
        while stack:
            i, node = stack.pop()
            i1 = 2 * i + 1
            i2 = 2 * i + 2
            if i1 < len(vals) and vals[i1] is not None:
                node.left = TreeNode(vals[i1])
                stack.append((i1, node.left))
            if i2 < len(vals) and vals[i2] is not None:
                node.right = TreeNode(vals[i2])
                stack.append((i2, node.right))

        return root

    def __str__(self) -> str:
        return f'{self.__class__.__name__}(val={self.val})'

    __repr__ = __str__


class Solution:

    def process(self, *args, **kwargs) -> List[int]:
        return self.postorderTraversal(*args)

    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []

        stack: list[Optional[TreeNode]] = [root]
        res = []
        while stack:
            node = stack.pop()
            if node is None:
                continue
            if node.left is None and node.right is None:
                res.append(node.val)
                continue
            left = node.left
            right = node.right
            node.left, node.right = None, None

            stack.append(node)
            stack.append(right)
            stack.append(left)

        return res
