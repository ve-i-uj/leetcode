-- 94. Binary Tree Inorder Traversal
--
-- https://leetcode.com/problems/consecutive-numbers/

SELECT DISTINCT l.num "ConsecutiveNums"
FROM Logs l
  JOIN (
    SELECT l1.id,
           l1.num
    FROM Logs l1
      JOIN Logs l2
        ON l1.id = l2.id + 1
    WHERE l1.num = l2.num
  ) sl
    ON l.id = sl.id + 1
WHERE l.num = sl.num
