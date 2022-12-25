-- 94. Binary Tree Inorder Traversal
--
-- https://leetcode.com/problems/duplicate-emails/

SELECT
  email Email
FROM (
  SELECT
  	email,
  	COUNT(email) cnt
  FROM Person
  GROUP BY email
) g
WHERE g.cnt > 1
