-- 94. Binary Tree Inorder Traversal
--
-- https://leetcode.com/problems/department-top-three-salaries/

EXPLAIN
WITH cte AS (
  SELECT d.name "Department",
         e.name "Employee",
         e.salary "Salary",
         DENSE_RANK() OVER( PARTITION BY d.id ORDER BY e.salary DESC ) AS "rnk"
  FROM Department d
    JOIN Employee e
      ON d.id = e.departmentId
)
SELECT Department,
       Employee,
       Salary
FROM cte
WHERE cte.rnk < 4
