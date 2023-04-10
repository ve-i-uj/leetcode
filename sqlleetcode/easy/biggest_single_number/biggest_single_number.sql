-- 94. Binary Tree Inorder Traversal
--
-- https://leetcode.com/problems/biggest-single-number/

SELECT IFNULL((
  SELECT num
  FROM MyNumbers mn
  GROUP BY num
  HAVING COUNT(num) = 1
  ORDER BY num DESC
  LIMIT 1
), 'null'
) num
