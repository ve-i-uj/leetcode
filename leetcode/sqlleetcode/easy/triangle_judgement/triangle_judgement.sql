-- 94. Binary Tree Inorder Traversal
--
-- https://leetcode.com/problems/triangle-judgement/

SELECT *,
       IF(x + y > z AND x + z > y AND z + y > x, "Yes", "No") "triangle"
FROM Triangle
