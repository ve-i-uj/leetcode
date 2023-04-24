-- 94. Binary Tree Inorder Traversal
--
-- https://leetcode.com/problems/list-the-products-ordered-in-a-period/

SELECT *
FROM (
  SELECT p.product_name,
         SUM(o.unit) "unit"
  FROM Orders o
    JOIN Products p
      ON o.product_id = p.product_id
  WHERE order_date BETWEEN CAST('2020-02-01' AS DATE)
    AND CAST('2020-02-29' AS DATE)
  GROUP BY p.product_name
) s
WHERE s.unit >= 100
