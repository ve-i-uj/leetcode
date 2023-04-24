-- 94. Binary Tree Inorder Traversal
--
-- https://leetcode.com/problems/find-total-time-spent-by-each-employee/

SELECT event_day "day",
       emp_id,
       SUM(out_time - in_time) "total_time"
FROM Employees e
GROUP BY emp_id, event_day
