-- 94. Binary Tree Inorder Traversal
--
-- https://leetcode.com/problems/human-traffic-of-stadium/

WITH cte AS (
  SELECT *,
         s1.people >= 100 AS value
  FROM Stadium s1
), islands AS (
  SELECT t1.id,
         t1.visit_date,
         t1.people,
         t1.id - ROW_NUMBER() OVER ( ORDER BY id ) AS 'diff'
  FROM cte t1
    LEFT OUTER JOIN cte t2
      ON t1.value = t2.value - 1
  WHERE t2.value IS NULL
), mx_mn AS (
  SELECT *,
         MAX(id) OVER( PARTITION BY diff ) AS mx,
         MIN(id) OVER( PARTITION BY diff ) AS mn
  FROM islands
)
SELECT id,
       visit_date,
       people
FROM mx_mn
WHERE mx - mn + 1 >= 3
ORDER BY visit_date
