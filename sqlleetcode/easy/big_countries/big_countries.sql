-- 94. Binary Tree Inorder Traversal
--
-- https://leetcode.com/problems/big-countries/

SELECT name,
       population,
       area
FROM World w
WHERE area > 3000000
  OR population > 25000000
