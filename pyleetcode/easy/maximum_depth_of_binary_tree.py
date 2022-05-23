"""104. Maximum Depth of Binary Tree

https://leetcode.com/problems/maximum-depth-of-binary-tree/
"""

from typing import Optional, List, Any  # noqa: F401


class TreeNode:

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        stack = [(1, root)]
        max_depth = 1
        while stack:
            depth, node = stack.pop()
            max_depth = max(max_depth, depth)
            if node.left is not None:
                stack.append((depth + 1, node.left))
            if node.right is not None:
                stack.append((depth + 1, node.right))

        return max_depth

    def process(self, *args, **kwargs) -> int:  # noqa: N802
        return self.maxDepth(*args, **kwargs)
