-- 94. Binary Tree Inorder Traversal
--
-- https://leetcode.com/problems/duplicate-emails/

SELECT
  email Email
FROM Person p
GROUP BY p.email
HAVING COUNT(email) > 1