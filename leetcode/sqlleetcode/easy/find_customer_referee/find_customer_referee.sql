-- 94. Binary Tree Inorder Traversal
--
-- https://leetcode.com/problems/find-customer-referee/

SELECT name
FROM Customer
WHERE IFNULL(referee_id, 0) != 2
