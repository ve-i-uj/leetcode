-- 94. Binary Tree Inorder Traversal
--
-- https://leetcode.com/problems/friend-requests-ii/

WITH reqs AS (
  SELECT requester_id AS id,
         COUNT(requester_id) cnt
  FROM RequestAccepted t1
  GROUP BY requester_id
), accs AS (
  SELECT accepter_id AS id,
         COUNT(accepter_id) cnt
  FROM RequestAccepted ra
  GROUP BY accepter_id
)
SELECT id,
       SUM(cnt) num
FROM (
  SELECT *
  FROM reqs
    UNION ALL
  SELECT *
  FROM accs
) res
GROUP BY id
ORDER BY SUM(cnt) DESC
LIMIT 1
