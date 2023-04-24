-- 94. Binary Tree Inorder Traversal
--
-- https://leetcode.com/problems/customer-placing-the-largest-number-of-orders/

WITH c AS (
  SELECT customer_number,
         COUNT(customer_number) "count"
  FROM orders o
  GROUP BY customer_number
  HAVING COUNT(customer_number)
)
SELECT customer_number
FROM c
WHERE c.count = (
  SELECT MAX(c.count) "max_c"
  FROM c
)
