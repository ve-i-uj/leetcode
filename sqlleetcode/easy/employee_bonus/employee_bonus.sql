-- 94. Binary Tree Inorder Traversal
--
-- https://leetcode.com/problems/employee-bonus/

SELECT e.name,
       b.bonus
FROM Employee e
  LEFT OUTER JOIN Bonus b
    ON e.empId = b.empId
WHERE b.bonus < 1000
  OR b.bonus IS NULL
