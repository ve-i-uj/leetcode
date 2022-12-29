-- 94. Binary Tree Inorder Traversal
--
-- https://leetcode.com/problems/nth-highest-salary/

CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
  RETURN (
    WITH cte AS (
        SELECT
            e.Salary ,
            ROW_NUMBER() OVER(ORDER BY e.Salary DESC) n
        FROM Employee e
        GROUP BY e.Salary
        )
    SELECT
        e.Salary
    FROM cte e
    WHERE e.n = N
  );
END
