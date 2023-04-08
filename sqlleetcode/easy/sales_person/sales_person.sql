-- 94. Binary Tree Inorder Traversal
--
-- https://leetcode.com/problems/sales-person/

SELECT name
FROM SalesPerson sp
WHERE sp.name NOT IN (
  SELECT sp.name
  FROM SalesPerson sp
    JOIN Orders o
      ON sp.sales_id = o.sales_id
    JOIN Company c
      ON c.com_id = o.com_id
  WHERE c.name = "RED"
)
