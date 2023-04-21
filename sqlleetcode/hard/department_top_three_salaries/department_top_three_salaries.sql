-- 94. Binary Tree Inorder Traversal
--
-- https://leetcode.com/problems/department-top-three-salaries/

SELECT d.name "Department",
       e.name "Employee",
       e.salary "Salary"
FROM Employee e
  JOIN (
    SELECT e.departmentId,
           e.salary,
           ROW_NUMBER() OVER( PARTITION BY e.departmentId ORDER BY e.salary DESC ) AS "r_number"
    FROM Employee e
    GROUP BY e.departmentId, e.salary
  ) tops ON e.departmentId = tops.departmentId
    AND e.salary = tops.salary
  JOIN Department d
    ON d.id = e.departmentId
WHERE tops.r_number < 4
