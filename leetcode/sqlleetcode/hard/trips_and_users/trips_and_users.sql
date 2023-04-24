-- 94. Binary Tree Inorder Traversal
--
-- https://leetcode.com/problems/trips-and-users/

WITH total AS (
  SELECT t.id,
         t.status,
         t.request_at
  FROM Trips t
    JOIN Users u1
      ON t.client_id = u1.users_id
    JOIN Users u2
      ON t.driver_id = u2.users_id
  WHERE t.request_at BETWEEN '2013-10-01' AND '2013-10-03'
    AND u1.banned = 'No'
    AND u2.banned = 'No'
)
SELECT t.request_at "Day",
       ROUND( (SUM(1) - SUM(t.status = 'completed')) / SUM(1), 2 ) AS "Cancellation Rate"
FROM total t
GROUP BY t.request_at
