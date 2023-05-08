-- 94. Binary Tree Inorder Traversal
--
-- https://leetcode.com/problems/human-traffic-of-stadium/

WITH cte AS (
  SELECT *,
         s.id - RANK() OVER(ORDER BY id) diff
  FROM Stadium s
  WHERE s.people > 99
)
SELECT id,
       visit_date,
       people
FROM cte
WHERE diff IN (
  SELECT diff
  FROM cte
  GROUP BY diff
  HAVING COUNT(diff) > 2
)
