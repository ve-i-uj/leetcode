-- 94. Binary Tree Inorder Traversal
--
-- https://leetcode.com/problems/rank-scores/

SELECT
  s.score,
  r.rank
FROM Scores s
  JOIN (
    SELECT
      ROW_NUMBER() OVER(ORDER BY r.score DESC) "rank" ,
      r.score
    FROM Scores r
    GROUP BY r.score
    ORDER BY r.score DESC
  ) r
    ON s.score = r.score
ORDER BY s.score DESC
