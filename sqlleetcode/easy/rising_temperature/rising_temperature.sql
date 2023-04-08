-- 94. Binary Tree Inorder Traversal
--
-- https://leetcode.com/problems/rising-temperature/

SELECT w1.id
FROM Weather w1
  JOIN (
    SELECT id,
           DATE_ADD(recordDate, INTERVAL 1 DAY) "recordDate",
           temperature
    FROM Weather w
  ) w2 ON w1.recordDate = w2.recordDate
WHERE w1.temperature > w2.temperature
