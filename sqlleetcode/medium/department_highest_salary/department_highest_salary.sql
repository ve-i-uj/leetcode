-- 94. Binary Tree Inorder Traversal
--
-- https://leetcode.com/problems/department-highest-salary/

SELECT
  d.name Department,
  e2.name Employee,
  e2.salary Salary
FROM Employee e2
  JOIN (
    SELECT
      MAX(e.salary) salary,
      e.departmentId departmentId
    FROM Employee e
    GROUP BY e.departmentId
  ) e1
  ON e2.salary = e1.salary
    AND e2.departmentId = e1.departmentId
  JOIN Department d
    ON e2.departmentId = d.id
