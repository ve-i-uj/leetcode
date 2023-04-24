-- 94. Binary Tree Inorder Traversal
--
-- https://leetcode.com/problems/consecutive-numbers/

SELECT DISTINCT l1.num "ConsecutiveNums"
FROM Logs l1
  JOIN Logs l2
    ON l1.id = l2.id - 1
  JOIN Logs l3
    ON l1.id = l3.id - 2
WHERE l1.num = l2.num
  AND l1.num = l3.num