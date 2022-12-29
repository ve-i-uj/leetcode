-- 94. Binary Tree Inorder Traversal
--
-- https://leetcode.com/problems/delete-duplicate-emails/

DELETE FROM Person
WHERE id NOT IN (
  SELECT
    MIN(p.id) id
  FROM (SELECT * FROM Person) p
  GROUP BY p.email
)
