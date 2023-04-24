-- 94. Binary Tree Inorder Traversal
--
-- https://leetcode.com/problems/game-play-analysis-iv/

SELECT ROUND( COUNT(t2.player_id) / COUNT(t1.player_id), 2 ) AS "fraction"
FROM (
  SELECT player_id,
         MIN(event_date) AS event_date
  FROM Activity
  GROUP BY player_id
) t1 LEFT JOIN Activity t2
  ON t1.player_id = t2.player_id
    AND DATE_ADD(t1.event_date, INTERVAL 1 DAY) = t2.event_date
