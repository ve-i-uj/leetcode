-- 94. Binary Tree Inorder Traversal
--
-- https://leetcode.com/problems/second-highest-salary/

SELECT MAX((
  SELECT
    e.salary
  FROM Employee e
  WHERE e.salary < (
    SELECT
      MAX(e.salary)
    FROM Employee e
  )
  ORDER BY e.salary DESC
  LIMIT 1
)) SecondHighestSalary
