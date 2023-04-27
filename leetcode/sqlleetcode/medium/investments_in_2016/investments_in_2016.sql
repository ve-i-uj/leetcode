-- 94. Binary Tree Inorder Traversal
--
-- https://leetcode.com/problems/investments-in-2016/

WITH cte AS (
  SELECT *,
         COUNT(*) OVER( PARTITION BY lon, lat ) > 1 AS "has_dup",
         COUNT(*) OVER( PARTITION BY tiv_2015 ) > 1 AS "equal_tiv"
  FROM Insurance
  ORDER BY pid
)
SELECT ROUND(SUM(tiv_2016), 2) "tiv_2016"
FROM cte
WHERE equal_tiv = 1
  AND has_dup = 0
