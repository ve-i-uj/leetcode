-- 94. Binary Tree Inorder Traversal
--
-- https://leetcode.com/problems/second-highest-salary/

SELECT (
  SELECT DISTINCT
    e.salary
  FROM Employee e
  ORDER BY e.salary DESC
  LIMIT 1, 1
) SecondHighestSalary
