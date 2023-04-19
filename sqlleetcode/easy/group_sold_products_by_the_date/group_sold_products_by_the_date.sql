-- 94. Binary Tree Inorder Traversal
--
-- https://leetcode.com/problems/group-sold-products-by-the-date/

SELECT DISTINCT sell_date,
       COUNT(DISTINCT product) AS "num_sold",
       GROUP_CONCAT(DISTINCT product ORDER BY product) AS "products"
FROM Activities a
GROUP BY sell_date
