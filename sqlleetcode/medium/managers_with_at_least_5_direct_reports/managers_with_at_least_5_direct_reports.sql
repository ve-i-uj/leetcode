-- 94. Binary Tree Inorder Traversal
--
-- https://leetcode.com/problems/managers-with-at-least-5-direct-reports/

SELECT e2.name
FROM Employee e1
  JOIN Employee e2
    ON e1.managerId = e2.id
GROUP BY e2.name
HAVING COUNT(*) > 4
