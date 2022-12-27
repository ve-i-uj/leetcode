-- 94. Binary Tree Inorder Traversal
--
-- https://leetcode.com/problems/rank-scores/

SELECT
  s.score,
  DENSE_RANK() OVER(ORDER BY s.score DESC) "rank"
FROM Scores s
