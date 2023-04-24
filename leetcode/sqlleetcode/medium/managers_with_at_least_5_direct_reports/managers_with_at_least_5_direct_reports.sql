-- 94. Binary Tree Inorder Traversal
--
-- https://leetcode.com/problems/managers-with-at-least-5-direct-reports/

SELECT e1.name
FROM Employee e1
  JOIN (
    SELECT managerId,
           COUNT(*)
    FROM Employee e
    GROUP BY managerId
    HAVING COUNT(*) > 4
  ) e2 ON e1.id = e2.managerId
