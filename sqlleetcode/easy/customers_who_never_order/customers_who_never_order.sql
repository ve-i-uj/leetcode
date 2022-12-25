-- 94. Binary Tree Inorder Traversal
--
-- https://leetcode.com/problems/customers-who-never-order/

SELECT
  c.name Customers
FROM Customers c
WHERE c.id NOT IN (
  SELECT o.customerId
  FROM Orders o
)
